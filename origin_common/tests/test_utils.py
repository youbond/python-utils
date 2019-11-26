from datetime import timedelta
from unittest import TestCase

from origin_common.utils import (
    DAYS_IN_A_MONTH,
    DAYS_IN_A_WEEK,
    DAYS_IN_A_YEAR,
    expand_duration_unit,
    join_list,
    string_to_timedelta,
    timedelta_to_string,
)


class TestExpandDurationUnit(TestCase):
    def test_week(self):
        assert expand_duration_unit("W") == "Week"

    def test_month(self):
        assert expand_duration_unit("M") == "Month"

    def test_year(self):
        assert expand_duration_unit("Y") == "Year"

    def test_default(self):
        assert expand_duration_unit("O/N") == "O/N"


class TestJoinList(TestCase):
    def test_can_join_list(self):
        value = ["a", "b", "c"]
        expected = "a, b & c"
        assert join_list(value) == expected

    def test_original_list_is_not_changed(self):
        value = ["a", "b", "c"]
        join_list(value)
        assert value == ["a", "b", "c"]

    def test_if_only_one_item_it_is_returned_as_a_string(self):
        class Dummy(object):
            def __str__(self):
                return "Dummy Object"

        value = [Dummy()]
        assert join_list(value) == "Dummy Object"

    def test_if_only_two_items_return_with_and(self):
        value = ["a", "b"]
        expected = "a & b"
        assert join_list(value) == expected

    def test_delimiter_can_be_changed(self):
        value = ["a", "b", "c", "d"]
        expected = "a-b-c & d"
        assert join_list(value, delimiter="-") == expected

    def test_last_delimiter_can_be_changed(self):
        value = ["a", "b", "c", "d"]
        expected = "a, b, c blahblah d"
        assert join_list(value, last_delimiter=" blahblah ") == expected

    def test_empty_lists_return_blank_string(self):
        assert join_list([]) == ""


class TestStringToTimedelta(TestCase):
    def test_match(self):
        values = {
            # input: expected
            "Overnight": timedelta(days=1),
            "O/N": timedelta(days=1),
            "1w": timedelta(days=1 * DAYS_IN_A_WEEK),
            "1W": timedelta(days=1 * DAYS_IN_A_WEEK),
            "1 week": timedelta(days=1 * DAYS_IN_A_WEEK),
            "1week": timedelta(days=1 * DAYS_IN_A_WEEK),
            "1 wk": timedelta(days=1 * DAYS_IN_A_WEEK),
            "1wk": timedelta(days=1 * DAYS_IN_A_WEEK),
            "2 weeks": timedelta(days=2 * DAYS_IN_A_WEEK),
            "2 wks": timedelta(days=2 * DAYS_IN_A_WEEK),
            "1": timedelta(days=1 * DAYS_IN_A_YEAR),
            "1Y": timedelta(days=1 * DAYS_IN_A_YEAR),
            "1 year": timedelta(days=1 * DAYS_IN_A_YEAR),
            "1year": timedelta(days=1 * DAYS_IN_A_YEAR),
            "1 yr": timedelta(days=1 * DAYS_IN_A_YEAR),
            "1yr": timedelta(days=1 * DAYS_IN_A_YEAR),
            "10years": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10 years": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10yrs": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10 yrs": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10y": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10 y": timedelta(days=10 * DAYS_IN_A_YEAR),
            "10 Y": timedelta(days=10 * DAYS_IN_A_YEAR),
            "1m": timedelta(days=1 * DAYS_IN_A_MONTH),
            "1M": timedelta(days=1 * DAYS_IN_A_MONTH),
            "1 month": timedelta(days=1 * DAYS_IN_A_MONTH),
            "1month": timedelta(days=1 * DAYS_IN_A_MONTH),
            "10months": timedelta(days=10 * DAYS_IN_A_MONTH),
            "10 months": timedelta(days=10 * DAYS_IN_A_MONTH),
            "1 yonth": None,
            "1 meay": None,
            "1 ms": None,
            "1 ys": None,
            "month": None,
            "year": None,
            "m": None,
            "y": None,
        }
        for input_string, expected in values.items():
            if expected is None:
                self.assertRaises(
                    ValueError, string_to_timedelta, input_string=input_string
                ), input_string
            else:
                assert (
                    string_to_timedelta(input_string=input_string) == expected
                ), input_string

    def test_returns_tuple_if_string_is_range(self):
        values = {
            # input: expected
            "1-10M": (
                timedelta(days=1 * DAYS_IN_A_MONTH),
                timedelta(days=10 * DAYS_IN_A_MONTH),
            ),
            "1-10": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1-10Y": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1-10 year": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1-10year": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1-10 yr": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1-10yr": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1 - 10years": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
            "1 - 10 years": (
                timedelta(days=1 * DAYS_IN_A_YEAR),
                timedelta(days=10 * DAYS_IN_A_YEAR),
            ),
        }
        for input_string, expected in values.items():
            assert (
                string_to_timedelta(input_string=input_string) == expected
            ), input_string
        expected = (
            timedelta(days=1 * DAYS_IN_A_MONTH),
            timedelta(days=10 * DAYS_IN_A_YEAR),
        )
        assert string_to_timedelta("1M - 10 Y") == expected
        assert string_to_timedelta("  O/n    - 1Y") == (
            timedelta(days=1),
            timedelta(days=1 * DAYS_IN_A_YEAR),
        )

    def test_raises_error_for_invalid_ranges(self):
        self.assertRaises(ValueError, string_to_timedelta, "1Y - 10M")
        self.assertRaises(
            ValueError, string_to_timedelta, "1Y -- 10Y"
        )  # double dash is invalid

    def test_ignores_asterisk(self):
        assert string_to_timedelta("1Y*") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("10m*") == timedelta(days=10 * DAYS_IN_A_MONTH)

    def test_ignores_whitespace(self):
        assert string_to_timedelta(" 1Y") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1Y ") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta(" 1Y ") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1 Y") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1      Y") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1\tY") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1\tY\t\t") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("1\nY") == timedelta(days=1 * DAYS_IN_A_YEAR)

    def test_ignores_nc(self):
        assert string_to_timedelta("NC1Y") == timedelta(days=1 * DAYS_IN_A_YEAR)
        assert string_to_timedelta("nc10m") == timedelta(days=10 * DAYS_IN_A_MONTH)
        assert string_to_timedelta(" nc 10m") == timedelta(days=10 * DAYS_IN_A_MONTH)

    def test_returns_timedelta_unchanged(self):
        td = timedelta(days=4 * DAYS_IN_A_YEAR)
        assert string_to_timedelta(td) is td


