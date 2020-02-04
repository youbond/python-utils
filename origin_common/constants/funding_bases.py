from typing import Tuple

from origin_common.constants.adjustments import ADJUSTMENTS, Adjustment
from origin_common.constants.base import Constant, Constants
from origin_common.constants.business_day_conventions import (
    BUSINESS_DAY_CONVENTIONS,
    BusinessDayConvention,
)
from origin_common.constants.currencies import CURRENCIES, Currency
from origin_common.constants.day_counts import DAY_COUNTS, DayCount
from origin_common.constants.payment_frequencies import (
    PAYMENT_FREQUENCIES,
    PaymentFrequency,
)

BASIS_TYPE_GOVIE = "govie"

BASIS_TYPE_MS = "ms"

BASIS_TYPE_FIXED = "fixed"

BASIS_TYPE_FLOATING = "floating"


class FundingBasis(Constant[str]):
    def __init__(
        self,
        value: str,
        label: str,
        currency: Currency,
        payment_frequency: PaymentFrequency,
        day_count: DayCount,
        sorting: int,
        adjustment: Adjustment = None,
        business_day_convention: BusinessDayConvention = None,
        pricing: bool = True,
    ):
        super().__init__(value, label)
        self.currency = currency
        self.payment_frequency = payment_frequency
        self.day_count = day_count
        self.sorting = sorting
        self.adjustment = adjustment
        self.business_day_convention = business_day_convention
        self.pricing = pricing
        self.is_callable_basis = False
        self.index = 0
        self.basis_type = None  # overridden in child classes

    @property
    def is_fixed_basis(self):
        return False

    @property
    def is_floating_basis(self):
        return False

    @property
    def is_ms_basis(self):
        return False

    @property
    def is_govie_basis(self):
        return False

    @property
    def symbol(self):
        return self.currency.symbol


