from origin_common.constants import (
    PAYMENT_FREQUENCIES,
    DAY_COUNTS,
    BUSINESS_DAY_CONVENTIONS,
    ADJUSTMENTS,
)
from origin_common.constants.adjustments import Adjustment
from origin_common.constants.base import Constant, Constants
from origin_common.constants.business_day_conventions import BusinessDayConvention
from origin_common.constants.day_counts import DayCount
from origin_common.constants.payment_frequencies import PaymentFrequency


class FundingBasis(Constant):
    def __init__(
        self,
        value: str,
        label: str,
        currency: str,
        symbol: str,
        payment_frequency: PaymentFrequency,
        day_count: DayCount,
        sorting: int,
        adjustment: Adjustment,
        business_day_convention: BusinessDayConvention,
    ):
        super().__init__(value, label)
        self.currency = currency
        self.symbol = symbol
        self.payment_frequency = payment_frequency
        self.day_count = day_count
        self.sorting = sorting
        self.adjustment = adjustment
        self.business_day_convention = business_day_convention


class FloatingFundingBasis(FundingBasis):
    def __init__(self, *args, index: int, screen_page: str, legal_label: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = "floating"
        self.index = index
        self.screen_page = screen_page
        self.is_callable_basis = True
        self.legal_label = legal_label


class FixedFundingBasis(FundingBasis):
    def __init__(self, *args, legal_label: str, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = "fixed"
        self.index = 0
        self.is_callable_basis = False
        self.legal_label = legal_label


class MSFundingBasis(FundingBasis):
    def __init__(self, *args, display_payment_frequency: PaymentFrequency, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = "ms"
        self.index = 0
        self.is_callable_basis = False
        self.display_payment_frequency = display_payment_frequency


class GovieFundingBasis(FundingBasis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.basis_type = "govie"
        self.index = 0
        self.is_callable_basis = False


class FundingBases(Constants):
    # BASIS_3M_EUR_VALUE = "3M_EUR"
    # BASIS_6M_EUR_VALUE = "6M_EUR"
    # BASIS_FIXED_EUR_VALUE = "FIXED_EUR"
    # BASIS_MS_EUR_VALUE = "MS_EUR"
    # BASIS_3M_USD_VALUE = "3M_USD"
    # BASIS_6M_USD_VALUE = "6M_USD"
    # BASIS_FIXED_USD_VALUE = "FIXED_USD"
    # BASIS_MS_USD_VALUE = "MS_USD"
    # BASIS_SONIA_GBP_VALUE = "SONIA"
    # BASIS_3M_GBP_VALUE = "3M_GBP"
    # BASIS_6M_GBP_VALUE = "6M_GBP"
    # BASIS_FIXED_GBP_VALUE = "FIXED_GBP"
    # BASIS_MS_GBP_VALUE = "MS_GBP"
    # BASIS_3M_JPY_VALUE = "3M_JPY"
    # BASIS_6M_JPY_VALUE = "6M_JPY"
    # BASIS_FIXED_JPY_VALUE = "FIXED_JPY"
    # BASIS_MS_JPY_VALUE = "MS_JPY"
    # BASIS_3M_CHF_VALUE = "3M_CHF"
    # BASIS_6M_CHF_VALUE = "6M_CHF"
    # BASIS_FIXED_CHF_VALUE = "FIXED_CHF"
    # BASIS_3M_AUD_VALUE = "3M_AUD"
    # BASIS_6M_AUD_VALUE = "6M_AUD"
    # BASIS_FIXED_AUD_VALUE = "FIXED_AUD"
    # BASIS_3M_SEK_VALUE = "3M_SEK"
    # BASIS_FIXED_SEK_VALUE = "FIXED_SEK"
    # BASIS_3M_NOK_VALUE = "3M_NOK"
    # BASIS_6M_NOK_VALUE = "6M_NOK"
    # BASIS_FIXED_NOK_VALUE = "FIXED_NOK"
    # BASIS_3M_CAD_VALUE = "3M_CAD"
    # BASIS_FIXED_CAD_VALUE = "FIXED_CAD"
    # BASIS_3M_NZD_VALUE = "3M_NZD"
    # BASIS_FIXED_NZD_VALUE = "FIXED_NZD"
    # BASIS_3M_HKD_VALUE = "3M_HKD"
    # BASIS_6M_HKD_VALUE = "6M_HKD"
    # BASIS_FIXED_HKD_VALUE = "FIXED_HKD"
    # BASIS_3M_SGD_VALUE = "3M_SGD"
    # BASIS_6M_SGD_VALUE = "6M_SGD"
    # BASIS_FIXED_SGD_VALUE = "FIXED_SGD"
    # BASIS_FIXED_CNH_VALUE = "FIXED_CNH"
    # BASIS_FIXED_CNY_VALUE = "FIXED_CNY"
    # BASIS_3M_ZAR_VALUE = "3M_ZAR"
    # BASIS_6M_ZAR_VALUE = "6M_ZAR"
    # BASIS_FIXED_ZAR_VALUE = "FIXED_ZAR"
    # BASIS_MS_CHF_VALUE = "MS_CHF"
    # BASIS_MS_AUD_VALUE = "MS_AUD"
    # BASIS_MS_SEK_VALUE = "MS_SEK"
    # BASIS_MS_NOK_VALUE = "MS_NOK"
    # BASIS_MS_CAD_VALUE = "MS_CAD"
    # BASIS_MS_NZD_VALUE = "MS_NZD"
    # BASIS_BTP_VALUE = "BTP"
    # BASIS_OAT_VALUE = "OAT"
    # BASIS_OLO_VALUE = "OLO"
    # BASIS_RAGB_VALUE = "RAGB"
    # BASIS_SPGB_VALUE = "SPGB"
    # BASIS_3M_CZK_VALUE = "3M_CZK"
    # BASIS_FIXED_CZK_VALUE = "FIXED_CZK"
    # BASIS_FIXED_KRW_VALUE = "FIXED_KRW"

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
        adjustment=ADJUSTMENTS.ADJUSTED,
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
        display_payment_frequency=PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        day_count=DAY_COUNTS.THIRTY_360,
        adjustment=ADJUSTMENTS.ADJUSTED,
        business_day_convention=BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        sorting=70,
    )

    # BASIS_SONIA_GBP_VALUE: {
    #     "currency": "GBP",
    #     "symbol": "£",
    #     "type": "floating",
    #     "index": 0,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 75,
    #     "label": "SONIA",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "non_pricing": True,
    #     "legal_label": "Compounded Daily SONIA",
    #     "screen_page": "SONIA",
    # },
    # BASIS_3M_GBP_VALUE: {
    #     "currency": "GBP",
    #     "symbol": "£",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 80,
    #     "label": "3mGBP-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month GBP LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_6M_GBP_VALUE: {
    #     "currency": "GBP",
    #     "symbol": "£",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 90,
    #     "label": "6mGBP-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month GBP LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_FIXED_GBP_VALUE: {
    #     "currency": "GBP",
    #     "symbol": "£",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 100,
    #     "label": "GBP Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_FOLLOWING,
    #     "legal_label": "Fixed Rate GBP",
    # },
    # BASIS_MS_GBP_VALUE: {
    #     "currency": "GBP",
    #     "symbol": "£",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "sorting": 110,
    #     "label": "GBP M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_GBP_VALUE
    #     ],
    # },
    # BASIS_3M_JPY_VALUE: {
    #     "currency": "JPY",
    #     "symbol": "¥",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 120,
    #     "label": "3mJPY-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month JPY LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_6M_JPY_VALUE: {
    #     "currency": "JPY",
    #     "symbol": "¥",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 130,
    #     "label": "6mJPY-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month JPY LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_FIXED_JPY_VALUE: {
    #     "currency": "JPY",
    #     "symbol": "¥",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 140,
    #     "label": "JPY Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate JPY",
    # },
    # BASIS_MS_JPY_VALUE: {
    #     "currency": "JPY",
    #     "symbol": "JPY",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365_NL,
    #     "sorting": 150,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "JPY M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_JPY_VALUE
    #     ],
    # },
    # BASIS_3M_CHF_VALUE: {
    #     "currency": "CHF",
    #     "symbol": "CHF",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 160,
    #     "label": "3mCHF-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month CHF LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_6M_CHF_VALUE: {
    #     "currency": "CHF",
    #     "symbol": "CHF",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 170,
    #     "label": "6mCHF-LIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month CHF LIBOR",
    #     "screen_page": "LIBOR01",
    # },
    # BASIS_FIXED_CHF_VALUE: {
    #     "currency": "CHF",
    #     "symbol": "CHF",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 180,
    #     "label": "CHF Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_FOLLOWING,
    #     "legal_label": "Fixed Rate CHF",
    # },
    # BASIS_MS_CHF_VALUE: {
    #     "currency": "CHF",
    #     "symbol": "CHF",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 190,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "CHF M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_CHF_VALUE
    #     ],
    # },
    # BASIS_3M_AUD_VALUE: {
    #     "currency": "AUD",
    #     "symbol": "AUD",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 200,
    #     "label": "3mBBSW",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month BBSW",
    #     "screen_page": "BBSW",
    # },
    # BASIS_6M_AUD_VALUE: {
    #     "currency": "AUD",
    #     "symbol": "AUD",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 210,
    #     "label": "6mBBSW",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month BBSW",
    #     "screen_page": "BBSW",
    # },
    # BASIS_FIXED_AUD_VALUE: {
    #     "currency": "AUD",
    #     "symbol": "AUD",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 220,
    #     "label": "AUD Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate AUD",
    # },
    # BASIS_MS_AUD_VALUE: {
    #     "currency": "AUD",
    #     "symbol": "AUD",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 230,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "AUD M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_AUD_VALUE
    #     ],
    # },
    # BASIS_3M_SEK_VALUE: {
    #     "currency": "SEK",
    #     "symbol": "SEK",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 240,
    #     "label": "3mSTIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month STIBOR",
    #     "screen_page": "SIDE",
    # },
    # BASIS_FIXED_SEK_VALUE: {
    #     "currency": "SEK",
    #     "symbol": "SEK",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 250,
    #     "label": "SEK Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_FOLLOWING,
    #     "legal_label": "SEK Fixed Rate",
    # },
    # BASIS_MS_SEK_VALUE: {
    #     "currency": "SEK",
    #     "symbol": "SEK",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 260,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "SEK M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_SEK_VALUE
    #     ],
    # },
    # BASIS_3M_NOK_VALUE: {
    #     "currency": "NOK",
    #     "symbol": "NOK",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 270,
    #     "label": "3mNIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month NIBOR",
    #     "screen_page": "NIBRO",
    # },
    # BASIS_6M_NOK_VALUE: {
    #     "currency": "NOK",
    #     "symbol": "NOK",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_360,
    #     "sorting": 280,
    #     "label": "6mNIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month NIBOR",
    #     "screen_page": "NIBRO",
    # },
    # BASIS_FIXED_NOK_VALUE: {
    #     "currency": "NOK",
    #     "symbol": "NOK",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 290,
    #     "label": "NOK Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_UNADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_FOLLOWING,
    #     "legal_label": "NOK Fixed Rate",
    # },
    # BASIS_MS_NOK_VALUE: {
    #     "currency": "NOK",
    #     "symbol": "NOK",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_THIRTY_360,
    #     "sorting": 300,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "NOK M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_NOK_VALUE
    #     ],
    # },
    # BASIS_3M_CAD_VALUE: {
    #     "currency": "CAD",
    #     "symbol": "CAD",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 310,
    #     "label": "3mCAD-BA-CDOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month BA-CDOR",
    #     "screen_page": "CDOR",
    # },
    # BASIS_FIXED_CAD_VALUE: {
    #     "currency": "CAD",
    #     "symbol": "CAD",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 320,
    #     "label": "CAD Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "CAD Fixed Rate",
    # },
    # BASIS_MS_CAD_VALUE: {
    #     "currency": "CAD",
    #     "symbol": "CAD",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 330,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "CAD M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_CAD_VALUE
    #     ],
    # },
    # BASIS_3M_NZD_VALUE: {
    #     "currency": "NZD",
    #     "symbol": "NZD",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 340,
    #     "label": "3mNZD-BB",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month NZD-BB",
    #     "screen_page": "",
    # },
    # BASIS_FIXED_NZD_VALUE: {
    #     "currency": "NZD",
    #     "symbol": "NZD",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 350,
    #     "label": "NZD Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate NZD",
    # },
    # BASIS_MS_NZD_VALUE: {
    #     "currency": "NZD",
    #     "symbol": "NZD",
    #     "type": "ms",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 360,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "label": "NZD M/S",
    #     "is_callable_basis": False,
    #     "ms_display_only_payment_freq": MS_DISPLAY_ONLY_PAYMENT_FREQ_MAPPING[
    #         BASIS_MS_NZD_VALUE
    #     ],
    # },
    # BASIS_3M_HKD_VALUE: {
    #     "currency": "HKD",
    #     "symbol": "HKD",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 368,
    #     "label": "3mHIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month HIBOR",
    #     "screen_page": "HKABHIBOR",
    # },
    # BASIS_6M_HKD_VALUE: {
    #     "currency": "HKD",
    #     "symbol": "HKD",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 369,
    #     "label": "6mHIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month HIBOR",
    #     "screen_page": "HKABHIBOR",
    # },
    # BASIS_FIXED_HKD_VALUE: {
    #     "currency": "HKD",
    #     "symbol": "HKD",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 370,
    #     "label": "HKD Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate HKD",
    # },
    # BASIS_3M_SGD_VALUE: {
    #     "currency": "SGD",
    #     "symbol": "SGD",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 373,
    #     "label": "3mSIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "3 month SIBOR",
    #     "screen_page": "ABSIRFIX01",
    # },
    # BASIS_6M_SGD_VALUE: {
    #     "currency": "SGD",
    #     "symbol": "SGD",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 374,
    #     "label": "6mSIBOR",
    #     "is_callable_basis": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "6 month SIBOR",
    #     "screen_page": "ABSIRFIX01",
    # },
    # BASIS_FIXED_SGD_VALUE: {
    #     "currency": "SGD",
    #     "symbol": "SGD",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 375,
    #     "label": "SGD Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate SGD",
    # },
    # BASIS_FIXED_CNH_VALUE: {
    #     "currency": "CNH",
    #     "symbol": "CNH",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 380,
    #     "label": "CNH Fixed",
    #     "is_callable_basis": False,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate CNH",
    # },
    # BASIS_FIXED_CNY_VALUE: {
    #     "currency": "CNY",
    #     "symbol": "CNY",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 381,
    #     "label": "CNY Fixed",
    #     "is_callable_basis": False,
    #     "non_pricing": True,
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "legal_label": "Fixed Rate CNY",
    # },
    # BASIS_FIXED_KRW_VALUE: {
    #     "currency": "KRW",
    #     "symbol": "₩",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 382,
    #     "label": "KRW Fixed",
    #     "is_callable_basis": False,
    #     "non_pricing": True,
    #     "legal_label": "Fixed Rate KRW",
    # },
    # BASIS_3M_CZK_VALUE: {
    #     "currency": "CZK",
    #     "symbol": "CZK",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 383,
    #     "label": "3mPRIBOR",
    #     "is_callable_basis": False,
    #     "non_pricing": True,
    #     "legal_label": "3 month CZK-PRIBOR-PRBO",
    #     "screen_page": "PRBO",
    # },
    # BASIS_FIXED_CZK_VALUE: {
    #     "currency": "CZK",
    #     "symbol": "CZK",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 384,
    #     "label": "CZK Fixed",
    #     "is_callable_basis": False,
    #     "non_pricing": True,
    #     "legal_label": "Fixed Rate CZK",
    # },
    # BASIS_3M_ZAR_VALUE: {
    #     "currency": "ZAR",
    #     "symbol": "ZAR",
    #     "type": "floating",
    #     "index": 3,
    #     "payment_freq": CONVERSION_QUARTERLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 385,
    #     "label": "3mJIBAR",
    #     "is_callable_basis": True,
    #     "non_pricing": True,
    #     "legal_label": "3 month JIBAR",
    #     "screen_page": "SAFEY",
    # },
    # BASIS_6M_ZAR_VALUE: {
    #     "currency": "ZAR",
    #     "symbol": "ZAR",
    #     "type": "floating",
    #     "index": 6,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 386,
    #     "label": "6mJIBAR",
    #     "is_callable_basis": True,
    #     "non_pricing": True,
    #     "legal_label": "6 month JIBAR",
    #     "screen_page": "SAFEY",
    # },
    # BASIS_FIXED_ZAR_VALUE: {
    #     "currency": "ZAR",
    #     "symbol": "ZAR",
    #     "type": "fixed",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_365,
    #     "sorting": 387,
    #     "label": "ZAR Fixed",
    #     "is_callable_basis": False,
    #     "non_pricing": True,
    #     "legal_label": "Fixed Rate ZAR",
    # },
    # BASIS_BTP_VALUE: {
    #     "currency": "EUR",
    #     "symbol": "€",
    #     "type": "govie",
    #     "index": 0,
    #     "payment_freq": CONVERSION_SEMI_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 390,
    #     "label": "BTP",
    #     "is_callable_basis": False,
    #     "ref_issuer_shortname": "Rep Italy",
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "max_tenor": TENOR_45Y_VAL,
    #     "min_tenor": TENOR_1Y_VAL,
    # },
    # BASIS_OAT_VALUE: {
    #     "currency": "EUR",
    #     "symbol": "€",
    #     "type": "govie",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 400,
    #     "label": "OAT",
    #     "is_callable_basis": False,
    #     "ref_issuer_shortname": "French Rep",
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "max_tenor": TENOR_45Y_VAL,
    #     "min_tenor": TENOR_1Y_VAL,
    # },
    # BASIS_OLO_VALUE: {
    #     "currency": "EUR",
    #     "symbol": "€",
    #     "type": "govie",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 410,
    #     "label": "OLO",
    #     "is_callable_basis": False,
    #     "ref_issuer_shortname": "Kdom Belgium",
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "max_tenor": TENOR_45Y_VAL,
    #     "min_tenor": TENOR_1Y_VAL,
    # },
    # BASIS_RAGB_VALUE: {
    #     "currency": "EUR",
    #     "symbol": "€",
    #     "type": "govie",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 420,
    #     "label": "RAGB",
    #     "is_callable_basis": False,
    #     "ref_issuer_shortname": "Rep Austria",
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "max_tenor": TENOR_25Y_VAL,
    #     "min_tenor": TENOR_1Y_VAL,
    # },
    # BASIS_SPGB_VALUE: {
    #     "currency": "EUR",
    #     "symbol": "€",
    #     "type": "govie",
    #     "index": 0,
    #     "payment_freq": CONVERSION_ANNUALLY,
    #     "daycount": CONVERSION_DCB_ACTUAL_ACTUAL_ICMA,
    #     "sorting": 430,
    #     "label": "SPGB",
    #     "is_callable_basis": False,
    #     "ref_issuer_shortname": "Kdom Spain",
    #     "adjustment": ADJUSTMENT_ADJUSTED,
    #     "business_day_convention": BUSINESS_DAY_CONVENTION_MODIFIED_FOLLOWING,
    #     "max_tenor": TENOR_45Y_VAL,
    #     "min_tenor": TENOR_1Y_VAL,
    # },
    # }


class MTNFundingBases(FundingBases):
    pass


class CDFundingBases(FundingBases):
    USD_FIXED = FixedFundingBasis(
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


FUNDING_BASES = FundingBases()
MTN_FUNDING_BASES = MTNFundingBases()
CD_FUNDING_BASES = CDFundingBases()