class TestTimedeltaToString(TestCase):
    def test_non_initial_units_is_correct(self):
        tenors_to_test = {
            timedelta(days=0): "0",
            timedelta(days=1): "Overnight",
            timedelta(days=1 * DAYS_IN_A_WEEK): "1 Week",
            timedelta(days=2 * DAYS_IN_A_WEEK): "2 Weeks",
            timedelta(days=1 * DAYS_IN_A_MONTH): "1 Month",
            timedelta(days=10 * DAYS_IN_A_MONTH): "10 Months",
            timedelta(days=1 * DAYS_IN_A_YEAR): "1 Year",
            timedelta(days=10 * DAYS_IN_A_YEAR): "10 Years",
        }

        for tenor, label in tenors_to_test.items():
            assert timedelta_to_string(tenor, only_initial=False) == label

    def test_returns_proper_label(self):
        assert timedelta_to_string(timedelta(days=0)) == "0"
        assert timedelta_to_string(timedelta(days=1)) == "O/N"
        assert timedelta_to_string(timedelta(days=2 * DAYS_IN_A_WEEK)) == "2W"
        assert timedelta_to_string(timedelta(days=6 * DAYS_IN_A_MONTH)) == "6M"
        assert timedelta_to_string(timedelta(days=1 * DAYS_IN_A_YEAR)) == "1Y"
        assert timedelta_to_string(timedelta(days=99 * DAYS_IN_A_YEAR)) == "99Y"
        assert timedelta_to_string(timedelta(days=54 * DAYS_IN_A_MONTH)) == "4.5Y"

    def test_returns_months_for_time_between_1Y_to_18M_unless_quarter_year(self):
        assert timedelta_to_string(timedelta(days=13 * DAYS_IN_A_MONTH)) == "13M"
        assert timedelta_to_string(timedelta(days=14 * DAYS_IN_A_MONTH)) == "14M"
        assert timedelta_to_string(timedelta(days=15 * DAYS_IN_A_MONTH)) == "1.25Y"
        assert timedelta_to_string(timedelta(days=16 * DAYS_IN_A_MONTH)) == "16M"
        assert timedelta_to_string(timedelta(days=17 * DAYS_IN_A_MONTH)) == "17M"
        assert timedelta_to_string(timedelta(days=18 * DAYS_IN_A_MONTH)) == "1.5Y"
        assert timedelta_to_string(timedelta(days=19 * DAYS_IN_A_MONTH)) == "19M"
        assert timedelta_to_string(timedelta(days=20 * DAYS_IN_A_MONTH)) == "20M"
        assert timedelta_to_string(timedelta(days=21 * DAYS_IN_A_MONTH)) == "1.75Y"
        assert timedelta_to_string(timedelta(days=22 * DAYS_IN_A_MONTH)) == "22M"
        assert timedelta_to_string(timedelta(days=23 * DAYS_IN_A_MONTH)) == "23M"
        assert timedelta_to_string(timedelta(days=24 * DAYS_IN_A_MONTH)) == "2Y"

    def test_values_for_quantlib(self):
        assert timedelta_to_string(timedelta(days=1), for_quantlib=True) == "1D"
        timedelta_string = timedelta_to_string(
            timedelta(days=1.5 * DAYS_IN_A_YEAR), for_quantlib=True
        )
        assert timedelta_string == "1Y6M"
        timedelta_string = timedelta_to_string(
            timedelta(days=18 * DAYS_IN_A_MONTH), for_quantlib=True
        )
        assert timedelta_string == "1Y6M"

    def test_returns_string_unchanged(self):
        assert timedelta_to_string("1 day") == "1 day"

    def test_returns_none_unchanged(self):
        assert timedelta_to_string(None) is None

    def test_can_round_to_n_digits(self):
        t = string_to_timedelta("10.234Y")
        timedelta_string = timedelta_to_string(t, round_ndigits=3, only_quarter_years=False)
        assert timedelta_string == "10.234Y"