class FloatingFundingBasis(FundingBasis):
    def __init__(self, *args, index: int, screen_page: str, legal_label: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = BASIS_TYPE_FLOATING
        self.index = index
        self.screen_page = screen_page
        self.is_callable_basis = True
        self.legal_label = legal_label

    @property
    def is_floating_basis(self):
        return True


class FixedFundingBasis(FundingBasis):
    def __init__(
        self,
        currency: Currency,
        payment_frequency: PaymentFrequency,
        day_count: DayCount,
        sorting: int,
        adjustment: Adjustment = None,
        business_day_convention: BusinessDayConvention = None,
        pricing: bool = True,
        legal_label: str = None,
    ):
        value = "FIXED_{}".format(currency.value)
        label = "{} Fixed".format(currency.value)
        if not legal_label:
            legal_label = "Fixed Rate {}".format(currency.value)
        super().__init__(
            value,
            label,
            currency,
            payment_frequency,
            day_count,
            sorting,
            adjustment,
            business_day_convention,
            pricing,
        )
        self.basis_type = BASIS_TYPE_FIXED
        self.legal_label = legal_label

    @property
    def is_fixed_basis(self):
        return True


class MSFundingBasis(FundingBasis):
    def __init__(
        self,
        currency: Currency,
        payment_frequency: PaymentFrequency,
        day_count: DayCount,
        sorting: int,
        floating_basis: FloatingFundingBasis,
        ms_payment_frequency: PaymentFrequency,
        display_payment_frequency: PaymentFrequency,
        ms_day_count: DayCount,
        adjustment: Adjustment = None,
        business_day_convention: BusinessDayConvention = None,
        pricing: bool = True,
    ):
        value = "MS_{}".format(currency.value)
        label = "{} M/S".format(currency.value)
        super().__init__(
            value,
            label,
            currency,
            payment_frequency,
            day_count,
            sorting,
            adjustment,
            business_day_convention,
            pricing,
        )
        self.basis_type = BASIS_TYPE_MS
        self.floating_basis = floating_basis
        self.display_payment_frequency = display_payment_frequency
        self.ms_payment_frequency = ms_payment_frequency
        self.ms_day_count = ms_day_count

    @property
    def is_ms_basis(self):
        return True


class GovieFundingBasis(FundingBasis):
    def __init__(self, *args, issuer_short_name: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = BASIS_TYPE_GOVIE
        self.issuer_short_name = issuer_short_name

    @property
    def is_govie_basis(self):
        return True


class FundingBases(Constants[FundingBasis]):
    EUR_3M = FloatingFundingBasis(
        value="3M_EUR",
        label="3mEURIBOR",
        currency=CURRENCIES.EUR,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month EURIBOR",
        screen_page="EURIBOR01",
        sorting=0,
    )
    EUR_6M = FloatingFundingBasis(
        value="6M_EUR",
        label="6mEURIBOR",
        currency=CURRENCIES.EUR,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month EURIBOR",
        screen_page="EURIBOR01",
        sorting=10,
    )
    EUR_FIXED = FixedFundingBasis(
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        sorting=20,
    )
    EUR_MS = MSFundingBasis(
        currency=CURRENCIES.EUR,
        floating_basis=EUR_6M,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=30,
    )

    USD_3M = FloatingFundingBasis(
        value="3M_USD",
        label="3mUSD-LIBOR",
        currency=CURRENCIES.USD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month USD LIBOR",
        screen_page="LIBOR01",
        sorting=40,
    )
    USD_6M = FloatingFundingBasis(
        value="6M_USD",
        label="6mUSD-LIBOR",
        currency=CURRENCIES.USD,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month USD LIBOR",
        screen_page="LIBOR01",
        sorting=50,
    )
    USD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.USD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        sorting=60,
    )
    USD_MS = MSFundingBasis(
        currency=CURRENCIES.USD,
        floating_basis=USD_3M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=70,
    )

    GBP_SONIA = FloatingFundingBasis(
        value="SONIA",
        currency=CURRENCIES.GBP,
        index=0,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=75,
        label="SONIA",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        pricing=False,
        legal_label="Compounded Daily SONIA",
        screen_page="SONIA",
    )
    GBP_3M = FloatingFundingBasis(
        value="3M_GBP",
        currency=CURRENCIES.GBP,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=80,
        label="3mGBP-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month GBP LIBOR",
        screen_page="LIBOR01",
    )
    GBP_6M = FloatingFundingBasis(
        value="6M_GBP",
        currency=CURRENCIES.GBP,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=90,
        label="6mGBP-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month GBP LIBOR",
        screen_page="LIBOR01",
    )
    GBP_FIXED = FixedFundingBasis(
        currency=CURRENCIES.GBP,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=100,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
    )
    GBP_MS = MSFundingBasis(
        currency=CURRENCIES.GBP,
        floating_basis=GBP_6M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        ms_day_count=DAY_COUNTS.ACTUAL_365,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=110,
    )
    JPY_3M = FloatingFundingBasis(
        value="3M_JPY",
        currency=CURRENCIES.JPY,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=120,
        label="3mJPY-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month JPY LIBOR",
        screen_page="LIBOR01",
    )
    JPY_6M = FloatingFundingBasis(
        value="6M_JPY",
        currency=CURRENCIES.JPY,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=130,
        label="6mJPY-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month JPY LIBOR",
        screen_page="LIBOR01",
    )
    JPY_FIXED = FixedFundingBasis(
        currency=CURRENCIES.JPY,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=140,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    JPY_MS = MSFundingBasis(
        currency=CURRENCIES.JPY,
        floating_basis=JPY_6M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365_NL,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        sorting=150,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    CHF_3M = FloatingFundingBasis(
        value="3M_CHF",
        currency=CURRENCIES.CHF,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=160,
        label="3mCHF-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month CHF LIBOR",
        screen_page="LIBOR01",
    )
    CHF_6M = FloatingFundingBasis(
        value="6M_CHF",
        currency=CURRENCIES.CHF,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=170,
        label="6mCHF-LIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month CHF LIBOR",
        screen_page="LIBOR01",
    )
    CHF_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CHF,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=180,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
    )
    CHF_MS = MSFundingBasis(
        currency=CURRENCIES.CHF,
        floating_basis=CHF_6M,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        sorting=190,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    AUD_3M = FloatingFundingBasis(
        value="3M_AUD",
        currency=CURRENCIES.AUD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=200,
        label="3mBBSW",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month BBSW",
        screen_page="BBSW",
    )
    AUD_6M = FloatingFundingBasis(
        value="6M_AUD",
        currency=CURRENCIES.AUD,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=210,
        label="6mBBSW",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month BBSW",
        screen_page="BBSW",
    )
    AUD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.AUD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=220,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    AUD_MS = MSFundingBasis(
        currency=CURRENCIES.AUD,
        floating_basis=AUD_3M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        ms_day_count=DAY_COUNTS.ACTUAL_365,
        sorting=230,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    SEK_3M = FloatingFundingBasis(
        value="3M_SEK",
        currency=CURRENCIES.SEK,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=240,
        label="3mSTIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month STIBOR",
        screen_page="SIDE",
    )
    SEK_FIXED = FixedFundingBasis(
        currency=CURRENCIES.SEK,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=250,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="SEK Fixed Rate",
    )
    SEK_MS = MSFundingBasis(
        currency=CURRENCIES.SEK,
        floating_basis=SEK_3M,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        sorting=260,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    NOK_3M = FloatingFundingBasis(
        value="3M_NOK",
        currency=CURRENCIES.NOK,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=270,
        label="3mNIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month NIBOR",
        screen_page="NIBRO",
    )
    NOK_6M = FloatingFundingBasis(
        value="6M_NOK",
        currency=CURRENCIES.NOK,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=280,
        label="6mNIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month NIBOR",
        screen_page="NIBRO",
    )
    NOK_FIXED = FixedFundingBasis(
        currency=CURRENCIES.NOK,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=290,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="NOK Fixed Rate",
    )
    NOK_MS = MSFundingBasis(
        currency=CURRENCIES.NOK,
        floating_basis=NOK_6M,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        ms_day_count=DAY_COUNTS.ACTUAL_360,
        sorting=300,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    CAD_3M = FloatingFundingBasis(
        value="3M_CAD",
        currency=CURRENCIES.CAD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=310,
        label="3mCAD-BA-CDOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month BA-CDOR",
        screen_page="CDOR",
    )
    CAD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CAD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=320,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="CAD Fixed Rate",
    )
    CAD_MS = MSFundingBasis(
        currency=CURRENCIES.CAD,
        floating_basis=CAD_3M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        ms_day_count=DAY_COUNTS.ACTUAL_365,
        sorting=330,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    NZD_3M = FloatingFundingBasis(
        value="3M_NZD",
        currency=CURRENCIES.NZD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=340,
        label="3mNZD-BB",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month NZD-BB",
        screen_page="",
    )
    NZD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.NZD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=350,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    NZD_MS = MSFundingBasis(
        currency=CURRENCIES.NZD,
        floating_basis=NZD_3M,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        ms_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        ms_day_count=DAY_COUNTS.ACTUAL_365,
        sorting=360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    HKD_3M = FloatingFundingBasis(
        value="3M_HKD",
        currency=CURRENCIES.HKD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=368,
        label="3mHIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month HIBOR",
        screen_page="HKABHIBOR",
    )
    HKD_6M = FloatingFundingBasis(
        value="6M_HKD",
        currency=CURRENCIES.HKD,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=369,
        label="6mHIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month HIBOR",
        screen_page="HKABHIBOR",
    )
    HKD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.HKD,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=370,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    SGD_3M = FloatingFundingBasis(
        value="3M_SGD",
        currency=CURRENCIES.SGD,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=373,
        label="3mSIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month SIBOR",
        screen_page="ABSIRFIX01",
    )
    SGD_6M = FloatingFundingBasis(
        value="6M_SGD",
        currency=CURRENCIES.SGD,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=374,
        label="6mSIBOR",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month SIBOR",
        screen_page="ABSIRFIX01",
    )
    SGD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.SGD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=375,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    CNH_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CNH,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=380,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    CNY_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CNY,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=381,
        pricing=False,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
    )
    KRW_FIXED = FixedFundingBasis(
        currency=CURRENCIES.KRW,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=382,
        pricing=False,
    )
    CZK_3M = FloatingFundingBasis(
        value="3M_CZK",
        currency=CURRENCIES.CZK,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=383,
        label="3mPRIBOR",
        pricing=False,
        legal_label="3 month CZK-PRIBOR-PRBO",
        screen_page="PRBO",
    )
    CZK_3M.is_callable_basis = False  # weird exception
    CZK_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CZK,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=384,
        pricing=False,
    )
    ZAR_3M = FloatingFundingBasis(
        value="3M_ZAR",
        currency=CURRENCIES.ZAR,
        index=3,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=385,
        label="3mJIBAR",
        pricing=False,
        legal_label="3 month JIBAR",
        screen_page="SAFEY",
    )
    ZAR_6M = FloatingFundingBasis(
        value="6M_ZAR",
        currency=CURRENCIES.ZAR,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=386,
        label="6mJIBAR",
        pricing=False,
        legal_label="6 month JIBAR",
        screen_page="SAFEY",
    )
    ZAR_FIXED = FixedFundingBasis(
        currency=CURRENCIES.ZAR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=387,
        pricing=False,
    )
    RON_FIXED = FixedFundingBasis(
        currency=CURRENCIES.RON,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=388,
        pricing=False,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
    )
    BTP = GovieFundingBasis(
        value="BTP",
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=390,
        label="BTP",
        issuer_short_name="Rep Italy",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # max_tenor=TENOR_45Y_VAL,
        # min_tenor=TENOR_1Y_VAL,
    )
    OAT = GovieFundingBasis(
        value="OAT",
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=400,
        label="OAT",
        issuer_short_name="French Rep",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # max_tenor=TENOR_45Y_VAL,
        # min_tenor=TENOR_1Y_VAL,
    )
    OLO = GovieFundingBasis(
        value="OLO",
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=410,
        label="OLO",
        issuer_short_name="Kdom Belgium",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # max_tenor=TENOR_45Y_VAL,
        # min_tenor=TENOR_1Y_VAL,
    )
    RAGB = GovieFundingBasis(
        value="RAGB",
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=420,
        label="RAGB",
        issuer_short_name="Rep Austria",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # max_tenor=TENOR_25Y_VAL,
        # min_tenor=TENOR_1Y_VAL,
    )
    SPGB = GovieFundingBasis(
        value="SPGB",
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=430,
        label="SPGB",
        issuer_short_name="Kdom Spain",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # max_tenor=TENOR_45Y_VAL,
        # min_tenor=TENOR_1Y_VAL,
    )

    def to_django_choices(
        self, is_callable_basis=None, pricing=None
    ) -> Tuple[Tuple[str, str]]:
        properties_to_check = {}
        if is_callable_basis is not None:
            properties_to_check["is_callable_basis"] = is_callable_basis
        if pricing is not None:
            properties_to_check["pricing"] = pricing
        return tuple(
            (basis.value, basis.label)
            for basis in self
            if all(
                getattr(basis, attr) == value
                for attr, value in properties_to_check.items()
            )
        )


class MTNFundingBases(FundingBases):
    pass


class CDFundingBases(FundingBases):
    def __init__(self):
        super().__init__()
        self.USD_FIXED = FixedFundingBasis(
            currency=CURRENCIES.USD,
            payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_360,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            sorting=60,
        )
        self.EUR_FIXED = FixedFundingBasis(
            currency=CURRENCIES.EUR,
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_360,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            sorting=20,
        )
        self.GBP_FIXED = FixedFundingBasis(
            currency=CURRENCIES.GBP,
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_365_NL,
            sorting=100,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        )


MTN_FUNDING_BASES = MTNFundingBases()
MTN_FUNDING_BASES.make_immutable()
CD_FUNDING_BASES = CDFundingBases()
CD_FUNDING_BASES.make_immutable()
FUNDING_BASES = MTN_FUNDING_BASES
