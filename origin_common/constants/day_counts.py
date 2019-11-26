from origin_common.constants.base import Constant, Constants


class DayCount(Constant):
    def __init__(self, value: str, label: str):
        super().__init__(value, label)


class DayCounts(Constants):
    ACTUAL_ACTUAL_ICMA = DayCount("ActualActualICMA", "ACT/ACT (ICMA)")
    ACTUAL_365 = DayCount("Actual365Fixed", "ACT/365F")
    ACTUAL_365_NL = DayCount("Actual365NoLeap", "NL/365")
    THIRTY_360 = DayCount("Thirty360", "30/360")
    ACTUAL_360 = DayCount("Actual360", "ACT/360")


DAY_COUNTS = DayCounts()
