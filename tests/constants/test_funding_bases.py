from datetime import time
from random import choice
from unittest import TestCase

from origin_common.better_test_mixins import LruCacheTestMixin
from origin_common.constants import (
    ADJUSTMENTS,
    BUSINESS_DAY_CONVENTIONS,
    CALENDARS,
    CD_FUNDING_BASES,
    DAY_COUNTS,
    FUNDING_BASES,
    MTN_FUNDING_BASES,
    PAYMENT_FREQUENCIES,
)
from origin_common.constants.funding_bases import (
    BANK_BILL_RATE,
    BBSW,
    CAD_BA_CDOR,
    EURIBOR,
    HIBOR,
    JIBAR,
    LIBOR_TWO_DAYS,
    LIBOR_ZERO_DAYS,
    NIBOR,
    PRIBOR,
    SIBOR,
    SONIA,
    STIBOR,
)


class FixingInfoTestMixin:
    fixing_info = None
    benchmark_base = None
    days_prior_to_fixing = None
    fixing_time = None
    fixing_location = None
    calendar = None

    def test_benchmark_base(self):
        assert self.fixing_info.benchmark_base == self.benchmark_base

    def test_days_prior_to_fixing(self):
        assert self.fixing_info.days_prior_to_fixing == self.days_prior_to_fixing

    def test_fixing_time(self):
        assert self.fixing_info.fixing_time == self.fixing_time

    def test_fixing_location(self):
        assert self.fixing_info.fixing_location == self.fixing_location

    def test_calendar(self):
        assert self.fixing_info.calendar == self.calendar


class TestEuriborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = EURIBOR
    benchmark_base = "EURIBOR"
    days_prior_to_fixing = 2
    fixing_time = time(hour=11)
    fixing_location = "Brussels"
    calendar = CALENDARS.TARGET2


class TestLiborTwoDaysFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = LIBOR_TWO_DAYS
    benchmark_base = "LIBOR"
    days_prior_to_fixing = 2
    fixing_time = time(hour=11)
    fixing_location = "London"
    calendar = CALENDARS.LONDON


class TestLiborZeroDaysFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = LIBOR_ZERO_DAYS
    benchmark_base = "LIBOR"
    days_prior_to_fixing = 0
    fixing_time = time(hour=11)
    fixing_location = "London"
    calendar = CALENDARS.LONDON


class TestSoniaFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = SONIA
    benchmark_base = "SONIA"
    days_prior_to_fixing = 5
    fixing_time = time(hour=9)
    fixing_location = "London"
    calendar = CALENDARS.LONDON


class TestBBSWFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = BBSW
    benchmark_base = "BBSW"
    days_prior_to_fixing = 0
    fixing_time = time(hour=10)
    fixing_location = "Sydney"
    calendar = CALENDARS.SYDNEY


class TestStiborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = STIBOR
    benchmark_base = "STIBOR"
    days_prior_to_fixing = 2
    fixing_time = time(hour=11)
    fixing_location = "(CET)"
    calendar = CALENDARS.STOCKHOLM


class TestNiborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = NIBOR
    benchmark_base = "NIBOR"
    days_prior_to_fixing = 2
    fixing_time = time(hour=11)
    fixing_location = "(CET)"
    calendar = CALENDARS.OSLO


class TestCadBaCdorFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = CAD_BA_CDOR
    benchmark_base = "CAD-BA-CDOR"
    days_prior_to_fixing = 0
    fixing_time = time(hour=10)
    fixing_location = "Toronto"
    calendar = CALENDARS.TORONTO


class TestBankBillRateFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = BANK_BILL_RATE
    benchmark_base = "Bank Bill Rate"
    days_prior_to_fixing = 0
    fixing_time = time(hour=11)
    fixing_location = "Auckland"
    calendar = CALENDARS.AUCKLAND


class TestPriborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = PRIBOR
    benchmark_base = "PRIBOR"
    days_prior_to_fixing = 2
    fixing_time = time(hour=11)
    fixing_location = "Prague"
    calendar = CALENDARS.PRAGUE


class TestHiborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = HIBOR
    benchmark_base = "HIBOR"
    days_prior_to_fixing = 0
    fixing_time = time(hour=11)
    fixing_location = "Hong Kong"
    calendar = CALENDARS.HONG_KONG


class TestSiborFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = SIBOR
    benchmark_base = "SIBOR"
    days_prior_to_fixing = 0
    fixing_time = time(hour=11)
    fixing_location = "Singapore"
    calendar = CALENDARS.SINGAPORE


class TestJibarFixingInfo(FixingInfoTestMixin, TestCase):
    fixing_info = JIBAR
    benchmark_base = "JIBAR"
    days_prior_to_fixing = 0
    fixing_time = time(hour=12)
    fixing_location = "Johannesburg"
    calendar = CALENDARS.JOHANNESBURG


