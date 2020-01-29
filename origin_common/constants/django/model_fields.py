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
from origin_common.constants.adjustments import Adjustment
from origin_common.constants.base import Constant, Constants
from origin_common.constants.business_day_conventions import BusinessDayConvention
from origin_common.constants.day_counts import DayCount
from origin_common.constants.funding_bases import FundingBasis
from origin_common.constants.payment_frequencies import PaymentFrequency
from origin_common.constants.tenors import Tenor

T = TypeVar("T")


class ConstantDescriptor:
    """
    The descriptor for the constant attribute on the model instance.
    Returns a Constant when accessed so you can do stuff like::

        >>> instance.constant.label

    Assigns a phone number object on assignment so you can do::

        >>> instance.constant = Constant(...)
    or
        >>> instance.constant = 'foobar'
    """

    def __init__(self, field: "ConstantField"):
        self.field = field

    def __get__(self, instance: models.Model = None, cls=None) -> Constant:
        if instance is None:
            return self
        return instance.__dict__[self.field.name]

    def __set__(self, instance: models.Model, value: Union[Constant, T, None]):
        instance.__dict__[self.field.name] = self.field.to_python(value)


class ConstantField(Generic[T], models.Field):
    attr_class: type(Constant) = None
    base_type: type = str
    constants: Constants = None
    descriptor_class = ConstantDescriptor
    description: str = "A single immutable constant"
    type_mappings: Dict[type, models.Field] = {
        str: models.CharField,
        int: models.IntegerField,
        timedelta: models.DurationField,
    }

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
        try:
            constant = self.constants[value]
        except KeyError:
            if value in {None, ""}:
                # for nullable/blank values
                return value
            raise ValidationError(f"Invalid input: '{value}' is not a valid constant.")
        else:
            constant.make_immutable()
            return constant

    def get_prep_value(self, value: Union[Constant, T, None]) -> Union[T, None]:
        if isinstance(value, Constant):
            return value.value
        return value

    def _get_flatchoices(self):
        flatchoices = super()._get_flatchoices()
        flatchoices.extend((constant, constant.label) for constant in self.constants)
        return flatchoices

    flatchoices = property(_get_flatchoices)


class AdjustmentField(ConstantField[str]):
    attr_class = Adjustment
    constants = ADJUSTMENTS


class BusinessDayConventionField(ConstantField[str]):
    attr_class = BusinessDayConvention
    constants = BUSINESS_DAY_CONVENTIONS


class DayCountField(ConstantField[str]):
    attr_class = DayCount
    constants = DAY_COUNTS


class FundingBasisField(ConstantField[str]):
    attr_class = FundingBasis
    constants = FUNDING_BASES


class PaymentFrequencyField(ConstantField[int]):
    attr_class = PaymentFrequency
    constants = PAYMENT_FREQUENCIES
    base_type = int


class TenorField(ConstantField[timedelta]):
    attr_class = Tenor
    constants = TENORS
    base_type = timedelta
