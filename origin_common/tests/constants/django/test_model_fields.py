from datetime import timedelta
from random import choice
from unittest import TestCase

import django
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from origin_common.constants import (
    ADJUSTMENTS,
    BUSINESS_DAY_CONVENTIONS,
    CURRENCIES,
    DAY_COUNTS,
    FUNDING_BASES,
    PAYMENT_FREQUENCIES,
    TENORS,
)
from origin_common.constants.base import Constants
from origin_common.constants.django.model_fields import (
    AdjustmentField,
    BusinessDayConventionField,
    ConstantField,
    CurrencyField,
    DayCountField,
    FundingBasisField,
    PaymentFrequencyField,
    TenorField,
)

# needed to create models
settings.configure()
django.setup()


class ConstantFieldTestBase:
    field_cls: type(ConstantField) = None
    constants: Constants = None
    base_type: type = None
    base_model_field: type(models.Field) = None

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        assert cls.field_cls is not None, "Set field class"

        class TestModel(models.Model):
            foo = cls.field_cls()

            class Meta:
                app_label = "test"

        cls.TestModel = TestModel

    def setUp(self) -> None:
        super().setUp()
        self.field: ConstantField = self.field_cls()

    def test_choices(self):
        expected = self.constants.to_django_choices()
        assert self.field.choices == expected

    def test_base_type(self):
        assert self.field.base_type == self.base_type

    def test_internal_type(self):
        expected = self.base_model_field().get_internal_type()
        assert self.field.get_internal_type() == expected

    def test_to_python_value_when_value_is_none(self):
        assert self.field.to_python(None) is None

    def test_to_python_value_when_value_is_actual_constant(self):
        constant = choice(list(self.constants))
        assert self.field.to_python(constant) is constant

    def test_to_python_value_when_value_is_constant_value(self):
        constant = choice(list(self.constants))
        assert self.field.to_python(constant.value) is constant

    def test_to_python_value_when_value_is_invalid(self):
        constant = choice(list(self.constants))
        value = constant.label + "foo"
        msg = f"Invalid input: '{value}' is not a valid constant."
        with self.assertRaises(ValidationError, msg=msg):
            self.field.to_python(value)

    def test_get_prep_value_when_value_is_none(self):
        assert self.field.get_prep_value(None) is None

    def test_get_prep_value_when_value_is_actual_constant(self):
        constant = choice(list(self.constants))
        assert self.field.get_prep_value(constant) == constant.value

    def test_get_prep_value_when_value_is_constant_value(self):
        constant = choice(list(self.constants))
        assert self.field.get_prep_value(constant.value) == constant.value

    def test_deconstruct_does_not_include_choices(self):
        name, path, args, kwargs = self.field.deconstruct()
        assert "choices" not in kwargs

    def test_deconstruct_includes_choices_if_not_default(self):
        choices = self.field.choices[:-1]
        self.field.choices = choices
        name, path, args, kwargs = self.field.deconstruct()
        assert kwargs["choices"] == list(choices)

    def test_get_foo_display_works_with_value(self):
        constant = choice(list(self.constants))
        instance = self.TestModel(foo=constant.value)
        assert instance.get_foo_display() == constant.label

    def test_get_foo_display_works_with_actual_constant(self):
        constant = choice(list(self.constants))
        instance = self.TestModel(foo=constant)
        assert instance.get_foo_display() == constant.label

    def test_attributes(self):
        constant = choice(list(self.constants))
        instance = self.TestModel(foo=constant.value)
        assert isinstance(instance.foo, self.field_cls.attr_class)
        assert isinstance(self.TestModel.foo, self.field_cls.descriptor_class)

    def test_blank_and_nullable_values(self):
        instance = self.TestModel(foo="")
        assert instance.foo == ""
        instance = self.TestModel(foo=None)
        assert instance.foo is None


class TestAdjustmentField(ConstantFieldTestBase, TestCase):
    field_cls = AdjustmentField
    constants = ADJUSTMENTS
    base_type = str
    base_model_field = models.CharField


class TestBusinessDayConventionField(ConstantFieldTestBase, TestCase):
    field_cls = BusinessDayConventionField
    constants = BUSINESS_DAY_CONVENTIONS
    base_type = str
    base_model_field = models.CharField


class TestCurrencyField(ConstantFieldTestBase, TestCase):
    field_cls = CurrencyField
    constants = CURRENCIES
    base_type = str
    base_model_field = models.CharField


class TestDayCountField(ConstantFieldTestBase, TestCase):
    field_cls = DayCountField
    constants = DAY_COUNTS
    base_type = str
    base_model_field = models.CharField


class TestFundingBasisField(ConstantFieldTestBase, TestCase):
    field_cls = FundingBasisField
    constants = FUNDING_BASES
    base_type = str
    base_model_field = models.CharField


class TestPaymentFrequencyField(ConstantFieldTestBase, TestCase):
    field_cls = PaymentFrequencyField
    constants = PAYMENT_FREQUENCIES
    base_type = int
    base_model_field = models.IntegerField


class TestTenorField(ConstantFieldTestBase, TestCase):
    field_cls = TenorField
    constants = TENORS
    base_type = timedelta
    base_model_field = models.DurationField
