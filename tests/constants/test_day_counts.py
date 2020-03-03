from unittest import TestCase

from origin_common.better_test_mixins import LruCacheTestMixin
from origin_common.constants import DAY_COUNTS


class TestDayCountValues(TestCase):
    def test_act_act(self):
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA.value == "ActualActualICMA"

    def test_act_365(self):
        assert DAY_COUNTS.ACTUAL_365.value == "Actual365Fixed"

    def test_act_365_no_leap(self):
        assert DAY_COUNTS.ACTUAL_365_NL.value == "Actual365NoLeap"

    def test_act_360(self):
        assert DAY_COUNTS.ACTUAL_360.value == "Actual360"

    def test_30_360(self):
        assert DAY_COUNTS.THIRTY_360.value == "Thirty360"


class TestDayCountLabels(TestCase):
    def test_act_act(self):
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA.label == "ACT/ACT (ICMA)"

    def test_act_365(self):
        assert DAY_COUNTS.ACTUAL_365.label == "ACT/365F"

    def test_act_365_no_leap(self):
        assert DAY_COUNTS.ACTUAL_365_NL.label == "NL/365"

    def test_act_360(self):
        assert DAY_COUNTS.ACTUAL_360.label == "ACT/360"

    def test_30_360(self):
        assert DAY_COUNTS.THIRTY_360.label == "30/360"


class TestDayCountOrder(LruCacheTestMixin, TestCase):
    def test_order(self):
        expected = [
            DAY_COUNTS.ACTUAL_ACTUAL_ICMA,
            DAY_COUNTS.ACTUAL_365,
            DAY_COUNTS.THIRTY_360,
            DAY_COUNTS.ACTUAL_360,
            DAY_COUNTS.ACTUAL_365_NL,
        ]
        assert list(DAY_COUNTS) == expected

    def test_django_choices(self):
        expected = (
            (DAY_COUNTS.ACTUAL_ACTUAL_ICMA.value, DAY_COUNTS.ACTUAL_ACTUAL_ICMA.label),
            (DAY_COUNTS.ACTUAL_365.value, DAY_COUNTS.ACTUAL_365.label),
            (DAY_COUNTS.THIRTY_360.value, DAY_COUNTS.THIRTY_360.label),
            (DAY_COUNTS.ACTUAL_360.value, DAY_COUNTS.ACTUAL_360.label),
            (DAY_COUNTS.ACTUAL_365_NL.value, DAY_COUNTS.ACTUAL_365_NL.label),
        )
        assert DAY_COUNTS.to_django_choices() == expected
        self.assert_has_lru_cache(DAY_COUNTS.to_django_choices)


class TestDayCountComparisons(TestCase):
    def test_less_than_day_count(self):
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA < DAY_COUNTS.ACTUAL_365_NL
        assert DAY_COUNTS.ACTUAL_365_NL <= DAY_COUNTS.ACTUAL_365_NL

    def test_less_than_string(self):
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA < DAY_COUNTS.ACTUAL_365_NL.value
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA <= DAY_COUNTS.ACTUAL_365_NL.value
        assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA.value < DAY_COUNTS.ACTUAL_365_NL
        assert DAY_COUNTS.ACTUAL_365_NL.value <= DAY_COUNTS.ACTUAL_365_NL

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA < 100
        with self.assertRaises(TypeError):
            assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA >= 1

    def test_cannot_compare_to_non_day_count_strings(self):
        with self.assertRaises(TypeError):
            assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA < "FOO"
        with self.assertRaises(TypeError):
            assert DAY_COUNTS.ACTUAL_ACTUAL_ICMA >= "BAR"

    def test_greater_than_day_count(self):
        assert DAY_COUNTS.ACTUAL_365_NL > DAY_COUNTS.ACTUAL_ACTUAL_ICMA
        assert DAY_COUNTS.ACTUAL_365_NL >= DAY_COUNTS.ACTUAL_365_NL

    def test_greater_than_string(self):
        assert DAY_COUNTS.ACTUAL_365_NL.value > DAY_COUNTS.ACTUAL_ACTUAL_ICMA
        assert DAY_COUNTS.ACTUAL_365_NL.value >= DAY_COUNTS.ACTUAL_ACTUAL_ICMA
        assert DAY_COUNTS.ACTUAL_365_NL > DAY_COUNTS.ACTUAL_ACTUAL_ICMA.value
        assert DAY_COUNTS.ACTUAL_365_NL >= DAY_COUNTS.ACTUAL_365_NL.value
