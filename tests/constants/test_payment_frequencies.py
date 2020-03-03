from unittest import TestCase

from origin_common.better_test_mixins import LruCacheTestMixin
from origin_common.constants import PAYMENT_FREQUENCIES


class TestPaymentFrequencyValues(TestCase):
    def test_annually_value(self):
        assert PAYMENT_FREQUENCIES.ANNUALLY.value == 12

    def test_semi_annually_value(self):
        assert PAYMENT_FREQUENCIES.SEMI_ANNUALLY.value == 6

    def test_quarterly_value(self):
        assert PAYMENT_FREQUENCIES.QUARTERLY.value == 3

    def test_at_maturity_value(self):
        assert PAYMENT_FREQUENCIES.AT_MATURITY.value == 0


class TestPaymentFrequencyLabels(TestCase):
    def test_annual_value(self):
        assert PAYMENT_FREQUENCIES.ANNUALLY.label == "Annually"

    def test_semi_annual_value(self):
        assert PAYMENT_FREQUENCIES.SEMI_ANNUALLY.label == "Semi-Annually"

    def test_quarterly_value(self):
        assert PAYMENT_FREQUENCIES.QUARTERLY.label == "Quarterly"

    def test_at_maturity_value(self):
        assert PAYMENT_FREQUENCIES.AT_MATURITY.label == "At Maturity"


class TestPaymentFrequencyOrder(LruCacheTestMixin, TestCase):
    def test_order(self):
        expected = [
            PAYMENT_FREQUENCIES.AT_MATURITY,
            PAYMENT_FREQUENCIES.QUARTERLY,
            PAYMENT_FREQUENCIES.SEMI_ANNUALLY,
            PAYMENT_FREQUENCIES.ANNUALLY,
        ]
        assert list(PAYMENT_FREQUENCIES) == expected

    def test_django_choices(self):
        pf = PAYMENT_FREQUENCIES
        expected = (
            (pf.AT_MATURITY.value, pf.AT_MATURITY.label),
            (pf.QUARTERLY.value, pf.QUARTERLY.label),
            (pf.SEMI_ANNUALLY.value, pf.SEMI_ANNUALLY.label),
            (pf.ANNUALLY.value, pf.ANNUALLY.label),
        )
        assert pf.to_django_choices() == expected
        self.assert_has_lru_cache(pf.to_django_choices)


class TestPaymentFrequencyComparisons(TestCase):
    def test_less_than_payment_frequency(self):
        assert PAYMENT_FREQUENCIES.AT_MATURITY < PAYMENT_FREQUENCIES.ANNUALLY
        assert PAYMENT_FREQUENCIES.ANNUALLY <= PAYMENT_FREQUENCIES.ANNUALLY

    def test_less_than_integer(self):
        assert PAYMENT_FREQUENCIES.AT_MATURITY < PAYMENT_FREQUENCIES.ANNUALLY.value
        assert PAYMENT_FREQUENCIES.AT_MATURITY <= PAYMENT_FREQUENCIES.ANNUALLY.value
        assert PAYMENT_FREQUENCIES.AT_MATURITY.value < PAYMENT_FREQUENCIES.ANNUALLY
        assert PAYMENT_FREQUENCIES.ANNUALLY.value <= PAYMENT_FREQUENCIES.ANNUALLY

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert PAYMENT_FREQUENCIES.AT_MATURITY < "Foo"
        with self.assertRaises(TypeError):
            assert PAYMENT_FREQUENCIES.AT_MATURITY >= "Bar"

    def test_cannot_compare_to_non_payment_frequency_integers(self):
        with self.assertRaises(TypeError):
            assert PAYMENT_FREQUENCIES.AT_MATURITY < 10
        with self.assertRaises(TypeError):
            assert PAYMENT_FREQUENCIES.AT_MATURITY >= -1

    def test_greater_than_payment_frequency(self):
        assert PAYMENT_FREQUENCIES.ANNUALLY > PAYMENT_FREQUENCIES.AT_MATURITY
        assert PAYMENT_FREQUENCIES.ANNUALLY >= PAYMENT_FREQUENCIES.ANNUALLY

    def test_greater_than_integer(self):
        assert PAYMENT_FREQUENCIES.ANNUALLY.value > PAYMENT_FREQUENCIES.AT_MATURITY
        assert PAYMENT_FREQUENCIES.ANNUALLY.value >= PAYMENT_FREQUENCIES.AT_MATURITY
        assert PAYMENT_FREQUENCIES.ANNUALLY > PAYMENT_FREQUENCIES.AT_MATURITY.value
        assert PAYMENT_FREQUENCIES.ANNUALLY >= PAYMENT_FREQUENCIES.ANNUALLY.value
