from unittest import TestCase

from origin_common.constants import ADJUSTMENTS


class TestAdjustmentValues(TestCase):
    def test_adjusted(self):
        assert ADJUSTMENTS.ADJUSTED.value == "Adjusted"

    def test_unadjusted(self):
        assert ADJUSTMENTS.UNADJUSTED.value == "Unadjusted"


class TestAdjustmentLabels(TestCase):
    def test_adjusted(self):
        assert ADJUSTMENTS.ADJUSTED.label == "Adjusted"

    def test_unadjusted(self):
        assert ADJUSTMENTS.UNADJUSTED.label == "Unadjusted"


class TestAdjustmentOrder(TestCase):
    def test_order(self):
        expected = [
            ADJUSTMENTS.ADJUSTED,
            ADJUSTMENTS.UNADJUSTED,
        ]
        assert list(ADJUSTMENTS) == expected

    def test_django_choices(self):
        expected = (
            (ADJUSTMENTS.ADJUSTED.value, ADJUSTMENTS.ADJUSTED.label),
            (ADJUSTMENTS.UNADJUSTED.value, ADJUSTMENTS.UNADJUSTED.label),
        )
        assert ADJUSTMENTS.to_django_choices() == expected


class TestAdjustmentComparisons(TestCase):
    def test_less_than_day_count(self):
        assert ADJUSTMENTS.ADJUSTED < ADJUSTMENTS.UNADJUSTED
        assert ADJUSTMENTS.UNADJUSTED <= ADJUSTMENTS.UNADJUSTED

    def test_less_than_string(self):
        assert ADJUSTMENTS.ADJUSTED < ADJUSTMENTS.UNADJUSTED.value
        assert ADJUSTMENTS.ADJUSTED <= ADJUSTMENTS.UNADJUSTED.value
        assert ADJUSTMENTS.ADJUSTED.value < ADJUSTMENTS.UNADJUSTED
        assert ADJUSTMENTS.UNADJUSTED.value <= ADJUSTMENTS.UNADJUSTED

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert ADJUSTMENTS.ADJUSTED < 100
        with self.assertRaises(TypeError):
            assert ADJUSTMENTS.ADJUSTED >= 1

    def test_cannot_compare_to_non_day_count_strings(self):
        with self.assertRaises(TypeError):
            assert ADJUSTMENTS.ADJUSTED < "FOO"
        with self.assertRaises(TypeError):
            assert ADJUSTMENTS.ADJUSTED >= "BAR"

    def test_greater_than_day_count(self):
        assert ADJUSTMENTS.UNADJUSTED > ADJUSTMENTS.ADJUSTED
        assert ADJUSTMENTS.UNADJUSTED >= ADJUSTMENTS.UNADJUSTED

    def test_greater_than_string(self):
        assert ADJUSTMENTS.UNADJUSTED.value > ADJUSTMENTS.ADJUSTED
        assert ADJUSTMENTS.UNADJUSTED.value >= ADJUSTMENTS.ADJUSTED
        assert ADJUSTMENTS.UNADJUSTED > ADJUSTMENTS.ADJUSTED.value
        assert ADJUSTMENTS.UNADJUSTED >= ADJUSTMENTS.UNADJUSTED.value