class BasisTestCase(TestCase):
    default_attributes = {
        "basis_type": "fixed",
        "index": 0,
        "is_callable_basis": False,
        "pricing": True,
        "adjustment": None,
        "business_day_convention": None,
        "calendars_for_payment": [],
    }
    attributes = {}
    basis = None
    is_fixed_basis = False
    is_floating_basis = False
    is_ms_basis = False
    is_govie_basis = False
    fixing_info = None

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

    def test_fixing_info(self):
        if self.fixing_info:
            assert self.basis.fixing_info is self.fixing_info
        else:
            assert not hasattr(self.basis, "fixing_info")


class TestEUR3mBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_3M
    is_floating_basis = True
    fixing_info = EURIBOR
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
        "calendars_for_payment": [CALENDARS.TARGET2],
    }


class TestEUR6mBasis(BasisTestCase):
    basis = FUNDING_BASES.EUR_6M
    is_floating_basis = True
    fixing_info = EURIBOR
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
        "calendars_for_payment": [CALENDARS.TARGET2],
    }


class TestEURFixedBasisForMTN(BasisTestCase):
    basis = MTN_FUNDING_BASES.EUR_FIXED
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
        "calendars_for_payment": [CALENDARS.TARGET2],
    }


class TestEURFixedBasisForCD(BasisTestCase):
    basis = CD_FUNDING_BASES.EUR_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_EUR",
        "currency": "EUR",
        "symbol": "€",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 20,
        "label": "EUR Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate EUR",
        "calendars_for_payment": [CALENDARS.TARGET2],
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
        "floating_basis": FUNDING_BASES.EUR_6M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.TARGET2],
    }


class TestUSD3mBasis(BasisTestCase):
    basis = FUNDING_BASES.USD_3M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.NEW_YORK],
    }


class TestUSD6mBasis(BasisTestCase):
    basis = FUNDING_BASES.USD_6M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.NEW_YORK],
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
        "calendars_for_payment": [CALENDARS.NEW_YORK],
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
        "calendars_for_payment": [CALENDARS.NEW_YORK],
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
        "floating_basis": FUNDING_BASES.USD_3M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.NEW_YORK],
    }


class TestGBPSoniaBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_SONIA
    is_floating_basis = True
    fixing_info = SONIA
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
        "calendars_for_payment": [CALENDARS.LONDON],
    }


class TestGBP3MBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_3M
    is_floating_basis = True
    fixing_info = LIBOR_ZERO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON],
    }


class TestGBP6MBasis(BasisTestCase):
    basis = FUNDING_BASES.GBP_6M
    is_floating_basis = True
    fixing_info = LIBOR_ZERO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON],
    }


class TestGBPFIXEDBasisForMTN(BasisTestCase):
    basis = MTN_FUNDING_BASES.GBP_FIXED
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
        "calendars_for_payment": [CALENDARS.LONDON],
    }


class TestGBPFIXEDBasisForCD(BasisTestCase):
    basis = CD_FUNDING_BASES.GBP_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_GBP",
        "currency": "GBP",
        "symbol": "£",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365,
        "sorting": 100,
        "label": "GBP Fixed",
        "is_callable_basis": False,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "legal_label": "Fixed Rate GBP",
        "calendars_for_payment": [CALENDARS.LONDON],
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
        "floating_basis": FUNDING_BASES.GBP_6M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_365,
        "calendars_for_payment": [CALENDARS.LONDON],
    }


class TestJPY3MBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_3M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.TOKYO],
    }


class TestJPY6MBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_6M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.TOKYO],
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
        "calendars_for_payment": [CALENDARS.TOKYO],
    }


class TestJPYMSBasis(BasisTestCase):
    basis = FUNDING_BASES.JPY_MS
    is_ms_basis = True
    attributes = {
        "value": "MS_JPY",
        "currency": "JPY",
        "symbol": "¥",
        "basis_type": "ms",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_365_NL,
        "sorting": 150,
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "label": "JPY M/S",
        "is_callable_basis": False,
        "floating_basis": FUNDING_BASES.JPY_6M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.TOKYO],
    }


class TestCHF3MBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_3M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.ZURICH],
    }


class TestCHF6MBasis(BasisTestCase):
    basis = FUNDING_BASES.CHF_6M
    is_floating_basis = True
    fixing_info = LIBOR_TWO_DAYS
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
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.ZURICH],
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
        "calendars_for_payment": [CALENDARS.ZURICH],
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
        "floating_basis": FUNDING_BASES.CHF_6M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.LONDON, CALENDARS.ZURICH],
    }


