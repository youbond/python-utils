from unittest import TestCase

from origin_common.constants import (
    ADJUSTMENTS,
    BUSINESS_DAY_CONVENTIONS,
    CD_FUNDING_BASES,
    DAY_COUNTS,
    FUNDING_BASES,
    MTN_FUNDING_BASES,
    PAYMENT_FREQUENCIES,
)


class BasisTestCase(TestCase):
    default_attributes = {
        "basis_type": "fixed",
        "index": 0,
        "is_callable_basis": False,
        "pricing": True,
        "adjustment": None,
        "business_day_convention": None,
    }
    attributes = {}
    basis = None
    is_fixed_basis = False
    is_floating_basis = False
    is_ms_basis = False
    is_govie_basis = False

    def test_attributes(self):
        if not self.attributes:
            return
        attributes_to_test = dict(self.default_attributes)
        attributes_to_test.update(self.attributes)
        for key, value in attributes_to_test.items():
            assert getattr(self.basis, key) == value, key

    def test_is_fixed_basis(self):
        if self.basis:
            assert self.basis.is_fixed_basis is self.is_fixed_basis

    def test_is_floating_basis(self):
        if self.basis:
            assert self.basis.is_floating_basis is self.is_floating_basis

    def test_is_ms_basis(self):
        if self.basis:
            assert self.basis.is_ms_basis is self.is_ms_basis

    def test_is_govie_basis(self):
        if self.basis:
            assert self.basis.is_govie_basis is self.is_govie_basis


class TestEUR3mBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_EUR",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 0,
        "label": "3mEURIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month EURIBOR",
        "screen_page": "EURIBOR01",
    }


class TestEUR6mBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_EUR",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 10,
        "label": "6mEURIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month EURIBOR",
        "screen_page": "EURIBOR01",
    }


class TestEURFixedBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_EUR",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 20,
        "label": "EUR Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "Fixed Rate EUR",
    }


class TestEURMSBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_EUR",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "sorting": 30,
        "label": "EUR M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
    }


class TestUSD3mBasis(BasisTestCase):
    basis = FUNDING_BASES.USD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_USD",
        "currency": "USD",
        "symbol": "$",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 40,
        "label": "3mUSD-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month USD LIBOR",
        "screen_page": "LIBOR01",
    }


class TestUSD6mBasis(BasisTestCase):
    basis = FUNDING_BASES.USD_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_USD",
        "currency": "USD",
        "symbol": "$",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 50,
        "label": "6mUSD-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month USD LIBOR",
        "screen_page": "LIBOR01",
    }


class TestUSDFixedBasisForMTN(BasisTestCase):
    basis = MTN_FUNDING_BASES.USD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_USD",
        "currency": "USD",
        "symbol": "$",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 60,
        "label": "USD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "Fixed Rate USD",
    }


class TestUSDFixedBasisForCD(BasisTestCase):
    basis = CD_FUNDING_BASES.USD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_USD",
        "currency": "USD",
        "symbol": "$",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 60,
        "label": "USD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate USD",
    }


class TestUSDMSBasis(BasisTestCase):
    basis = FUNDING_BASES.USD_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_USD",
        "currency": "USD",
        "symbol": "$",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "sorting": 70,
        "label": "USD M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
    }


class TestGBPSoniaBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_SONIA
    is_floating_basis = True
    attributes = {
        "value": "SONIA",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "floating",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 75,
        "label": "SONIA",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "pricing": False,
        "legal_label": "Compounded Daily SONIA",
        "screen_page": "SONIA",
    }


class TestGBP3MBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_GBP",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 80,
        "label": "3mGBP-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month GBP LIBOR",
        "screen_page": "LIBOR01",
    }


class TestGBP6MBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_GBP",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 90,
        "label": "6mGBP-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month GBP LIBOR",
        "screen_page": "LIBOR01",
    }


class TestGBPFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_GBP",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 100,
        "label": "GBP Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "Fixed Rate GBP",
    }


class TestGBPMSBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_GBP",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "sorting": 110,
        "label": "GBP M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
    }


class TestJPY3MBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_JPY",
        "currency": "JPY",
        "symbol": "¥",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 120,
        "label": "3mJPY-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month JPY LIBOR",
        "screen_page": "LIBOR01",
    }


class TestJPY6MBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_JPY",
        "currency": "JPY",
        "symbol": "¥",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 130,
        "label": "6mJPY-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month JPY LIBOR",
        "screen_page": "LIBOR01",
    }


class TestJPYFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_JPY",
        "currency": "JPY",
        "symbol": "¥",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 140,
        "label": "JPY Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate JPY",
    }


class TestJPYMSBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_JPY",
        "currency": "JPY",
        "symbol": "JPY",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365_NL,
        "sorting": 150,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "JPY M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
    }


class TestCHF3MBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_CHF",
        "currency": "CHF",
        "symbol": "CHF",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 160,
        "label": "3mCHF-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month CHF LIBOR",
        "screen_page": "LIBOR01",
    }


class TestCHF6MBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_CHF",
        "currency": "CHF",
        "symbol": "CHF",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 170,
        "label": "6mCHF-LIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month CHF LIBOR",
        "screen_page": "LIBOR01",
    }


class TestCHFFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_CHF",
        "currency": "CHF",
        "symbol": "CHF",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 180,
        "label": "CHF Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "Fixed Rate CHF",
    }


class TestCHFMSBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_CHF",
        "currency": "CHF",
        "symbol": "CHF",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 190,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "CHF M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
    }


class TestAUD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_AUD",
        "currency": "AUD",
        "symbol": "AUD",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 200,
        "label": "3mBBSW",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month BBSW",
        "screen_page": "BBSW",
    }


class TestAUD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_AUD",
        "currency": "AUD",
        "symbol": "AUD",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 210,
        "label": "6mBBSW",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month BBSW",
        "screen_page": "BBSW",
    }


class TestAUDFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_AUD",
        "currency": "AUD",
        "symbol": "AUD",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 220,
        "label": "AUD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate AUD",
    }


class TestAUDMSBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_AUD",
        "currency": "AUD",
        "symbol": "AUD",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 230,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "AUD M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
    }


class TestSEK3MBasis(BasisTestCase):
    basis = FUNDING_BASES.SEK_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_SEK",
        "currency": "SEK",
        "symbol": "SEK",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 240,
        "label": "3mSTIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month STIBOR",
        "screen_page": "SIDE",
    }


class TestSEKFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.SEK_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_SEK",
        "currency": "SEK",
        "symbol": "SEK",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 250,
        "label": "SEK Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "SEK Fixed Rate",
    }


class TestSEKMSBasis(BasisTestCase):
    basis = FUNDING_BASES.SEK_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_SEK",
        "currency": "SEK",
        "symbol": "SEK",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 260,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "SEK M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
    }


class TestNOK3MBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_NOK",
        "currency": "NOK",
        "symbol": "NOK",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 270,
        "label": "3mNIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month NIBOR",
        "screen_page": "NIBRO",
    }


class TestNOK6MBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_NOK",
        "currency": "NOK",
        "symbol": "NOK",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 280,
        "label": "6mNIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month NIBOR",
        "screen_page": "NIBRO",
    }


class TestNOKFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_NOK",
        "currency": "NOK",
        "symbol": "NOK",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 290,
        "label": "NOK Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "legal_label": "NOK Fixed Rate",
    }


class TestNOKMSBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_NOK",
        "currency": "NOK",
        "symbol": "NOK",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.THIRTY_360,
        "sorting": 300,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "NOK M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
    }


class TestCAD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.CAD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_CAD",
        "currency": "CAD",
        "symbol": "CAD",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 310,
        "label": "3mCAD-BA-CDOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month BA-CDOR",
        "screen_page": "CDOR",
    }


class TestCADFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.CAD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_CAD",
        "currency": "CAD",
        "symbol": "CAD",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 320,
        "label": "CAD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "CAD Fixed Rate",
    }


class TestCADMSBasis(BasisTestCase):
    basis = FUNDING_BASES.CAD_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_CAD",
        "currency": "CAD",
        "symbol": "CAD",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 330,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "CAD M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
    }


class TestNZD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.NZD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_NZD",
        "currency": "NZD",
        "symbol": "NZD",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 340,
        "label": "3mNZD-BB",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month NZD-BB",
        "screen_page": "",
    }


class TestNZDFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.NZD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_NZD",
        "currency": "NZD",
        "symbol": "NZD",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 350,
        "label": "NZD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate NZD",
    }


class TestNZDMSBasis(BasisTestCase):
    basis = FUNDING_BASES.NZD_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_NZD",
        "currency": "NZD",
        "symbol": "NZD",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 360,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "NZD M/S",
        "is_callable_basis": False,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
    }


class TestHKD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.HKD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_HKD",
        "currency": "HKD",
        "symbol": "HKD",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 368,
        "label": "3mHIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month HIBOR",
        "screen_page": "HKABHIBOR",
    }


class TestHKD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.HKD_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_HKD",
        "currency": "HKD",
        "symbol": "HKD",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 369,
        "label": "6mHIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month HIBOR",
        "screen_page": "HKABHIBOR",
    }


class TestHKDFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.HKD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_HKD",
        "currency": "HKD",
        "symbol": "HKD",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 370,
        "label": "HKD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate HKD",
    }


class TestSGD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.SGD_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_SGD",
        "currency": "SGD",
        "symbol": "SGD",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 373,
        "label": "3mSIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "3 month SIBOR",
        "screen_page": "ABSIRFIX01",
    }


class TestSGD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.SGD_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_SGD",
        "currency": "SGD",
        "symbol": "SGD",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 374,
        "label": "6mSIBOR",
        "is_callable_basis": True,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "6 month SIBOR",
        "screen_page": "ABSIRFIX01",
    }


class TestSGDFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.SGD_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_SGD",
        "currency": "SGD",
        "symbol": "SGD",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 375,
        "label": "SGD Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate SGD",
    }


class TestCNHFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.CNH_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_CNH",
        "currency": "CNH",
        "symbol": "CNH",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 380,
        "label": "CNH Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate CNH",
    }


class TestCNYFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.CNY_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_CNY",
        "currency": "CNY",
        "symbol": "CNY",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 381,
        "label": "CNY Fixed",
        "is_callable_basis": False,
        "pricing": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate CNY",
    }


class TestKRWFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.KRW_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_KRW",
        "currency": "KRW",
        "symbol": "₩",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 382,
        "label": "KRW Fixed",
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "Fixed Rate KRW",
    }


class TestCZK3MBasis(BasisTestCase):
    basis = FUNDING_BASES.CZK_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_CZK",
        "currency": "CZK",
        "symbol": "CZK",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 383,
        "label": "3mPRIBOR",
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "3 month CZK-PRIBOR-PRBO",
        "screen_page": "PRBO",
    }


class TestCZKFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.CZK_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_CZK",
        "currency": "CZK",
        "symbol": "CZK",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 384,
        "label": "CZK Fixed",
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "Fixed Rate CZK",
    }


class TestZAR3MBasis(BasisTestCase):
    basis = FUNDING_BASES.ZAR_3M
    is_floating_basis = True
    attributes = {
        "value": "3M_ZAR",
        "currency": "ZAR",
        "symbol": "ZAR",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 385,
        "label": "3mJIBAR",
        "is_callable_basis": True,
        "pricing": False,
        "legal_label": "3 month JIBAR",
        "screen_page": "SAFEY",
    }


