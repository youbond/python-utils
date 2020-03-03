from datetime import time
from functools import lru_cache
from typing import List, Tuple

from origin_common.constants.adjustments import ADJUSTMENTS, Adjustment
from origin_common.constants.base import Constant, Constants, add_sorting_functions
from origin_common.constants.business_day_conventions import (
    BUSINESS_DAY_CONVENTIONS,
    BusinessDayConvention,
)
from origin_common.constants.calendars import CALENDARS, Calendar
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


class FixingInfo(Constant[str]):
    def __init__(
        self,
        benchmark_base: str,
        days_prior_to_fixing: int,
        fixing_time: time,
        fixing_location: str,
        calendar: Calendar,
    ):
        super().__init__(benchmark_base, benchmark_base)
        self.benchmark_base = benchmark_base
        self.days_prior_to_fixing = days_prior_to_fixing
        self.fixing_time = fixing_time
        self.fixing_location = fixing_location
        self.calendar = calendar
        self.make_immutable()


EURIBOR = FixingInfo(
    benchmark_base="EURIBOR",
    days_prior_to_fixing=2,
    fixing_time=time(hour=11),
    fixing_location="Brussels",
    calendar=CALENDARS.TARGET2,
)

LIBOR_TWO_DAYS = FixingInfo(
    benchmark_base="LIBOR",
    days_prior_to_fixing=2,
    fixing_time=time(hour=11),
    fixing_location="London",
    calendar=CALENDARS.LONDON,
)

LIBOR_ZERO_DAYS = FixingInfo(
    benchmark_base="LIBOR",
    days_prior_to_fixing=0,
    fixing_time=time(hour=11),
    fixing_location="London",
    calendar=CALENDARS.LONDON,
)