class TestAUD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_3M
    is_floating_basis = True
    fixing_info = BBSW
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
        "calendars_for_payment": [CALENDARS.SYDNEY],
    }


class TestAUD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.AUD_6M
    is_floating_basis = True
    fixing_info = BBSW
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
        "calendars_for_payment": [CALENDARS.SYDNEY],
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
        "calendars_for_payment": [CALENDARS.SYDNEY],
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
        "floating_basis": FUNDING_BASES.AUD_3M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_365,
        "calendars_for_payment": [CALENDARS.SYDNEY],
    }


class TestSEK3MBasis(BasisTestCase):
    basis = FUNDING_BASES.SEK_3M
    is_floating_basis = True
    fixing_info = STIBOR
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
        "calendars_for_payment": [CALENDARS.STOCKHOLM],
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
        "calendars_for_payment": [CALENDARS.STOCKHOLM],
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
        "floating_basis": FUNDING_BASES.SEK_3M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.STOCKHOLM],
    }


class TestNOK3MBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_3M
    is_floating_basis = True
    fixing_info = NIBOR
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
        "screen_page": "ORIBOR",
        "calendars_for_payment": [CALENDARS.OSLO],
    }


class TestNOK6MBasis(BasisTestCase):
    basis = FUNDING_BASES.NOK_6M
    is_floating_basis = True
    fixing_info = NIBOR
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
        "screen_page": "ORIBOR",
        "calendars_for_payment": [CALENDARS.OSLO],
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
        "calendars_for_payment": [CALENDARS.OSLO],
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
        "floating_basis": FUNDING_BASES.NOK_6M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_360,
        "calendars_for_payment": [CALENDARS.OSLO],
    }


class TestCAD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.CAD_3M
    is_floating_basis = True
    fixing_info = CAD_BA_CDOR
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
        "calendars_for_payment": [CALENDARS.TORONTO],
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
        "calendars_for_payment": [CALENDARS.TORONTO],
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
        "floating_basis": FUNDING_BASES.CAD_3M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_365,
        "calendars_for_payment": [CALENDARS.TORONTO],
    }


class TestNZD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.NZD_3M
    is_floating_basis = True
    fixing_info = BANK_BILL_RATE
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
        "calendars_for_payment": [CALENDARS.AUCKLAND],
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
        "calendars_for_payment": [CALENDARS.AUCKLAND],
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
        "floating_basis": FUNDING_BASES.NZD_3M,
        "ms_payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "display_payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "ms_day_count": DAY_COUNTS.ACTUAL_365,
        "calendars_for_payment": [CALENDARS.AUCKLAND],
    }


class TestHKD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.HKD_3M
    is_floating_basis = True
    fixing_info = HIBOR
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
        "calendars_for_payment": [CALENDARS.HONG_KONG],
    }


class TestHKD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.HKD_6M
    is_floating_basis = True
    fixing_info = HIBOR
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
        "calendars_for_payment": [CALENDARS.HONG_KONG],
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
        "calendars_for_payment": [CALENDARS.HONG_KONG],
    }


class TestSGD3MBasis(BasisTestCase):
    basis = FUNDING_BASES.SGD_3M
    is_floating_basis = True
    fixing_info = SIBOR
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
        "calendars_for_payment": [CALENDARS.SINGAPORE],
    }


class TestSGD6MBasis(BasisTestCase):
    basis = FUNDING_BASES.SGD_6M
    is_floating_basis = True
    fixing_info = SIBOR
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
        "calendars_for_payment": [CALENDARS.SINGAPORE],
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
        "calendars_for_payment": [CALENDARS.SINGAPORE],
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
    fixing_info = PRIBOR
    attributes = {
        "value": "3M_CZK",
        "currency": "CZK",
        "symbol": "CZK",
        "basis_type": "floating",
        "index": 3,
        "payment_frequency": PAYMENT_FREQUENCIES.QUARTERLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 383,
        "label": "3mPRIBOR",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "3 month PRIBOR",
        "screen_page": "PRIBOR",
    }


class TestCZK6MBasis(BasisTestCase):
    basis = FUNDING_BASES.CZK_6M
    is_floating_basis = True
    fixing_info = PRIBOR
    attributes = {
        "value": "6M_CZK",
        "currency": "CZK",
        "symbol": "CZK",
        "basis_type": "floating",
        "index": 6,
        "payment_frequency": PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_360,
        "sorting": 384,
        "label": "6mPRIBOR",
        "adjustment": ADJUSTMENTS.ADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "6 month PRIBOR",
        "screen_page": "PRIBOR",
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
    fixing_info = JIBAR
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
        "calendars_for_payment": [CALENDARS.JOHANNESBURG],
    }


