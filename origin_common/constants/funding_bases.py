from typing import Tuple

from origin_common.constants.adjustments import ADJUSTMENTS, Adjustment
from origin_common.constants.base import Constant, Constants
from origin_common.constants.business_day_conventions import (
    BUSINESS_DAY_CONVENTIONS,
    BusinessDayConvention,
)
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
        currency: str,
        symbol: str,
        payment_frequency: PaymentFrequency,
        day_count: DayCount,
        sorting: int,
        adjustment: Adjustment = None,
        business_day_convention: BusinessDayConvention = None,
        pricing: bool = True,
    ):
        super().__init__(value, label)
        self.currency = currency
        self.symbol = symbol
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

    def get_swap_config(self):
        # should this live here or in bankangle?
        return {
            "value": self.value,
            "label": self.label,
            "symbol": self.symbol,
            "payment_freq": self.payment_frequency.value,
            "day_count": self.day_count.value,
            "payment_freq_selectable": not self.is_floating_basis,
            "daycount_selectable": True,
        }


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
    def __init__(self, *args, legal_label: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = BASIS_TYPE_FIXED
        self.legal_label = legal_label

    @property
    def is_fixed_basis(self):
        return True


class MSFundingBasis(FundingBasis):
    def __init__(
        self,
        *args,
        floating_basis: FloatingFundingBasis,
        display_payment_frequency: PaymentFrequency,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.basis_type = BASIS_TYPE_MS
        self.floating_basis = floating_basis
        self.display_payment_frequency = display_payment_frequency

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
        currency="EUR",
        symbol="€",
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
        currency="EUR",
        symbol="€",
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
        value="FIXED_EUR",
        label="EUR Fixed",
        currency="EUR",
        symbol="€",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="Fixed Rate EUR",
        sorting=20,
    )
    EUR_MS = MSFundingBasis(
        value="MS_EUR",
        label="EUR M/S",
        currency="EUR",
        symbol="€",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        floating_basis=EUR_6M,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=30,
    )

    USD_3M = FloatingFundingBasis(
        value="3M_USD",
        label="3mUSD-LIBOR",
        currency="USD",
        symbol="$",
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
        currency="USD",
        symbol="$",
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
        value="FIXED_USD",
        label="USD Fixed",
        currency="USD",
        symbol="$",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="Fixed Rate USD",
        sorting=60,
    )
    USD_MS = MSFundingBasis(
        value="MS_USD",
        label="USD M/S",
        currency="USD",
        symbol="$",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=USD_3M,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=70,
    )

    GBP_SONIA = FloatingFundingBasis(
        value="SONIA",
        currency="GBP",
        symbol="£",
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
        currency="GBP",
        symbol="£",
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
        currency="GBP",
        symbol="£",
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
        value="FIXED_GBP",
        currency="GBP",
        symbol="£",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=100,
        label="GBP Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="Fixed Rate GBP",
    )
    GBP_MS = MSFundingBasis(
        value="MS_GBP",
        currency="GBP",
        symbol="£",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=GBP_6M,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=110,
        label="GBP M/S",
    )
    JPY_3M = FloatingFundingBasis(
        value="3M_JPY",
        currency="JPY",
        symbol="¥",
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
        currency="JPY",
        symbol="¥",
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
        value="FIXED_JPY",
        currency="JPY",
        symbol="¥",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=140,
        label="JPY Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate JPY",
    )
    JPY_MS = MSFundingBasis(
        value="MS_JPY",
        currency="JPY",
        symbol="JPY",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=JPY_6M,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365_NL,
        sorting=150,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="JPY M/S",
    )
    CHF_3M = FloatingFundingBasis(
        value="3M_CHF",
        currency="CHF",
        symbol="CHF",
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
        currency="CHF",
        symbol="CHF",
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
        value="FIXED_CHF",
        currency="CHF",
        symbol="CHF",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=180,
        label="CHF Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="Fixed Rate CHF",
    )
    CHF_MS = MSFundingBasis(
        value="MS_CHF",
        currency="CHF",
        symbol="CHF",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        floating_basis=CHF_6M,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=190,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="CHF M/S",
    )
    AUD_3M = FloatingFundingBasis(
        value="3M_AUD",
        currency="AUD",
        symbol="AUD",
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
        currency="AUD",
        symbol="AUD",
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
        value="FIXED_AUD",
        currency="AUD",
        symbol="AUD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=220,
        label="AUD Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate AUD",
    )
    AUD_MS = MSFundingBasis(
        value="MS_AUD",
        currency="AUD",
        symbol="AUD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=AUD_3M,
        display_payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=230,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="AUD M/S",
    )
    SEK_3M = FloatingFundingBasis(
        value="3M_SEK",
        currency="SEK",
        symbol="SEK",
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
        value="FIXED_SEK",
        currency="SEK",
        symbol="SEK",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=250,
        label="SEK Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="SEK Fixed Rate",
    )
    SEK_MS = MSFundingBasis(
        value="MS_SEK",
        currency="SEK",
        symbol="SEK",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        floating_basis=SEK_3M,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=260,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="SEK M/S",
    )
    NOK_3M = FloatingFundingBasis(
        value="3M_NOK",
        currency="NOK",
        symbol="NOK",
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
        currency="NOK",
        symbol="NOK",
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
        value="FIXED_NOK",
        currency="NOK",
        symbol="NOK",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=290,
        label="NOK Fixed",
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="NOK Fixed Rate",
    )
    NOK_MS = MSFundingBasis(
        value="MS_NOK",
        currency="NOK",
        symbol="NOK",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        floating_basis=NOK_6M,
        display_payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=300,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="NOK M/S",
    )
    CAD_3M = FloatingFundingBasis(
        value="3M_CAD",
        currency="CAD",
        symbol="CAD",
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
        value="FIXED_CAD",
        currency="CAD",
        symbol="CAD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=320,
        label="CAD Fixed",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="CAD Fixed Rate",
    )
    CAD_MS = MSFundingBasis(
        value="MS_CAD",
        currency="CAD",
        symbol="CAD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=CAD_3M,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=330,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="CAD M/S",
    )
    NZD_3M = FloatingFundingBasis(
        value="3M_NZD",
        currency="NZD",
        symbol="NZD",
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
        value="FIXED_NZD",
        currency="NZD",
        symbol="NZD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=350,
        label="NZD Fixed",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate NZD",
    )
    NZD_MS = MSFundingBasis(
        value="MS_NZD",
        currency="NZD",
        symbol="NZD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        floating_basis=NZD_3M,
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        label="NZD M/S",
    )
    HKD_3M = FloatingFundingBasis(
        value="3M_HKD",
        currency="HKD",
        symbol="HKD",
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
        currency="HKD",
        symbol="HKD",
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
        value="FIXED_HKD",
        currency="HKD",
        symbol="HKD",
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=370,
        label="HKD Fixed",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate HKD",
    )
    SGD_3M = FloatingFundingBasis(
        value="3M_SGD",
        currency="SGD",
        symbol="SGD",
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
        currency="SGD",
        symbol="SGD",
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
        value="FIXED_SGD",
        currency="SGD",
        symbol="SGD",
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=375,
        label="SGD Fixed",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate SGD",
    )
    CNH_FIXED = FixedFundingBasis(
        value="FIXED_CNH",
        currency="CNH",
        symbol="CNH",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=380,
        label="CNH Fixed",
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate CNH",
    )
    CNY_FIXED = FixedFundingBasis(
        value="FIXED_CNY",
        currency="CNY",
        symbol="CNY",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=381,
        label="CNY Fixed",
        pricing=False,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="Fixed Rate CNY",
    )
    KRW_FIXED = FixedFundingBasis(
        value="FIXED_KRW",
        currency="KRW",
        symbol="₩",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=382,
        label="KRW Fixed",
        pricing=False,
        legal_label="Fixed Rate KRW",
    )
    CZK_3M = FloatingFundingBasis(
        value="3M_CZK",
        currency="CZK",
        symbol="CZK",
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
        value="FIXED_CZK",
        currency="CZK",
        symbol="CZK",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=384,
        label="CZK Fixed",
        pricing=False,
        legal_label="Fixed Rate CZK",
    )
    ZAR_3M = FloatingFundingBasis(
        value="3M_ZAR",
        currency="ZAR",
        symbol="ZAR",
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
        currency="ZAR",
        symbol="ZAR",
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
        value="FIXED_ZAR",
        currency="ZAR",
        symbol="ZAR",
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=387,
        label="ZAR Fixed",
        pricing=False,
        legal_label="Fixed Rate ZAR",
    )
    BTP = GovieFundingBasis(
        value="BTP",
        currency="EUR",
        symbol="€",
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
        currency="EUR",
        symbol="€",
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
        currency="EUR",
        symbol="€",
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
        currency="EUR",
        symbol="€",
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
        currency="EUR",
        symbol="€",
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
            value="FIXED_USD",
            label="USD Fixed",
            currency="USD",
            symbol="$",
            payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_360,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            legal_label="Fixed Rate USD",
            sorting=60,
        )
        self.EUR_FIXED = FixedFundingBasis(
            value="FIXED_EUR",
            label="EUR Fixed",
            currency="EUR",
            symbol="€",
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_360,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            legal_label="Fixed Rate EUR",
            sorting=20,
        )
        self.GBP_FIXED = FixedFundingBasis(
            value="FIXED_GBP",
            currency="GBP",
            symbol="£",
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_365_NL,
            sorting=100,
            label="GBP Fixed",
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            legal_label="Fixed Rate GBP",
        )


MTN_FUNDING_BASES = MTNFundingBases()
CD_FUNDING_BASES = CDFundingBases()
FUNDING_BASES = MTN_FUNDING_BASES
