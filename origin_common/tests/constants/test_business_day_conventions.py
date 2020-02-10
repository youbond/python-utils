from unittest import TestCase

from origin_common.constants import BUSINESS_DAY_CONVENTIONS


class TestBusinessDayConventionValues(TestCase):
    def test_following(self):
        assert BUSINESS_DAY_CONVENTIONS.FOLLOWING.value == "Following"

    def test_preceding(self):
        assert BUSINESS_DAY_CONVENTIONS.PRECEDING.value == "Preceding"

    def test_modified_following(self):
        assert BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING.value == "Modified Following"

    def test_modified_preceding(self):
        assert BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value == "Modified Preceding"

    def test_half_month_modified_following(self):
        value = BUSINESS_DAY_CONVENTIONS.HALF_MONTH_MODIFIED_FOLLOWING.value
        assert value == "Half Month Modified Following"


class TestBusinessDayConventionLabels(TestCase):
    def test_following(self):
        assert BUSINESS_DAY_CONVENTIONS.FOLLOWING.label == "Following"

    def test_preceding(self):
        assert BUSINESS_DAY_CONVENTIONS.PRECEDING.label == "Preceding"

    def test_modified_following(self):
        assert BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING.label == "Modified Following"

    def test_modified_preceding(self):
        assert BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.label == "Modified Preceding"

    def test_half_month_modified_following(self):
        label = BUSINESS_DAY_CONVENTIONS.HALF_MONTH_MODIFIED_FOLLOWING.label
        assert label == "Half Month Modified Following"


class TestBusinessDayConventionOrder(TestCase):
    def test_order(self):
        expected = [
            BUSINESS_DAY_CONVENTIONS.FOLLOWING,
            BUSINESS_DAY_CONVENTIONS.PRECEDING,
            BUSINESS_DAY_CONVENTIONS.MODIFIED_FOLLOWING,
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING,
            BUSINESS_DAY_CONVENTIONS.HALF_MONTH_MODIFIED_FOLLOWING,
        ]
        assert list(BUSINESS_DAY_CONVENTIONS) == expected

    def test_django_choices(self):
        conventions = BUSINESS_DAY_CONVENTIONS
        expected = (
            (conventions.FOLLOWING.value, conventions.FOLLOWING.label),
            (conventions.PRECEDING.value, conventions.PRECEDING.label),
            (
                conventions.MODIFIED_FOLLOWING.value,
                conventions.MODIFIED_FOLLOWING.label,
            ),
            (
                conventions.MODIFIED_PRECEDING.value,
                conventions.MODIFIED_PRECEDING.label,
            ),
            (
                conventions.HALF_MONTH_MODIFIED_FOLLOWING.value,
                conventions.HALF_MONTH_MODIFIED_FOLLOWING.label,
            ),
        )
        assert BUSINESS_DAY_CONVENTIONS.to_django_choices() == expected


class TestBusinessDayConventionComparisons(TestCase):
    def test_less_than_business_day_convention(self):
        assert (
            BUSINESS_DAY_CONVENTIONS.FOLLOWING
            < BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
            <= BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
        )

    def test_less_than_string(self):
        assert (
            BUSINESS_DAY_CONVENTIONS.FOLLOWING
            < BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.FOLLOWING
            <= BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.FOLLOWING.value
            < BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
            <= BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
        )

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert BUSINESS_DAY_CONVENTIONS.FOLLOWING < 100
        with self.assertRaises(TypeError):
            assert BUSINESS_DAY_CONVENTIONS.FOLLOWING >= 1

    def test_cannot_compare_to_non_business_day_convention_strings(self):
        with self.assertRaises(TypeError):
            assert BUSINESS_DAY_CONVENTIONS.FOLLOWING < "FOO"
        with self.assertRaises(TypeError):
            assert BUSINESS_DAY_CONVENTIONS.FOLLOWING >= "BAR"

    def test_greater_than_business_day_convention(self):
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
            > BUSINESS_DAY_CONVENTIONS.FOLLOWING
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
            >= BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
        )

    def test_greater_than_string(self):
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
            > BUSINESS_DAY_CONVENTIONS.FOLLOWING
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
            >= BUSINESS_DAY_CONVENTIONS.FOLLOWING
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
            > BUSINESS_DAY_CONVENTIONS.FOLLOWING.value
        )
        assert (
            BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING
            >= BUSINESS_DAY_CONVENTIONS.MODIFIED_PRECEDING.value
        )