SONIA = FixingInfo(
    benchmark_base="SONIA",
    days_prior_to_fixing=5,
    fixing_time=time(hour=9),
    fixing_location="London",
    calendar=CALENDARS.LONDON,
)
BBSW = FixingInfo(
    benchmark_base="BBSW",
    days_prior_to_fixing=0,
    fixing_time=time(hour=10),
    fixing_location="Sydney",
    calendar=CALENDARS.SYDNEY,
)
STIBOR = FixingInfo(
    benchmark_base="STIBOR",
    days_prior_to_fixing=2,
    fixing_time=time(hour=11),
    fixing_location="(CET)",
    calendar=CALENDARS.STOCKHOLM,
)
NIBOR = FixingInfo(
    benchmark_base="NIBOR",
    days_prior_to_fixing=2,
    fixing_time=time(hour=11),
    fixing_location="(CET)",
    calendar=CALENDARS.OSLO,
)
CAD_BA_CDOR = FixingInfo(
    benchmark_base="CAD-BA-CDOR",
    days_prior_to_fixing=0,
    fixing_time=time(hour=10),
    fixing_location="Toronto",
    calendar=CALENDARS.TORONTO,
)
BANK_BILL_RATE = FixingInfo(
    benchmark_base="Bank Bill Rate",
    days_prior_to_fixing=0,
    fixing_time=time(hour=11),
    fixing_location="Auckland",
    calendar=CALENDARS.AUCKLAND,
)
PRIBOR = FixingInfo(
    benchmark_base="PRIBOR",
    days_prior_to_fixing=2,
    fixing_time=time(hour=11),
    fixing_location="Prague",
    calendar=CALENDARS.PRAGUE,
)
HIBOR = FixingInfo(
    benchmark_base="HIBOR",
    days_prior_to_fixing=0,
    fixing_time=time(hour=11),
    fixing_location="Hong Kong",
    calendar=CALENDARS.HONG_KONG,
)
SIBOR = FixingInfo(
    benchmark_base="SIBOR",
    days_prior_to_fixing=0,
    fixing_time=time(hour=11),
    fixing_location="Singapore",
    calendar=CALENDARS.SINGAPORE,
)
JIBAR = FixingInfo(
    benchmark_base="JIBAR",
    days_prior_to_fixing=0,
    fixing_time=time(hour=12),
    fixing_location="Johannesburg",
    calendar=CALENDARS.JOHANNESBURG,
)


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
        calendars_for_payment: List[Calendar] = None,
    ):
        super().__init__(value, label)
        self.currency = currency
        self.payment_frequency = payment_frequency
        self.day_count = day_count
        self.sorting = sorting
        self.adjustment = adjustment
        self.business_day_convention = business_day_convention
        self.pricing = pricing
        self.calendars_for_payment = calendars_for_payment or []
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
    def __init__(
        self,
        *args,
        index: int,
        screen_page: str,
        legal_label: str,
        fixing_info: FixingInfo = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.basis_type = BASIS_TYPE_FLOATING
        self.index = index
        self.screen_page = screen_page
        self.is_callable_basis = True
        self.legal_label = legal_label
        self.fixing_info = fixing_info

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
        calendars_for_payment: List[Calendar] = None,
    ):
        value = f"FIXED_{currency.value}"
        label = f"{currency.value} Fixed"
        if not legal_label:
            legal_label = f"Fixed Rate {currency.value}"
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
            calendars_for_payment,
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
        calendars_for_payment: List[Calendar] = None,
    ):
        value = f"MS_{currency.value}"
        label = f"{currency.value} M/S"
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
            calendars_for_payment,
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
        calendars_for_payment=[CALENDARS.TARGET2],
        fixing_info=EURIBOR,
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
        calendars_for_payment=[CALENDARS.TARGET2],
        fixing_info=EURIBOR,
    )
    EUR_FIXED = FixedFundingBasis(
        currency=CURRENCIES.EUR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        sorting=20,
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.NEW_YORK],
        fixing_info=LIBOR_TWO_DAYS,
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.NEW_YORK],
        fixing_info=LIBOR_TWO_DAYS,
    )
    USD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.USD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        sorting=60,
        calendars_for_payment=[CALENDARS.NEW_YORK],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.NEW_YORK],
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
        calendars_for_payment=[CALENDARS.LONDON],
        fixing_info=SONIA,
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
        calendars_for_payment=[CALENDARS.LONDON],
        fixing_info=LIBOR_ZERO_DAYS,
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
        calendars_for_payment=[CALENDARS.LONDON],
        fixing_info=LIBOR_ZERO_DAYS,
    )
    GBP_FIXED = FixedFundingBasis(
        currency=CURRENCIES.GBP,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=100,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        calendars_for_payment=[CALENDARS.LONDON],
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
        calendars_for_payment=[CALENDARS.LONDON],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.TOKYO],
        fixing_info=LIBOR_TWO_DAYS,
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.TOKYO],
        fixing_info=LIBOR_TWO_DAYS,
    )
    JPY_FIXED = FixedFundingBasis(
        currency=CURRENCIES.JPY,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=140,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        calendars_for_payment=[CALENDARS.TOKYO],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.TOKYO],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.ZURICH],
        fixing_info=LIBOR_TWO_DAYS,
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.ZURICH],
        fixing_info=LIBOR_TWO_DAYS,
    )
    CHF_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CHF,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=180,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        calendars_for_payment=[CALENDARS.ZURICH],
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
        calendars_for_payment=[CALENDARS.LONDON, CALENDARS.ZURICH],
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
        calendars_for_payment=[CALENDARS.SYDNEY],
        fixing_info=BBSW,
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
        calendars_for_payment=[CALENDARS.SYDNEY],
        fixing_info=BBSW,
    )
    AUD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.AUD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=220,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        calendars_for_payment=[CALENDARS.SYDNEY],
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
        calendars_for_payment=[CALENDARS.SYDNEY],
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
        calendars_for_payment=[CALENDARS.STOCKHOLM],
        fixing_info=STIBOR,
    )
    SEK_FIXED = FixedFundingBasis(
        currency=CURRENCIES.SEK,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        sorting=250,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="SEK Fixed Rate",
        calendars_for_payment=[CALENDARS.STOCKHOLM],
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
        calendars_for_payment=[CALENDARS.STOCKHOLM],
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
        screen_page="ORIBOR",
        calendars_for_payment=[CALENDARS.OSLO],
        fixing_info=NIBOR,
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
        screen_page="ORIBOR",
        calendars_for_payment=[CALENDARS.OSLO],
        fixing_info=NIBOR,
    )
    NOK_FIXED = FixedFundingBasis(
        currency=CURRENCIES.NOK,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=290,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        legal_label="NOK Fixed Rate",
        calendars_for_payment=[CALENDARS.OSLO],
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
        calendars_for_payment=[CALENDARS.OSLO],
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
        calendars_for_payment=[CALENDARS.TORONTO],
        fixing_info=CAD_BA_CDOR,
    )
    CAD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.CAD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=320,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="CAD Fixed Rate",
        calendars_for_payment=[CALENDARS.TORONTO],
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
        calendars_for_payment=[CALENDARS.TORONTO],
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
        calendars_for_payment=[CALENDARS.AUCKLAND],
        fixing_info=BANK_BILL_RATE,
    )
    NZD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.NZD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=350,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        calendars_for_payment=[CALENDARS.AUCKLAND],
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
        calendars_for_payment=[CALENDARS.AUCKLAND],
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
        calendars_for_payment=[CALENDARS.HONG_KONG],
        fixing_info=HIBOR,
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
        calendars_for_payment=[CALENDARS.HONG_KONG],
        fixing_info=HIBOR,
    )
    HKD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.HKD,
        payment_frequency=PAYMENT_FREQUENCIES.QUARTERLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=370,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        calendars_for_payment=[CALENDARS.HONG_KONG],
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
        calendars_for_payment=[CALENDARS.SINGAPORE],
        fixing_info=SIBOR,
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
        calendars_for_payment=[CALENDARS.SINGAPORE],
        fixing_info=SIBOR,
    )
    SGD_FIXED = FixedFundingBasis(
        currency=CURRENCIES.SGD,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=375,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        calendars_for_payment=[CALENDARS.SINGAPORE],
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
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=383,
        label="3mPRIBOR",
        pricing=False,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="3 month PRIBOR",
        screen_page="PRIBOR",
        fixing_info=PRIBOR,
    )
    CZK_3M.is_callable_basis = False  # weird exception
    CZK_6M = FloatingFundingBasis(
        value="6M_CZK",
        currency=CURRENCIES.CZK,
        index=6,
        payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_360,
        sorting=384,
        label="6mPRIBOR",
        pricing=False,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        legal_label="6 month PRIBOR",
        screen_page="PRIBOR",
        fixing_info=PRIBOR,
    )
    CZK_6M.is_callable_basis = False  # weird exception
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
        calendars_for_payment=[CALENDARS.JOHANNESBURG],
        fixing_info=JIBAR,
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
        calendars_for_payment=[CALENDARS.JOHANNESBURG],
        fixing_info=JIBAR,
    )
    ZAR_FIXED = FixedFundingBasis(
        currency=CURRENCIES.ZAR,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_365,
        sorting=387,
        pricing=False,
        calendars_for_payment=[CALENDARS.JOHANNESBURG],
    )
    RON_FIXED = FixedFundingBasis(
        currency=CURRENCIES.RON,
        payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
        day_count=DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        sorting=388,
        pricing=False,
        adjustment=ADJUSTMENTS.UNADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        calendars_for_payment=[CALENDARS.BUCHAREST],
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
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.TARGET2],
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
        calendars_for_payment=[CALENDARS.TARGET2],
    )

    @lru_cache()
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
            calendars_for_payment=[CALENDARS.NEW_YORK],
        )
        self.EUR_FIXED = FixedFundingBasis(
            currency=CURRENCIES.EUR,
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_360,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            sorting=20,
            calendars_for_payment=[CALENDARS.TARGET2],
        )
        self.GBP_FIXED = FixedFundingBasis(
            currency=CURRENCIES.GBP,
            payment_frequency=PAYMENT_FREQUENCIES.ANNUALLY,
            day_count=DAY_COUNTS.ACTUAL_365,
            sorting=100,
            adjustment=ADJUSTMENTS.ADJUSTED,
            business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            calendars_for_payment=[CALENDARS.LONDON],
        )


MTN_FUNDING_BASES = MTNFundingBases()
MTN_FUNDING_BASES.make_immutable()
CD_FUNDING_BASES = CDFundingBases()
CD_FUNDING_BASES.make_immutable()
FUNDING_BASES = MTN_FUNDING_BASES
add_sorting_functions(FundingBasis, FUNDING_BASES)
