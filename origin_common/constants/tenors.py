import re
from datetime import timedelta

from origin_common.constants.base import Constant, Constants

SECONDS_IN_A_DAY = 86400.0
DAYS_IN_A_YEAR = 365.25
DAYS_IN_A_MONTH = DAYS_IN_A_YEAR / 12
DAYS_IN_A_WEEK = DAYS_IN_A_YEAR / 52


ONE_MONTH_TIMEDELTA = timedelta(days=1 * DAYS_IN_A_MONTH)
THREE_MONTH_TIMEDELTA = timedelta(days=3 * DAYS_IN_A_MONTH)
ONE_YEAR_TIMEDELTA = timedelta(days=1 * DAYS_IN_A_YEAR)


class Tenor(Constant[timedelta]):
    def __init__(self, value: timedelta, label: str, color_code: str):
        super().__init__(value, label)
        self.color_code = color_code
        self.number_of_months = self.get_tenor_months_calculation()

    def get_tenor_months_calculation(self) -> float:
        if self.label == "O/N":
            return 1 / float(DAYS_IN_A_MONTH)  # 1 day is 1/30 months
        regex = r"([\d\.]+)(M|Y|W)"
        number, duration_unit = re.match(regex, self.label).groups()
        if duration_unit == "M":
            return float(number)
        elif duration_unit == "Y":
            return float(number) * DAYS_IN_A_YEAR / DAYS_IN_A_MONTH
        elif duration_unit == "W":
            return (
                float(number) * DAYS_IN_A_WEEK / DAYS_IN_A_MONTH
            )  # 1 week is 7/30 months
        else:
            raise Exception("Invalid tenor")

    @property
    def is_callable_tenor(self):
        return (
            self.value >= ONE_YEAR_TIMEDELTA
            or self.value % THREE_MONTH_TIMEDELTA.days == 0
            or self.value == ONE_MONTH_TIMEDELTA
        )


