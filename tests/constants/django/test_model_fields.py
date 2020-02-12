from datetime import timedelta
from random import choice

from django.core.exceptions import ValidationError
from django.db import models
from django.test import TestCase

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
# connection = psycopg2.connect("user=resley password='catsrgr8' dbname=postgres")
# cursor = connection.cursor()
# cursor.execute("CREATE DATABASE testdb;")
# atexit.register(lambda: cursor.execute("DROP DATABASE testdb;"))
# needed to create models
# settings.configure(DATABASES={
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "testdb",
#         # "USER": "gitlab",
#         # "PASSWORD": "gitlabpwd",
#         # "HOST": "postgres",
#     },
# },MIGRATION_MODULES = {
#         # This lets us skip creating migrations for the test models as many of
#         # them depend on one of the following contrib applications.
#         'auth': None,
#         'contenttypes': None,
#         'sessions': None,
#     })
# django.setup()
from tests.models import TestModel


class ConstantFieldTestBase:
    field_cls: type(ConstantField) = None
    constants: Constants = None
    base_type: type = None
    base_model_field: type(models.Field) = None

    # @classmethod
    # @isolate_apps("test")
    # def setUpClass(cls) -> None:
    #     super().setUpClass()
    #     assert cls.field_cls is not None, "Set field class"
    #
    #     class TestModel(models.Model):
    #         foo = cls.field_cls()
    #         array = ArrayField(cls.field_cls(), default=list)
    #
    #         class Meta:
    #             app_label = "test"
    #
    #     cls.TestModel = TestModel

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

    def get_model_field_name(self):
        return self.field_cls.__name__.replace("Field", "").lower()

    def test_get_foo_display_works_with_value(self):
        constant = choice(list(self.constants))
        field_name = self.get_model_field_name()
        instance = TestModel(**{field_name: constant.value})
        display_func = getattr(instance, f"get_{field_name}_display")
        assert display_func() == constant.label

    def test_get_foo_display_works_with_actual_constant(self):
        constant = choice(list(self.constants))
        field_name = self.get_model_field_name()
        instance = TestModel(**{field_name: constant})
        display_func = getattr(instance, f"get_{field_name}_display")
        assert display_func() == constant.label

    def test_attributes(self):
        constant = choice(list(self.constants))
        field_name = self.get_model_field_name()
        instance = TestModel(**{field_name: constant.value})
        assert isinstance(getattr(instance, field_name), self.field_cls.attr_class)
        assert isinstance(
            getattr(TestModel, field_name), self.field_cls.descriptor_class
        )

    def test_blank_and_nullable_values(self):
        field_name = self.get_model_field_name()
        instance = TestModel(**{field_name: ""})
        assert getattr(instance, field_name) == ""
        instance = TestModel(**{field_name: None})
        assert getattr(instance, field_name) is None

    def test_can_use_constant_in_lookups(self):
        constant = choice(list(self.constants))
        manager = TestModel.objects
        field_name = self.get_model_field_name()
        TestModel(**{field_name: constant, f"{field_name}_array": [constant]}).save()
        assert manager.filter(**{field_name: constant}).exists()
        assert manager.filter(
            **{f"{field_name}_array__overlap": [constant]}
        ).exists()


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