class TestZAR6MBasis(BasisTestCase):
    basis = FUNDING_BASES.ZAR_6M
    is_floating_basis = True
    fixing_info = JIBAR
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
        "calendars_for_payment": [CALENDARS.JOHANNESBURG],
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
        "calendars_for_payment": [CALENDARS.JOHANNESBURG],
    }


class TestRONFIXEDBasis(BasisTestCase):
    basis = FUNDING_BASES.RON_FIXED
    is_fixed_basis = True
    attributes = {
        "value": "FIXED_RON",
        "currency": "RON",
        "symbol": "RON",
        "basis_type": "fixed",
        "index": 0,
        "payment_frequency": PAYMENT_FREQUENCIES.ANNUALLY,
        "day_count": DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
        "sorting": 388,
        "label": "RON Fixed",
        "is_callable_basis": False,
        "pricing": False,
        "legal_label": "Fixed Rate RON",
        "adjustment": ADJUSTMENTS.UNADJUSTED,
        "business_day_convention": BUSINESS_DAY_CONVENTIONS.FOLLOWING,
        "calendars_for_payment": [CALENDARS.BUCHAREST],
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
        "calendars_for_payment": [CALENDARS.TARGET2],
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
        "calendars_for_payment": [CALENDARS.TARGET2],
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
        "calendars_for_payment": [CALENDARS.TARGET2],
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
        "calendars_for_payment": [CALENDARS.TARGET2],
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
        "calendars_for_payment": [CALENDARS.TARGET2],
    }


class TestMTNFundingBasesOrder(LruCacheTestMixin, TestCase):
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
        self.assert_has_lru_cache(MTN_FUNDING_BASES.to_django_choices)

    def test_django_choices_for_callable_basis(self):
        rand_bool = choice([True, False])
        expected = tuple(
            (basis.value, basis.label)
            for basis in sorted(MTN_FUNDING_BASES, key=lambda x: x.sorting)
            if basis.is_callable_basis is rand_bool
        )
        actual = MTN_FUNDING_BASES.to_django_choices(is_callable_basis=rand_bool)
        assert actual == expected
        self.assert_has_lru_cache(MTN_FUNDING_BASES.to_django_choices)

    def test_django_choices_for_pricing(self):
        rand_bool = choice([True, False])
        expected = tuple(
            (basis.value, basis.label)
            for basis in sorted(MTN_FUNDING_BASES, key=lambda x: x.sorting)
            if basis.pricing is rand_bool
        )
        actual = MTN_FUNDING_BASES.to_django_choices(pricing=rand_bool)
        assert actual == expected
        self.assert_has_lru_cache(MTN_FUNDING_BASES.to_django_choices)


class TestCDFundingBasesOrder(LruCacheTestMixin, TestCase):
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
        self.assert_has_lru_cache(CD_FUNDING_BASES.to_django_choices)


class TestFundingBasisComparisons(TestCase):
    def test_less_than_funding_basis(self):
        assert FUNDING_BASES.EUR_3M < FUNDING_BASES.JPY_FIXED
        assert FUNDING_BASES.JPY_FIXED <= FUNDING_BASES.JPY_FIXED

    def test_less_than_string(self):
        assert FUNDING_BASES.EUR_3M < FUNDING_BASES.JPY_FIXED.value
        assert FUNDING_BASES.EUR_3M <= FUNDING_BASES.JPY_FIXED.value
        assert FUNDING_BASES.EUR_3M.value < FUNDING_BASES.JPY_FIXED
        assert FUNDING_BASES.JPY_FIXED.value <= FUNDING_BASES.JPY_FIXED

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert FUNDING_BASES.EUR_3M < 100
        with self.assertRaises(TypeError):
            assert FUNDING_BASES.EUR_3M >= 1

    def test_cannot_compare_to_non_funding_basis_strings(self):
        with self.assertRaises(TypeError):
            assert FUNDING_BASES.EUR_3M < "FOO"
        with self.assertRaises(TypeError):
            assert FUNDING_BASES.EUR_3M >= "BAR"

    def test_greater_than_funding_basis(self):
        assert FUNDING_BASES.JPY_FIXED > FUNDING_BASES.EUR_3M
        assert FUNDING_BASES.JPY_FIXED >= FUNDING_BASES.JPY_FIXED

    def test_greater_than_string(self):
        assert FUNDING_BASES.JPY_FIXED.value > FUNDING_BASES.EUR_3M
        assert FUNDING_BASES.JPY_FIXED.value >= FUNDING_BASES.EUR_3M
        assert FUNDING_BASES.JPY_FIXED > FUNDING_BASES.EUR_3M.value
        assert FUNDING_BASES.JPY_FIXED >= FUNDING_BASES.JPY_FIXED.value