class Tenors(Constants[Tenor]):
    OVERNIGHT = Tenor(timedelta(days=1), "O/N", "#665241")
    ONE_WEEK = Tenor(timedelta(days=1 * DAYS_IN_A_WEEK), "1W", "#C1B591")
    TWO_WEEK = Tenor(timedelta(days=2 * DAYS_IN_A_WEEK), "2W", "#426B94")
    ONE_MONTH = Tenor(ONE_MONTH_TIMEDELTA, "1M", "#426B94")
    TWO_MONTH = Tenor(timedelta(days=2 * DAYS_IN_A_MONTH), "2M", "#C4A77D")
    THREE_MONTH = Tenor(THREE_MONTH_TIMEDELTA, "3M", "#FF6666")
    FOUR_MONTH = Tenor(timedelta(days=4 * DAYS_IN_A_MONTH), "4M", "#F9613C")
    FIVE_MONTH = Tenor(timedelta(days=5 * DAYS_IN_A_MONTH), "5M", "#F3DFC1")
    SIX_MONTH = Tenor(timedelta(days=6 * DAYS_IN_A_MONTH), "6M", "#856A5D")
    SEVEN_MONTH = Tenor(timedelta(days=7 * DAYS_IN_A_MONTH), "7M", "#1B3022")
    EIGHT_MONTH = Tenor(timedelta(days=8 * DAYS_IN_A_MONTH), "8M", "#395756")
    NINE_MONTH = Tenor(timedelta(days=9 * DAYS_IN_A_MONTH), "9M", "#FFB30F")
    TEN_MONTH = Tenor(timedelta(days=10 * DAYS_IN_A_MONTH), "10M", "#01295F")
    ELEVEN_MONTH = Tenor(timedelta(days=11 * DAYS_IN_A_MONTH), "11M", "#849324")
    ONE_YEAR = Tenor(ONE_YEAR_TIMEDELTA, "1Y", "#204B57")
    ONE_AND_HALF_YEAR = Tenor(timedelta(days=18 * DAYS_IN_A_MONTH), "1.5Y", "#8A716A")
    TWO_YEAR = Tenor(timedelta(days=2 * DAYS_IN_A_YEAR), "2Y", "#EF946C")
    THREE_YEAR = Tenor(timedelta(days=3 * DAYS_IN_A_YEAR), "3Y", "#45C7A6")
    FOUR_YEAR = Tenor(timedelta(days=4 * DAYS_IN_A_YEAR), "4Y", "#2F2963")
    FIVE_YEAR = Tenor(timedelta(days=5 * DAYS_IN_A_YEAR), "5Y", "#3A435E")
    SIX_YEAR = Tenor(timedelta(days=6 * DAYS_IN_A_YEAR), "6Y", "#B2C9AB")
    SEVEN_YEAR = Tenor(timedelta(days=7 * DAYS_IN_A_YEAR), "7Y", "#C6D8FF")
    EIGHT_YEAR = Tenor(timedelta(days=8 * DAYS_IN_A_YEAR), "8Y", "#92B6B1")
    NINE_YEAR = Tenor(timedelta(days=9 * DAYS_IN_A_YEAR), "9Y", "#71A9F7")
    TEN_YEAR = Tenor(timedelta(days=10 * DAYS_IN_A_YEAR), "10Y", "#788AA3")
    ELEVEN_YEAR = Tenor(timedelta(days=11 * DAYS_IN_A_YEAR), "11Y", "#CF995F")
    TWELVE_YEAR = Tenor(timedelta(days=12 * DAYS_IN_A_YEAR), "12Y", "#780116")
    THIRTEEN_YEAR = Tenor(timedelta(days=13 * DAYS_IN_A_YEAR), "13Y", "#7F9C96")
    FOURTEEN_YEAR = Tenor(timedelta(days=14 * DAYS_IN_A_YEAR), "14Y", "#F9C80E")
    FIFTEEN_YEAR = Tenor(timedelta(days=15 * DAYS_IN_A_YEAR), "15Y", "#F86624")
    SIXTEEN_YEAR = Tenor(timedelta(days=16 * DAYS_IN_A_YEAR), "16Y", "#495325")
    SEVENTEEN_YEAR = Tenor(timedelta(days=17 * DAYS_IN_A_YEAR), "17Y", "#AEB88A")
    EIGHTEEN_YEAR = Tenor(timedelta(days=18 * DAYS_IN_A_YEAR), "18Y", "#1D4324")
    NINETEEN_YEAR = Tenor(timedelta(days=19 * DAYS_IN_A_YEAR), "19Y", "#6F9475")
    TWENTY_YEAR = Tenor(timedelta(days=20 * DAYS_IN_A_YEAR), "20Y", "#EA3546")
    TWENTY_ONE_YEAR = Tenor(timedelta(days=21 * DAYS_IN_A_YEAR), "21Y", "#FCAA46")
    TWENTY_TWO_YEAR = Tenor(timedelta(days=22 * DAYS_IN_A_YEAR), "22Y", "#B8ED5C")
    TWENTY_THREE_YEAR = Tenor(timedelta(days=23 * DAYS_IN_A_YEAR), "23Y", "#CAAFD0")
    TWENTY_FOUR_YEAR = Tenor(timedelta(days=24 * DAYS_IN_A_YEAR), "24Y", "#2782A8")
    TWENTY_FIVE_YEAR = Tenor(timedelta(days=25 * DAYS_IN_A_YEAR), "25Y", "#C933F6")
    TWENTY_SIX_YEAR = Tenor(timedelta(days=26 * DAYS_IN_A_YEAR), "26Y", "#7B29FA")
    TWENTY_SEVEN_YEAR = Tenor(timedelta(days=27 * DAYS_IN_A_YEAR), "27Y", "#F68A9A")
    TWENTY_EIGHT_YEAR = Tenor(timedelta(days=28 * DAYS_IN_A_YEAR), "28Y", "#4F10DB")
    TWENTY_NINE_YEAR = Tenor(timedelta(days=29 * DAYS_IN_A_YEAR), "29Y", "#D199B6")
    THIRTY_YEAR = Tenor(timedelta(days=30 * DAYS_IN_A_YEAR), "30Y", "#D2C11A")
    THIRTY_ONE_YEAR = Tenor(timedelta(days=31 * DAYS_IN_A_YEAR), "31Y", "#2A5934")
    THIRTY_TWO_YEAR = Tenor(timedelta(days=32 * DAYS_IN_A_YEAR), "32Y", "#987313")
    THIRTY_THREE_YEAR = Tenor(timedelta(days=33 * DAYS_IN_A_YEAR), "33Y", "#B05C9B")
    THIRTY_FOUR_YEAR = Tenor(timedelta(days=34 * DAYS_IN_A_YEAR), "34Y", "#53418A")
    THIRTY_FIVE_YEAR = Tenor(timedelta(days=35 * DAYS_IN_A_YEAR), "35Y", "#7A06E1")
    THIRTY_SIX_YEAR = Tenor(timedelta(days=36 * DAYS_IN_A_YEAR), "36Y", "#C5312D")
    THIRTY_SEVEN_YEAR = Tenor(timedelta(days=37 * DAYS_IN_A_YEAR), "37Y", "#B89772")
    THIRTY_EIGHT_YEAR = Tenor(timedelta(days=38 * DAYS_IN_A_YEAR), "38Y", "#499791")
    THIRTY_NINE_YEAR = Tenor(timedelta(days=39 * DAYS_IN_A_YEAR), "39Y", "#9CAF24")
    FORTY_YEAR = Tenor(timedelta(days=40 * DAYS_IN_A_YEAR), "40Y", "#6FE546")
    FORTY_ONE_YEAR = Tenor(timedelta(days=41 * DAYS_IN_A_YEAR), "41Y", "#F0123F")
    FORTY_TWO_YEAR = Tenor(timedelta(days=42 * DAYS_IN_A_YEAR), "42Y", "#CB4BAA")
    FORTY_THREE_YEAR = Tenor(timedelta(days=43 * DAYS_IN_A_YEAR), "43Y", "#285306")
    FORTY_FOUR_YEAR = Tenor(timedelta(days=44 * DAYS_IN_A_YEAR), "44Y", "#7C90DB")
    FORTY_FIVE_YEAR = Tenor(timedelta(days=45 * DAYS_IN_A_YEAR), "45Y", "#F396BE")
    FORTY_SIX_YEAR = Tenor(timedelta(days=46 * DAYS_IN_A_YEAR), "46Y", "#905A82")
    FORTY_SEVEN_YEAR = Tenor(timedelta(days=47 * DAYS_IN_A_YEAR), "47Y", "#455217")
    FORTY_EIGHT_YEAR = Tenor(timedelta(days=48 * DAYS_IN_A_YEAR), "48Y", "#2C7326")
    FORTY_NINE_YEAR = Tenor(timedelta(days=49 * DAYS_IN_A_YEAR), "49Y", "#C3F73A")
    FIFTY_YEAR = Tenor(timedelta(days=50 * DAYS_IN_A_YEAR), "50Y", "#226453")
