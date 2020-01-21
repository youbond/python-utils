from datetime import timedelta
from typing import Dict, Generic, List, Tuple, TypeVar, Union

from django.core.exceptions import ValidationError
from django.db import models

from origin_common.constants import (
    ADJUSTMENTS,
    BUSINESS_DAY_CONVENTIONS,
    DAY_COUNTS,
    FUNDING_BASES,
    PAYMENT_FREQUENCIES,
    TENORS,
)
from origin_common.constants.base import Constant, Constants

T = TypeVar("T")


class ConstantField(Generic[T], models.Field):
    description = "A single immutable constant"  # type: str
    constants = None  # type: Constants
    base_type = str  # type: type
    type_mappings = {
        str: models.CharField,
        int: models.IntegerField,
        timedelta: models.DurationField,
    }  # type: Dict[type, models.Field]

    def __init__(self, *args, **kwargs):
        if "choices" not in kwargs:
            kwargs["choices"] = self.constants.to_django_choices()
        if "max_length" not in kwargs and self.base_type == str:
            kwargs["max_length"] = max(len(x) for x, _ in kwargs["choices"])
        super().__init__(*args, **kwargs)

    def deconstruct(self) -> Tuple[str, str, List, Dict]:
        name, path, args, kwargs = super().deconstruct()
        if tuple(kwargs["choices"]) == self.constants.to_django_choices():
            del kwargs["choices"]
        return name, path, args, kwargs

    def get_internal_type(self) -> str:
        return self.type_mappings[self.base_type].__name__

    def to_python(self, value: Union[None, T]) -> Union[Constant, None]:
        if value is None:
            # for nullable values
            return None
        try:
            constant = self.constants[value]
        except KeyError:
            raise ValidationError(
                "Invalid input: '{}' is not a valid constant.".format(value)
            )
        else:
            constant.make_immutable()
            return constant

    def get_prep_value(self, value: Union[Constant, T, None]) -> Union[T, None]:
        if isinstance(value, Constant):
            return value.value
        return value


class AdjustmentField(ConstantField[str]):
    constants = ADJUSTMENTS


class BusinessDayConventionField(ConstantField[str]):
    constants = BUSINESS_DAY_CONVENTIONS


class DayCountField(ConstantField[str]):
    constants = DAY_COUNTS


class FundingBasisField(ConstantField[str]):
    constants = FUNDING_BASES


class PaymentFrequencyField(ConstantField[int]):
    constants = PAYMENT_FREQUENCIES
    base_type = int


class TenorField(ConstantField[timedelta]):
    constants = TENORS
    base_type = timedelta