class TestZAR6MBasis(BasisTestCase):
    basis = FUNDING_BASES.ZAR_6M
    is_floating_basis = True
    attributes = {
        "value": "6M_ZAR",
        "currency": "ZAR",
        "symbol": "ZAR",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 386,
        "label": "6mJIBAR",
        "is_callable_basis": True,
        "pricing": False,
        "legal_label": "6 month JIBAR",
        "screen_page": "SAFEY",
    }


class TestZARFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.ZAR_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_ZAR",
        "currency": "ZAR",
        "symbol": "ZAR",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 387,
        "label": "ZAR Fixed",
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "Fixed Rate ZAR",
    }


class TestBTPBasis(BasisTestCase):
    basis = FUNDING_BASES.BTP
    is_govie_basis = True
    attributes = {
        "value": "BTP",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "govie",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 390,
        "label": "BTP",
        "is_callable_basis": False,
        "issuer_short_name": "Rep Italy",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # "max_tenor": TENOR_45Y_VAL,
        # "min_tenor": TENOR_1Y_VAL,
    }


class TestOATBasis(BasisTestCase):
    basis = FUNDING_BASES.OAT
    is_govie_basis = True
    attributes = {
        "value": "OAT",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "govie",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 400,
        "label": "OAT",
        "is_callable_basis": False,
        "issuer_short_name": "French Rep",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # "max_tenor": TENOR_45Y_VAL,
        # "min_tenor": TENOR_1Y_VAL,
    }


class TestOLOBasis(BasisTestCase):
    basis = FUNDING_BASES.OLO
    is_govie_basis = True
    attributes = {
        "value": "OLO",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "govie",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 410,
        "label": "OLO",
        "is_callable_basis": False,
        "issuer_short_name": "Kdom Belgium",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # "max_tenor": TENOR_45Y_VAL,
        # "min_tenor": TENOR_1Y_VAL,
    }


class TestRAGBBasis(BasisTestCase):
    basis = FUNDING_BASES.RAGB
    is_govie_basis = True
    attributes = {
        "value": "RAGB",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "govie",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 420,
        "label": "RAGB",
        "is_callable_basis": False,
        "issuer_short_name": "Rep Austria",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # "max_tenor": TENOR_25Y_VAL,
        # "min_tenor": TENOR_1Y_VAL,
    }


class TestSPGBBasis(BasisTestCase):
    basis = FUNDING_BASES.SPGB
    is_govie_basis = True
    attributes = {
        "value": "SPGB",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "govie",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 430,
        "label": "SPGB",
        "is_callable_basis": False,
        "issuer_short_name": "Kdom Spain",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        # "max_tenor": TENOR_45Y_VAL,
        # "min_tenor": TENOR_1Y_VAL,
    }


class TestMTNFundingBasesOrder(TestCase):
    def test_order(self):
        # we expect it to be sorted according to this value
        # but currently implementation is based on declaration order
        expected = sorted(MTN_FUNDING_BASES, key=lambda x: x.sorting)
        assert list(MTN_FUNDING_BASES) == expected

    def test_django_choices(self):
        expected = tuple(
            (basis.value, basis.label)
            for basis in sorted(MTN_FUNDING_BASES, key=lambda x: x.sorting)
        )
        assert MTN_FUNDING_BASES.to_django_choices() == expected


class TestCDFundingBasesOrder(TestCase):
    def test_order(self):
        # we expect it to be sorted according to this value
        # but currently implementation is based on declaration order
        expected = sorted(CD_FUNDING_BASES, key=lambda x: x.sorting)
        assert list(CD_FUNDING_BASES) == expected

    def test_django_choices(self):
        expected = tuple(
            (basis.value, basis.label)
            for basis in sorted(CD_FUNDING_BASES, key=lambda x: x.sorting)
        )
        assert CD_FUNDING_BASES.to_django_choices() == expected
