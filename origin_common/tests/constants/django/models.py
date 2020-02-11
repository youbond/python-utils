from django.contrib.postgres.fields import ArrayField
from django.db import models

from origin_common.constants.django.model_fields import (
    AdjustmentField,
    BusinessDayConventionField,
    CurrencyField,
    DayCountField,
    FundingBasisField,
    PaymentFrequencyField,
    TenorField,
)


class TestModel(models.Model):
    adjustment = AdjustmentField(null=True, blank=True)
    adjustment_array = ArrayField(AdjustmentField(), default=list)
    businessdayconvention = BusinessDayConventionField(null=True, blank=True)
    businessdayconvention_array = ArrayField(BusinessDayConventionField(), default=list)
    currency = CurrencyField(null=True, blank=True)
    currency_array = ArrayField(CurrencyField(), default=list)
    daycount = DayCountField(null=True, blank=True)
    daycount_array = ArrayField(DayCountField(), default=list)
    fundingbasis = FundingBasisField(null=True, blank=True)
    fundingbasis_array = ArrayField(FundingBasisField(), default=list)
    paymentfrequency = PaymentFrequencyField(null=True, blank=True)
    paymentfrequency_array = ArrayField(PaymentFrequencyField(), default=list)
    tenor = TenorField(null=True, blank=True)
    tenor_array = ArrayField(TenorField(), default=list)

    class Meta:
        app_label = "test"
