import re
from datetime import timedelta

SECONDS_IN_A_DAY = 86400.0
DAYS_IN_A_YEAR = 365.25
DAYS_IN_A_MONTH = DAYS_IN_A_YEAR / 12
DAYS_IN_A_WEEK = DAYS_IN_A_YEAR / 52
TIMEDELTA_STRING_REGEX = re.compile(
    r"^\s*(?:nc)?\s*(\d+(?:\.\d+)?)\s*(m(?:onths?)?"
    r"|y(?:ea)?(?:rs?)?|w(?:ee)?(?:ks?)?)?\*?\s*$",
    flags=re.IGNORECASE,
)


def expand_duration_unit(unit):
    if unit == "W":
        return "Week"
    if unit == "M":
        return "Month"
    if unit == "Y":
        return "Year"
    return unit


def __get_duration_units(duration, round_ndigits=None, only_quarter_years=True):
    total_days = duration.total_seconds() / SECONDS_IN_A_DAY
    if total_days < DAYS_IN_A_MONTH:
        value, units = (total_days // DAYS_IN_A_WEEK), "W"
    elif total_days < DAYS_IN_A_YEAR or (
        only_quarter_years and duration % timedelta(days=3 * DAYS_IN_A_MONTH)
    ):
        value, units = (total_days / DAYS_IN_A_MONTH), "M"
    else:
        value, units = (total_days / DAYS_IN_A_YEAR), "Y"
    if round_ndigits is not None:
        value = round(value, round_ndigits)
    if value.is_integer():
        value = int(value)
    return units, value


def __get_number_of_day(units):
    """Given units, return the number of days as a float."""
    multiplier = DAYS_IN_A_YEAR
    if units:
        if units.lower().startswith("w"):
            multiplier = DAYS_IN_A_WEEK
        elif units.lower().startswith("m"):
            multiplier = DAYS_IN_A_MONTH
    return multiplier


def join_list(
    object_list: list, delimiter: str = ", ", last_delimiter: str = " & "
) -> str:
    """
    Takes a list ["a", "b", "c"] and returns a string "a, b & c"
    :param object_list: The list that needs to be joined
    :param last_delimiter: The string to join the last element with the rest of the string
    :param delimiter: The string to join all the elements (except last) of the list
    """
    if not object_list:
        return ""
    list_copy = list(object_list)
    last = list_copy.pop()
    if list_copy:
        return "{}{}{}".format(delimiter.join(list_copy), last_delimiter, last)
    return "{}".format(last)


def string_to_timedelta(input_string, return_units=False):
    if isinstance(input_string, timedelta):
        return input_string

    split_input = input_string.split("-", maxsplit=1)
    if len(split_input) == 2:
        start, start_unit = string_to_timedelta(split_input[0], return_units=True)
        end, end_unit = string_to_timedelta(split_input[1], return_units=True)

        if start_unit is None:
            total_days = (
                start.total_seconds()
                / SECONDS_IN_A_DAY
                / DAYS_IN_A_YEAR
                * __get_number_of_day(end_unit)
            )
            start = timedelta(days=total_days)
        if end < start:
            raise ValueError('Invalid input "{}"!'.format(input_string))
        return start, end

    match = TIMEDELTA_STRING_REGEX.match(input_string)
    if not match:
        input_string = input_string.strip()
        if input_string.lower() == "overnight" or input_string.upper() == "O/N":
            if return_units:
                return timedelta(days=1), "O/N"
            return timedelta(days=1)
        raise ValueError('Invalid input "{}"!'.format(input_string))

    period_start, units = match.groups()

    multiplier = __get_number_of_day(units)
    if return_units:
        return timedelta(days=float(period_start) * multiplier), units
    return timedelta(days=float(period_start) * multiplier)


def timedelta_to_string(
    duration,
    only_initial=True,
    round_ndigits=None,
    only_quarter_years=True,
    for_quantlib=False,
):
    assert (
        not for_quantlib or for_quantlib is only_initial
    ), "QuantLib requires only initials"
    if isinstance(duration, str):
        return duration
    if duration is None:
        return None
    if not duration:
        return "0"  # no units for 0
    if duration == timedelta(days=1):
        if for_quantlib:
            return "1D"
        if only_initial:
            return "O/N"
        return "Overnight"

    units, value = __get_duration_units(duration, round_ndigits, only_quarter_years)
    if for_quantlib and isinstance(value, float):
        int_part, decimal_part = str(value).split(".")
        return "{}{}".format(
            timedelta_to_string(string_to_timedelta("{}{}".format(int_part, units))),
            timedelta_to_string(
                string_to_timedelta("0.{}{}".format(decimal_part, units))
            ),
        )
    if only_initial:
        return "{}{}".format(value, units)
    if value > 1:
        return "{} {}s".format(value, expand_duration_unit(units))
    return "{} {}".format(value, expand_duration_unit(units))
