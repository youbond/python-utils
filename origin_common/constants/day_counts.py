from origin_common.constants.base import Constant, Constants


class DayCount(Constant[str]):
    pass


class DayCounts(Constants):
    ACTUAL_ACTUAL_ICMA = DayCount("ActualActualICMA", "ACT/ACT (ICMA)")
    ACTUAL_365 = DayCount("Actual365Fixed", "ACT/365F")
    THIRTY_360 = DayCount("Thirty360", "30/360")
    ACTUAL_360 = DayCount("Actual360", "ACT/360")
    ACTUAL_365_NL = DayCount("Actual365NoLeap", "NL/365")


DAY_COUNTS = DayCounts()
DAY_COUNTS.make_immutable()
