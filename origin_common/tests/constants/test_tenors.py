import json
from datetime import timedelta
from unittest import TestCase

from origin_common.constants import TENORS
from origin_common.constants.tenors import (
    ONE_MONTH_TIMEDELTA,
    ONE_YEAR_TIMEDELTA,
    THREE_MONTH_TIMEDELTA,
    Tenor,
)
from origin_common.utils import DAYS_IN_A_MONTH, DAYS_IN_A_WEEK, DAYS_IN_A_YEAR


class TestTenorValues(TestCase):
    def test_overnight_value(self):
        assert TENORS.OVERNIGHT.value == timedelta(days=1)

    def test_one_week_value(self):
        assert TENORS.ONE_WEEK.value == timedelta(days=1 * DAYS_IN_A_WEEK)

    def test_two_week_value(self):
        assert TENORS.TWO_WEEK.value == timedelta(days=2 * DAYS_IN_A_WEEK)

    def test_one_month_value(self):
        assert TENORS.ONE_MONTH.value == ONE_MONTH_TIMEDELTA

    def test_two_month_value(self):
        assert TENORS.TWO_MONTH.value == timedelta(days=2 * DAYS_IN_A_MONTH)

    def test_three_month_value(self):
        assert TENORS.THREE_MONTH.value == THREE_MONTH_TIMEDELTA

    def test_four_month_value(self):
        assert TENORS.FOUR_MONTH.value == timedelta(days=4 * DAYS_IN_A_MONTH)

    def test_five_month_value(self):
        assert TENORS.FIVE_MONTH.value == timedelta(days=5 * DAYS_IN_A_MONTH)

    def test_six_month_value(self):
        assert TENORS.SIX_MONTH.value == timedelta(days=6 * DAYS_IN_A_MONTH)

    def test_seven_month_value(self):
        assert TENORS.SEVEN_MONTH.value == timedelta(days=7 * DAYS_IN_A_MONTH)

    def test_eight_month_value(self):
        assert TENORS.EIGHT_MONTH.value == timedelta(days=8 * DAYS_IN_A_MONTH)

    def test_nine_month_value(self):
        assert TENORS.NINE_MONTH.value == timedelta(days=9 * DAYS_IN_A_MONTH)

    def test_ten_month_value(self):
        assert TENORS.TEN_MONTH.value == timedelta(days=10 * DAYS_IN_A_MONTH)

    def test_eleven_month_value(self):
        assert TENORS.ELEVEN_MONTH.value == timedelta(days=11 * DAYS_IN_A_MONTH)

    def test_one_year_value(self):
        assert TENORS.ONE_YEAR.value == ONE_YEAR_TIMEDELTA

    def test_one_and_half_year_value(self):
        assert TENORS.ONE_AND_HALF_YEAR.value == timedelta(days=18 * DAYS_IN_A_MONTH)

    def test_two_year_value(self):
        assert TENORS.TWO_YEAR.value == timedelta(days=2 * DAYS_IN_A_YEAR)

    def test_three_year_value(self):
        assert TENORS.THREE_YEAR.value == timedelta(days=3 * DAYS_IN_A_YEAR)

    def test_four_year_value(self):
        assert TENORS.FOUR_YEAR.value == timedelta(days=4 * DAYS_IN_A_YEAR)

    def test_five_year_value(self):
        assert TENORS.FIVE_YEAR.value == timedelta(days=5 * DAYS_IN_A_YEAR)

    def test_six_year_value(self):
        assert TENORS.SIX_YEAR.value == timedelta(days=6 * DAYS_IN_A_YEAR)

    def test_seven_year_value(self):
        assert TENORS.SEVEN_YEAR.value == timedelta(days=7 * DAYS_IN_A_YEAR)

    def test_eight_year_value(self):
        assert TENORS.EIGHT_YEAR.value == timedelta(days=8 * DAYS_IN_A_YEAR)

    def test_nine_year_value(self):
        assert TENORS.NINE_YEAR.value == timedelta(days=9 * DAYS_IN_A_YEAR)

    def test_ten_year_value(self):
        assert TENORS.TEN_YEAR.value == timedelta(days=10 * DAYS_IN_A_YEAR)

    def test_eleven_year_value(self):
        assert TENORS.ELEVEN_YEAR.value == timedelta(days=11 * DAYS_IN_A_YEAR)

    def test_twelve_year_value(self):
        assert TENORS.TWELVE_YEAR.value == timedelta(days=12 * DAYS_IN_A_YEAR)

    def test_thirteen_year_value(self):
        assert TENORS.THIRTEEN_YEAR.value == timedelta(days=13 * DAYS_IN_A_YEAR)

    def test_fourteen_year_value(self):
        assert TENORS.FOURTEEN_YEAR.value == timedelta(days=14 * DAYS_IN_A_YEAR)

    def test_fifteen_year_value(self):
        assert TENORS.FIFTEEN_YEAR.value == timedelta(days=15 * DAYS_IN_A_YEAR)

    def test_sixteen_year_value(self):
        assert TENORS.SIXTEEN_YEAR.value == timedelta(days=16 * DAYS_IN_A_YEAR)

    def test_seventeen_year_value(self):
        assert TENORS.SEVENTEEN_YEAR.value == timedelta(days=17 * DAYS_IN_A_YEAR)

    def test_eighteen_year_value(self):
        assert TENORS.EIGHTEEN_YEAR.value == timedelta(days=18 * DAYS_IN_A_YEAR)

    def test_nineteen_year_value(self):
        assert TENORS.NINETEEN_YEAR.value == timedelta(days=19 * DAYS_IN_A_YEAR)

    def test_twenty_year_value(self):
        assert TENORS.TWENTY_YEAR.value == timedelta(days=20 * DAYS_IN_A_YEAR)

    def test_twenty_one_year_value(self):
        assert TENORS.TWENTY_ONE_YEAR.value == timedelta(days=21 * DAYS_IN_A_YEAR)

    def test_twenty_two_year_value(self):
        assert TENORS.TWENTY_TWO_YEAR.value == timedelta(days=22 * DAYS_IN_A_YEAR)

    def test_twenty_three_year_value(self):
        assert TENORS.TWENTY_THREE_YEAR.value == timedelta(days=23 * DAYS_IN_A_YEAR)

    def test_twenty_four_year_value(self):
        assert TENORS.TWENTY_FOUR_YEAR.value == timedelta(days=24 * DAYS_IN_A_YEAR)

    def test_twenty_five_year_value(self):
        assert TENORS.TWENTY_FIVE_YEAR.value == timedelta(days=25 * DAYS_IN_A_YEAR)

    def test_twenty_six_year_value(self):
        assert TENORS.TWENTY_SIX_YEAR.value == timedelta(days=26 * DAYS_IN_A_YEAR)

    def test_twenty_seven_year_value(self):
        assert TENORS.TWENTY_SEVEN_YEAR.value == timedelta(days=27 * DAYS_IN_A_YEAR)

    def test_twenty_eight_year_value(self):
        assert TENORS.TWENTY_EIGHT_YEAR.value == timedelta(days=28 * DAYS_IN_A_YEAR)

    def test_twenty_nine_year_value(self):
        assert TENORS.TWENTY_NINE_YEAR.value == timedelta(days=29 * DAYS_IN_A_YEAR)

    def test_thirty_year_value(self):
        assert TENORS.THIRTY_YEAR.value == timedelta(days=30 * DAYS_IN_A_YEAR)

    def test_thirty_one_year_value(self):
        assert TENORS.THIRTY_ONE_YEAR.value == timedelta(days=31 * DAYS_IN_A_YEAR)

    def test_thirty_two_year_value(self):
        assert TENORS.THIRTY_TWO_YEAR.value == timedelta(days=32 * DAYS_IN_A_YEAR)

    def test_thirty_three_year_value(self):
        assert TENORS.THIRTY_THREE_YEAR.value == timedelta(days=33 * DAYS_IN_A_YEAR)

    def test_thirty_four_year_value(self):
        assert TENORS.THIRTY_FOUR_YEAR.value == timedelta(days=34 * DAYS_IN_A_YEAR)

    def test_thirty_five_year_value(self):
        assert TENORS.THIRTY_FIVE_YEAR.value == timedelta(days=35 * DAYS_IN_A_YEAR)

    def test_thirty_six_year_value(self):
        assert TENORS.THIRTY_SIX_YEAR.value == timedelta(days=36 * DAYS_IN_A_YEAR)

    def test_thirty_seven_year_value(self):
        assert TENORS.THIRTY_SEVEN_YEAR.value == timedelta(days=37 * DAYS_IN_A_YEAR)

    def test_thirty_eight_year_value(self):
        assert TENORS.THIRTY_EIGHT_YEAR.value == timedelta(days=38 * DAYS_IN_A_YEAR)

    def test_thirty_nine_year_value(self):
        assert TENORS.THIRTY_NINE_YEAR.value == timedelta(days=39 * DAYS_IN_A_YEAR)

    def test_forty_year_value(self):
        assert TENORS.FORTY_YEAR.value == timedelta(days=40 * DAYS_IN_A_YEAR)

    def test_forty_one_year_value(self):
        assert TENORS.FORTY_ONE_YEAR.value == timedelta(days=41 * DAYS_IN_A_YEAR)

    def test_forty_two_year_value(self):
        assert TENORS.FORTY_TWO_YEAR.value == timedelta(days=42 * DAYS_IN_A_YEAR)

    def test_forty_three_year_value(self):
        assert TENORS.FORTY_THREE_YEAR.value == timedelta(days=43 * DAYS_IN_A_YEAR)

    def test_forty_four_year_value(self):
        assert TENORS.FORTY_FOUR_YEAR.value == timedelta(days=44 * DAYS_IN_A_YEAR)

    def test_forty_five_year_value(self):
        assert TENORS.FORTY_FIVE_YEAR.value == timedelta(days=45 * DAYS_IN_A_YEAR)

    def test_forty_six_year_value(self):
        assert TENORS.FORTY_SIX_YEAR.value == timedelta(days=46 * DAYS_IN_A_YEAR)

    def test_forty_seven_year_value(self):
        assert TENORS.FORTY_SEVEN_YEAR.value == timedelta(days=47 * DAYS_IN_A_YEAR)

    def test_forty_eight_year_value(self):
        assert TENORS.FORTY_EIGHT_YEAR.value == timedelta(days=48 * DAYS_IN_A_YEAR)

    def test_forty_nine_year_value(self):
        assert TENORS.FORTY_NINE_YEAR.value == timedelta(days=49 * DAYS_IN_A_YEAR)

    def test_fifty_year_value(self):
        assert TENORS.FIFTY_YEAR.value == timedelta(days=50 * DAYS_IN_A_YEAR)


class TestTenorLabels(TestCase):
    def test_overnight_label(self):
        assert TENORS.OVERNIGHT.label == "O/N"

    def test_one_week_label(self):
        assert TENORS.ONE_WEEK.label == "1W"

    def test_two_week_label(self):
        assert TENORS.TWO_WEEK.label == "2W"

    def test_one_month_label(self):
        assert TENORS.ONE_MONTH.label == "1M"

    def test_two_month_label(self):
        assert TENORS.TWO_MONTH.label == "2M"

    def test_three_month_label(self):
        assert TENORS.THREE_MONTH.label == "3M"

    def test_four_month_label(self):
        assert TENORS.FOUR_MONTH.label == "4M"

    def test_five_month_label(self):
        assert TENORS.FIVE_MONTH.label == "5M"

    def test_six_month_label(self):
        assert TENORS.SIX_MONTH.label == "6M"

    def test_seven_month_label(self):
        assert TENORS.SEVEN_MONTH.label == "7M"

    def test_eight_month_label(self):
        assert TENORS.EIGHT_MONTH.label == "8M"

    def test_nine_month_label(self):
        assert TENORS.NINE_MONTH.label == "9M"

    def test_ten_month_label(self):
        assert TENORS.TEN_MONTH.label == "10M"

    def test_eleven_month_label(self):
        assert TENORS.ELEVEN_MONTH.label == "11M"

    def test_one_year_label(self):
        assert TENORS.ONE_YEAR.label == "1Y"

    def test_one_and_half_year_label(self):
        assert TENORS.ONE_AND_HALF_YEAR.label == "1.5Y"

    def test_two_year_label(self):
        assert TENORS.TWO_YEAR.label == "2Y"

    def test_three_year_label(self):
        assert TENORS.THREE_YEAR.label == "3Y"

    def test_four_year_label(self):
        assert TENORS.FOUR_YEAR.label == "4Y"

    def test_five_year_label(self):
        assert TENORS.FIVE_YEAR.label == "5Y"

    def test_six_year_label(self):
        assert TENORS.SIX_YEAR.label == "6Y"

    def test_seven_year_label(self):
        assert TENORS.SEVEN_YEAR.label == "7Y"

    def test_eight_year_label(self):
        assert TENORS.EIGHT_YEAR.label == "8Y"

    def test_nine_year_label(self):
        assert TENORS.NINE_YEAR.label == "9Y"

    def test_ten_year_label(self):
        assert TENORS.TEN_YEAR.label == "10Y"

    def test_eleven_year_label(self):
        assert TENORS.ELEVEN_YEAR.label == "11Y"

    def test_twelve_year_label(self):
        assert TENORS.TWELVE_YEAR.label == "12Y"

    def test_thirteen_year_label(self):
        assert TENORS.THIRTEEN_YEAR.label == "13Y"

    def test_fourteen_year_label(self):
        assert TENORS.FOURTEEN_YEAR.label == "14Y"

    def test_fifteen_year_label(self):
        assert TENORS.FIFTEEN_YEAR.label == "15Y"

    def test_sixteen_year_label(self):
        assert TENORS.SIXTEEN_YEAR.label == "16Y"

    def test_seventeen_year_label(self):
        assert TENORS.SEVENTEEN_YEAR.label == "17Y"

    def test_eighteen_year_label(self):
        assert TENORS.EIGHTEEN_YEAR.label == "18Y"

    def test_nineteen_year_label(self):
        assert TENORS.NINETEEN_YEAR.label == "19Y"

    def test_twenty_year_label(self):
        assert TENORS.TWENTY_YEAR.label == "20Y"

    def test_twenty_one_year_label(self):
        assert TENORS.TWENTY_ONE_YEAR.label == "21Y"

    def test_twenty_two_year_label(self):
        assert TENORS.TWENTY_TWO_YEAR.label == "22Y"

    def test_twenty_three_year_label(self):
        assert TENORS.TWENTY_THREE_YEAR.label == "23Y"

    def test_twenty_four_year_label(self):
        assert TENORS.TWENTY_FOUR_YEAR.label == "24Y"

    def test_twenty_five_year_label(self):
        assert TENORS.TWENTY_FIVE_YEAR.label == "25Y"

    def test_twenty_six_year_label(self):
        assert TENORS.TWENTY_SIX_YEAR.label == "26Y"

    def test_twenty_seven_year_label(self):
        assert TENORS.TWENTY_SEVEN_YEAR.label == "27Y"

    def test_twenty_eight_year_label(self):
        assert TENORS.TWENTY_EIGHT_YEAR.label == "28Y"

    def test_twenty_nine_year_label(self):
        assert TENORS.TWENTY_NINE_YEAR.label == "29Y"

    def test_thirty_year_label(self):
        assert TENORS.THIRTY_YEAR.label == "30Y"

    def test_thirty_one_year_label(self):
        assert TENORS.THIRTY_ONE_YEAR.label == "31Y"

    def test_thirty_two_year_label(self):
        assert TENORS.THIRTY_TWO_YEAR.label == "32Y"

    def test_thirty_three_year_label(self):
        assert TENORS.THIRTY_THREE_YEAR.label == "33Y"

    def test_thirty_four_year_label(self):
        assert TENORS.THIRTY_FOUR_YEAR.label == "34Y"

    def test_thirty_five_year_label(self):
        assert TENORS.THIRTY_FIVE_YEAR.label == "35Y"

    def test_thirty_six_year_label(self):
        assert TENORS.THIRTY_SIX_YEAR.label == "36Y"

    def test_thirty_seven_year_label(self):
        assert TENORS.THIRTY_SEVEN_YEAR.label == "37Y"

    def test_thirty_eight_year_label(self):
        assert TENORS.THIRTY_EIGHT_YEAR.label == "38Y"

    def test_thirty_nine_year_label(self):
        assert TENORS.THIRTY_NINE_YEAR.label == "39Y"

    def test_forty_year_label(self):
        assert TENORS.FORTY_YEAR.label == "40Y"

    def test_forty_one_year_label(self):
        assert TENORS.FORTY_ONE_YEAR.label == "41Y"

    def test_forty_two_year_label(self):
        assert TENORS.FORTY_TWO_YEAR.label == "42Y"

    def test_forty_three_year_label(self):
        assert TENORS.FORTY_THREE_YEAR.label == "43Y"

    def test_forty_four_year_label(self):
        assert TENORS.FORTY_FOUR_YEAR.label == "44Y"

    def test_forty_five_year_label(self):
        assert TENORS.FORTY_FIVE_YEAR.label == "45Y"

    def test_forty_six_year_label(self):
        assert TENORS.FORTY_SIX_YEAR.label == "46Y"

    def test_forty_seven_year_label(self):
        assert TENORS.FORTY_SEVEN_YEAR.label == "47Y"

    def test_forty_eight_year_label(self):
        assert TENORS.FORTY_EIGHT_YEAR.label == "48Y"

    def test_forty_nine_year_label(self):
        assert TENORS.FORTY_NINE_YEAR.label == "49Y"

    def test_fifty_year_label(self):
        assert TENORS.FIFTY_YEAR.label == "50Y"


class TestTenorColorCodes(TestCase):
    def test_overnight_color_code(self):
        assert TENORS.OVERNIGHT.color_code == "#665241"

    def test_one_week_color_code(self):
        assert TENORS.ONE_WEEK.color_code == "#C1B591"

    def test_two_week_color_code(self):
        assert TENORS.TWO_WEEK.color_code == "#426B94"

    def test_one_month_color_code(self):
        assert TENORS.ONE_MONTH.color_code == "#426B94"

    def test_two_month_color_code(self):
        assert TENORS.TWO_MONTH.color_code == "#C4A77D"

    def test_three_month_color_code(self):
        assert TENORS.THREE_MONTH.color_code == "#FF6666"

    def test_four_month_color_code(self):
        assert TENORS.FOUR_MONTH.color_code == "#F9613C"

    def test_five_month_color_code(self):
        assert TENORS.FIVE_MONTH.color_code == "#F3DFC1"

    def test_six_month_color_code(self):
        assert TENORS.SIX_MONTH.color_code == "#856A5D"

    def test_seven_month_color_code(self):
        assert TENORS.SEVEN_MONTH.color_code == "#1B3022"

    def test_eight_month_color_code(self):
        assert TENORS.EIGHT_MONTH.color_code == "#395756"

    def test_nine_month_color_code(self):
        assert TENORS.NINE_MONTH.color_code == "#FFB30F"

    def test_ten_month_color_code(self):
        assert TENORS.TEN_MONTH.color_code == "#01295F"

    def test_eleven_month_color_code(self):
        assert TENORS.ELEVEN_MONTH.color_code == "#849324"

    def test_one_year_color_code(self):
        assert TENORS.ONE_YEAR.color_code == "#204B57"

    def test_one_and_half_year_color_code(self):
        assert TENORS.ONE_AND_HALF_YEAR.color_code == "#8A716A"

    def test_two_year_color_code(self):
        assert TENORS.TWO_YEAR.color_code == "#EF946C"

    def test_three_year_color_code(self):
        assert TENORS.THREE_YEAR.color_code == "#45C7A6"

    def test_four_year_color_code(self):
        assert TENORS.FOUR_YEAR.color_code == "#2F2963"

    def test_five_year_color_code(self):
        assert TENORS.FIVE_YEAR.color_code == "#3A435E"

    def test_six_year_color_code(self):
        assert TENORS.SIX_YEAR.color_code == "#B2C9AB"

    def test_seven_year_color_code(self):
        assert TENORS.SEVEN_YEAR.color_code == "#C6D8FF"

    def test_eight_year_color_code(self):
        assert TENORS.EIGHT_YEAR.color_code == "#92B6B1"

    def test_nine_year_color_code(self):
        assert TENORS.NINE_YEAR.color_code == "#71A9F7"

    def test_ten_year_color_code(self):
        assert TENORS.TEN_YEAR.color_code == "#788AA3"

    def test_eleven_year_color_code(self):
        assert TENORS.ELEVEN_YEAR.color_code == "#CF995F"

    def test_twelve_year_color_code(self):
        assert TENORS.TWELVE_YEAR.color_code == "#780116"

    def test_thirteen_year_color_code(self):
        assert TENORS.THIRTEEN_YEAR.color_code == "#7F9C96"

    def test_fourteen_year_color_code(self):
        assert TENORS.FOURTEEN_YEAR.color_code == "#F9C80E"

    def test_fifteen_year_color_code(self):
        assert TENORS.FIFTEEN_YEAR.color_code == "#F86624"

    def test_sixteen_year_color_code(self):
        assert TENORS.SIXTEEN_YEAR.color_code == "#495325"

    def test_seventeen_year_color_code(self):
        assert TENORS.SEVENTEEN_YEAR.color_code == "#AEB88A"

    def test_eighteen_year_color_code(self):
        assert TENORS.EIGHTEEN_YEAR.color_code == "#1D4324"

    def test_nineteen_year_color_code(self):
        assert TENORS.NINETEEN_YEAR.color_code == "#6F9475"

    def test_twenty_year_color_code(self):
        assert TENORS.TWENTY_YEAR.color_code == "#EA3546"

    def test_twenty_one_year_color_code(self):
        assert TENORS.TWENTY_ONE_YEAR.color_code == "#FCAA46"

    def test_twenty_two_year_color_code(self):
        assert TENORS.TWENTY_TWO_YEAR.color_code == "#B8ED5C"

    def test_twenty_three_year_color_code(self):
        assert TENORS.TWENTY_THREE_YEAR.color_code == "#CAAFD0"

    def test_twenty_four_year_color_code(self):
        assert TENORS.TWENTY_FOUR_YEAR.color_code == "#2782A8"

    def test_twenty_five_year_color_code(self):
        assert TENORS.TWENTY_FIVE_YEAR.color_code == "#C933F6"

    def test_twenty_six_year_color_code(self):
        assert TENORS.TWENTY_SIX_YEAR.color_code == "#7B29FA"

    def test_twenty_seven_year_color_code(self):
        assert TENORS.TWENTY_SEVEN_YEAR.color_code == "#F68A9A"

    def test_twenty_eight_year_color_code(self):
        assert TENORS.TWENTY_EIGHT_YEAR.color_code == "#4F10DB"

    def test_twenty_nine_year_color_code(self):
        assert TENORS.TWENTY_NINE_YEAR.color_code == "#D199B6"

    def test_thirty_year_color_code(self):
        assert TENORS.THIRTY_YEAR.color_code == "#D2C11A"

    def test_thirty_one_year_color_code(self):
        assert TENORS.THIRTY_ONE_YEAR.color_code == "#2A5934"

    def test_thirty_two_year_color_code(self):
        assert TENORS.THIRTY_TWO_YEAR.color_code == "#987313"

    def test_thirty_three_year_color_code(self):
        assert TENORS.THIRTY_THREE_YEAR.color_code == "#B05C9B"

    def test_thirty_four_year_color_code(self):
        assert TENORS.THIRTY_FOUR_YEAR.color_code == "#53418A"

    def test_thirty_five_year_color_code(self):
        assert TENORS.THIRTY_FIVE_YEAR.color_code == "#7A06E1"

    def test_thirty_six_year_color_code(self):
        assert TENORS.THIRTY_SIX_YEAR.color_code == "#C5312D"

    def test_thirty_seven_year_color_code(self):
        assert TENORS.THIRTY_SEVEN_YEAR.color_code == "#B89772"

    def test_thirty_eight_year_color_code(self):
        assert TENORS.THIRTY_EIGHT_YEAR.color_code == "#499791"

    def test_thirty_nine_year_color_code(self):
        assert TENORS.THIRTY_NINE_YEAR.color_code == "#9CAF24"

    def test_forty_year_color_code(self):
        assert TENORS.FORTY_YEAR.color_code == "#6FE546"

    def test_forty_one_year_color_code(self):
        assert TENORS.FORTY_ONE_YEAR.color_code == "#F0123F"

    def test_forty_two_year_color_code(self):
        assert TENORS.FORTY_TWO_YEAR.color_code == "#CB4BAA"

    def test_forty_three_year_color_code(self):
        assert TENORS.FORTY_THREE_YEAR.color_code == "#285306"

    def test_forty_four_year_color_code(self):
        assert TENORS.FORTY_FOUR_YEAR.color_code == "#7C90DB"

    def test_forty_five_year_color_code(self):
        assert TENORS.FORTY_FIVE_YEAR.color_code == "#F396BE"

    def test_forty_six_year_color_code(self):
        assert TENORS.FORTY_SIX_YEAR.color_code == "#905A82"

    def test_forty_seven_year_color_code(self):
        assert TENORS.FORTY_SEVEN_YEAR.color_code == "#455217"

    def test_forty_eight_year_color_code(self):
        assert TENORS.FORTY_EIGHT_YEAR.color_code == "#2C7326"

    def test_forty_nine_year_color_code(self):
        assert TENORS.FORTY_NINE_YEAR.color_code == "#C3F73A"

    def test_fifty_year_color_code(self):
        assert TENORS.FIFTY_YEAR.color_code == "#226453"


class TestTenorNumberOfMonths(TestCase):
    def test_overnight_number_of_months(self):
        assert TENORS.OVERNIGHT.number_of_months == 1 / DAYS_IN_A_MONTH

    def test_one_week_number_of_months(self):
        assert TENORS.ONE_WEEK.number_of_months == DAYS_IN_A_WEEK / DAYS_IN_A_MONTH

    def test_two_week_number_of_months(self):
        assert TENORS.TWO_WEEK.number_of_months == 2 * DAYS_IN_A_WEEK / DAYS_IN_A_MONTH

    def test_one_month_number_of_months(self):
        assert TENORS.ONE_MONTH.number_of_months == 1

    def test_two_month_number_of_months(self):
        assert TENORS.TWO_MONTH.number_of_months == 2

    def test_three_month_number_of_months(self):
        assert TENORS.THREE_MONTH.number_of_months == 3

    def test_four_month_number_of_months(self):
        assert TENORS.FOUR_MONTH.number_of_months == 4

    def test_five_month_number_of_months(self):
        assert TENORS.FIVE_MONTH.number_of_months == 5

    def test_six_month_number_of_months(self):
        assert TENORS.SIX_MONTH.number_of_months == 6

    def test_seven_month_number_of_months(self):
        assert TENORS.SEVEN_MONTH.number_of_months == 7

    def test_eight_month_number_of_months(self):
        assert TENORS.EIGHT_MONTH.number_of_months == 8

    def test_nine_month_number_of_months(self):
        assert TENORS.NINE_MONTH.number_of_months == 9

    def test_ten_month_number_of_months(self):
        assert TENORS.TEN_MONTH.number_of_months == 10

    def test_eleven_month_number_of_months(self):
        assert TENORS.ELEVEN_MONTH.number_of_months == 11

    def test_one_year_number_of_months(self):
        assert TENORS.ONE_YEAR.number_of_months == 12

    def test_one_and_half_year_number_of_months(self):
        assert TENORS.ONE_AND_HALF_YEAR.number_of_months == 18

    def test_two_year_number_of_months(self):
        assert TENORS.TWO_YEAR.number_of_months == 2 * 12

    def test_three_year_number_of_months(self):
        assert TENORS.THREE_YEAR.number_of_months == 3 * 12

    def test_four_year_number_of_months(self):
        assert TENORS.FOUR_YEAR.number_of_months == 4 * 12

    def test_five_year_number_of_months(self):
        assert TENORS.FIVE_YEAR.number_of_months == 5 * 12

    def test_six_year_number_of_months(self):
        assert TENORS.SIX_YEAR.number_of_months == 6 * 12

    def test_seven_year_number_of_months(self):
        assert TENORS.SEVEN_YEAR.number_of_months == 7 * 12

    def test_eight_year_number_of_months(self):
        assert TENORS.EIGHT_YEAR.number_of_months == 8 * 12

    def test_nine_year_number_of_months(self):
        assert TENORS.NINE_YEAR.number_of_months == 9 * 12

    def test_ten_year_number_of_months(self):
        assert TENORS.TEN_YEAR.number_of_months == 10 * 12

    def test_eleven_year_number_of_months(self):
        assert TENORS.ELEVEN_YEAR.number_of_months == 11 * 12

    def test_twelve_year_number_of_months(self):
        assert TENORS.TWELVE_YEAR.number_of_months == 12 * 12

    def test_thirteen_year_number_of_months(self):
        assert TENORS.THIRTEEN_YEAR.number_of_months == 13 * 12

    def test_fourteen_year_number_of_months(self):
        assert TENORS.FOURTEEN_YEAR.number_of_months == 14 * 12

    def test_fifteen_year_number_of_months(self):
        assert TENORS.FIFTEEN_YEAR.number_of_months == 15 * 12

    def test_sixteen_year_number_of_months(self):
        assert TENORS.SIXTEEN_YEAR.number_of_months == 16 * 12

    def test_seventeen_year_number_of_months(self):
        assert TENORS.SEVENTEEN_YEAR.number_of_months == 17 * 12

    def test_eighteen_year_number_of_months(self):
        assert TENORS.EIGHTEEN_YEAR.number_of_months == 18 * 12

    def test_nineteen_year_number_of_months(self):
        assert TENORS.NINETEEN_YEAR.number_of_months == 19 * 12

    def test_twenty_year_number_of_months(self):
        assert TENORS.TWENTY_YEAR.number_of_months == 20 * 12

    def test_twenty_one_year_number_of_months(self):
        assert TENORS.TWENTY_ONE_YEAR.number_of_months == 21 * 12

    def test_twenty_two_year_number_of_months(self):
        assert TENORS.TWENTY_TWO_YEAR.number_of_months == 22 * 12

    def test_twenty_three_year_number_of_months(self):
        assert TENORS.TWENTY_THREE_YEAR.number_of_months == 23 * 12

    def test_twenty_four_year_number_of_months(self):
        assert TENORS.TWENTY_FOUR_YEAR.number_of_months == 24 * 12

    def test_twenty_five_year_number_of_months(self):
        assert TENORS.TWENTY_FIVE_YEAR.number_of_months == 25 * 12

    def test_twenty_six_year_number_of_months(self):
        assert TENORS.TWENTY_SIX_YEAR.number_of_months == 26 * 12

    def test_twenty_seven_year_number_of_months(self):
        assert TENORS.TWENTY_SEVEN_YEAR.number_of_months == 27 * 12

    def test_twenty_eight_year_number_of_months(self):
        assert TENORS.TWENTY_EIGHT_YEAR.number_of_months == 28 * 12

    def test_twenty_nine_year_number_of_months(self):
        assert TENORS.TWENTY_NINE_YEAR.number_of_months == 29 * 12

    def test_thirty_year_number_of_months(self):
        assert TENORS.THIRTY_YEAR.number_of_months == 30 * 12

    def test_thirty_one_year_number_of_months(self):
        assert TENORS.THIRTY_ONE_YEAR.number_of_months == 31 * 12

    def test_thirty_two_year_number_of_months(self):
        assert TENORS.THIRTY_TWO_YEAR.number_of_months == 32 * 12

    def test_thirty_three_year_number_of_months(self):
        assert TENORS.THIRTY_THREE_YEAR.number_of_months == 33 * 12

    def test_thirty_four_year_number_of_months(self):
        assert TENORS.THIRTY_FOUR_YEAR.number_of_months == 34 * 12

    def test_thirty_five_year_number_of_months(self):
        assert TENORS.THIRTY_FIVE_YEAR.number_of_months == 35 * 12

    def test_thirty_six_year_number_of_months(self):
        assert TENORS.THIRTY_SIX_YEAR.number_of_months == 36 * 12

    def test_thirty_seven_year_number_of_months(self):
        assert TENORS.THIRTY_SEVEN_YEAR.number_of_months == 37 * 12

    def test_thirty_eight_year_number_of_months(self):
        assert TENORS.THIRTY_EIGHT_YEAR.number_of_months == 38 * 12

    def test_thirty_nine_year_number_of_months(self):
        assert TENORS.THIRTY_NINE_YEAR.number_of_months == 39 * 12

    def test_forty_year_number_of_months(self):
        assert TENORS.FORTY_YEAR.number_of_months == 40 * 12

    def test_forty_one_year_number_of_months(self):
        assert TENORS.FORTY_ONE_YEAR.number_of_months == 41 * 12

    def test_forty_two_year_number_of_months(self):
        assert TENORS.FORTY_TWO_YEAR.number_of_months == 42 * 12

    def test_forty_three_year_number_of_months(self):
        assert TENORS.FORTY_THREE_YEAR.number_of_months == 43 * 12

    def test_forty_four_year_number_of_months(self):
        assert TENORS.FORTY_FOUR_YEAR.number_of_months == 44 * 12

    def test_forty_five_year_number_of_months(self):
        assert TENORS.FORTY_FIVE_YEAR.number_of_months == 45 * 12

    def test_forty_six_year_number_of_months(self):
        assert TENORS.FORTY_SIX_YEAR.number_of_months == 46 * 12

    def test_forty_seven_year_number_of_months(self):
        assert TENORS.FORTY_SEVEN_YEAR.number_of_months == 47 * 12

    def test_forty_eight_year_number_of_months(self):
        assert TENORS.FORTY_EIGHT_YEAR.number_of_months == 48 * 12

    def test_forty_nine_year_number_of_months(self):
        assert TENORS.FORTY_NINE_YEAR.number_of_months == 49 * 12

    def test_fifty_year_number_of_months(self):
        assert TENORS.FIFTY_YEAR.number_of_months == 50 * 12

    def test_invalid_tenor(self):
        with self.assertRaises(ValueError):
            Tenor(timedelta(1), "1D", "red")


class TestTenorIsCallableTenor(TestCase):
    def test_overnight_is_not_callable_tenor(self):
        assert TENORS.OVERNIGHT.is_callable_tenor is False

    def test_one_week_is_not_callable_tenor(self):
        assert TENORS.ONE_WEEK.is_callable_tenor is False

    def test_two_week_is_not_callable_tenor(self):
        assert TENORS.TWO_WEEK.is_callable_tenor is False

    def test_one_month_is_callable_tenor(self):
        assert TENORS.ONE_MONTH.is_callable_tenor is True

    def test_two_month_is_not_callable_tenor(self):
        assert TENORS.TWO_MONTH.is_callable_tenor is False

    def test_three_month_is_callable_tenor(self):
        assert TENORS.THREE_MONTH.is_callable_tenor is True

    def test_four_month_is_not_callable_tenor(self):
        assert TENORS.FOUR_MONTH.is_callable_tenor is False

    def test_five_month_is_not_callable_tenor(self):
        assert TENORS.FIVE_MONTH.is_callable_tenor is False

    def test_six_month_is_callable_tenor(self):
        assert TENORS.SIX_MONTH.is_callable_tenor is True

    def test_seven_month_is_not_callable_tenor(self):
        assert TENORS.SEVEN_MONTH.is_callable_tenor is False

    def test_eight_month_is_not_callable_tenor(self):
        assert TENORS.EIGHT_MONTH.is_callable_tenor is False

    def test_nine_month_is_callable_tenor(self):
        assert TENORS.NINE_MONTH.is_callable_tenor is True

    def test_ten_month_is_not_callable_tenor(self):
        assert TENORS.TEN_MONTH.is_callable_tenor is False

    def test_eleven_month_is_not_callable_tenor(self):
        assert TENORS.ELEVEN_MONTH.is_callable_tenor is False

    def test_one_year_is_callable_tenor(self):
        assert TENORS.ONE_YEAR.is_callable_tenor is True

    def test_one_and_half_year_is_callable_tenor(self):
        assert TENORS.ONE_AND_HALF_YEAR.is_callable_tenor is True

    def test_two_year_is_callable_tenor(self):
        assert TENORS.TWO_YEAR.is_callable_tenor is True

    def test_three_year_is_callable_tenor(self):
        assert TENORS.THREE_YEAR.is_callable_tenor is True

    def test_four_year_is_callable_tenor(self):
        assert TENORS.FOUR_YEAR.is_callable_tenor is True

    def test_five_year_is_callable_tenor(self):
        assert TENORS.FIVE_YEAR.is_callable_tenor is True

    def test_six_year_is_callable_tenor(self):
        assert TENORS.SIX_YEAR.is_callable_tenor is True

    def test_seven_year_is_callable_tenor(self):
        assert TENORS.SEVEN_YEAR.is_callable_tenor is True

    def test_eight_year_is_callable_tenor(self):
        assert TENORS.EIGHT_YEAR.is_callable_tenor is True

    def test_nine_year_is_callable_tenor(self):
        assert TENORS.NINE_YEAR.is_callable_tenor is True

    def test_ten_year_is_callable_tenor(self):
        assert TENORS.TEN_YEAR.is_callable_tenor is True

    def test_eleven_year_is_callable_tenor(self):
        assert TENORS.ELEVEN_YEAR.is_callable_tenor is True

    def test_twelve_year_is_callable_tenor(self):
        assert TENORS.TWELVE_YEAR.is_callable_tenor is True

    def test_thirteen_year_is_callable_tenor(self):
        assert TENORS.THIRTEEN_YEAR.is_callable_tenor is True

    def test_fourteen_year_is_callable_tenor(self):
        assert TENORS.FOURTEEN_YEAR.is_callable_tenor is True

    def test_fifteen_year_is_callable_tenor(self):
        assert TENORS.FIFTEEN_YEAR.is_callable_tenor is True

    def test_sixteen_year_is_callable_tenor(self):
        assert TENORS.SIXTEEN_YEAR.is_callable_tenor is True

    def test_seventeen_year_is_callable_tenor(self):
        assert TENORS.SEVENTEEN_YEAR.is_callable_tenor is True

    def test_eighteen_year_is_callable_tenor(self):
        assert TENORS.EIGHTEEN_YEAR.is_callable_tenor is True

    def test_nineteen_year_is_callable_tenor(self):
        assert TENORS.NINETEEN_YEAR.is_callable_tenor is True

    def test_twenty_year_is_callable_tenor(self):
        assert TENORS.TWENTY_YEAR.is_callable_tenor is True

    def test_twenty_one_year_is_callable_tenor(self):
        assert TENORS.TWENTY_ONE_YEAR.is_callable_tenor is True

    def test_twenty_two_year_is_callable_tenor(self):
        assert TENORS.TWENTY_TWO_YEAR.is_callable_tenor is True

    def test_twenty_three_year_is_callable_tenor(self):
        assert TENORS.TWENTY_THREE_YEAR.is_callable_tenor is True

    def test_twenty_four_year_is_callable_tenor(self):
        assert TENORS.TWENTY_FOUR_YEAR.is_callable_tenor is True

    def test_twenty_five_year_is_callable_tenor(self):
        assert TENORS.TWENTY_FIVE_YEAR.is_callable_tenor is True

    def test_twenty_six_year_is_callable_tenor(self):
        assert TENORS.TWENTY_SIX_YEAR.is_callable_tenor is True

    def test_twenty_seven_year_is_callable_tenor(self):
        assert TENORS.TWENTY_SEVEN_YEAR.is_callable_tenor is True

    def test_twenty_eight_year_is_callable_tenor(self):
        assert TENORS.TWENTY_EIGHT_YEAR.is_callable_tenor is True

    def test_twenty_nine_year_is_callable_tenor(self):
        assert TENORS.TWENTY_NINE_YEAR.is_callable_tenor is True

    def test_thirty_year_is_callable_tenor(self):
        assert TENORS.THIRTY_YEAR.is_callable_tenor is True

    def test_thirty_one_year_is_callable_tenor(self):
        assert TENORS.THIRTY_ONE_YEAR.is_callable_tenor is True

    def test_thirty_two_year_is_callable_tenor(self):
        assert TENORS.THIRTY_TWO_YEAR.is_callable_tenor is True

    def test_thirty_three_year_is_callable_tenor(self):
        assert TENORS.THIRTY_THREE_YEAR.is_callable_tenor is True

    def test_thirty_four_year_is_callable_tenor(self):
        assert TENORS.THIRTY_FOUR_YEAR.is_callable_tenor is True

    def test_thirty_five_year_is_callable_tenor(self):
        assert TENORS.THIRTY_FIVE_YEAR.is_callable_tenor is True

    def test_thirty_six_year_is_callable_tenor(self):
        assert TENORS.THIRTY_SIX_YEAR.is_callable_tenor is True

    def test_thirty_seven_year_is_callable_tenor(self):
        assert TENORS.THIRTY_SEVEN_YEAR.is_callable_tenor is True

    def test_thirty_eight_year_is_callable_tenor(self):
        assert TENORS.THIRTY_EIGHT_YEAR.is_callable_tenor is True

    def test_thirty_nine_year_is_callable_tenor(self):
        assert TENORS.THIRTY_NINE_YEAR.is_callable_tenor is True

    def test_forty_year_is_callable_tenor(self):
        assert TENORS.FORTY_YEAR.is_callable_tenor is True

    def test_forty_one_year_is_callable_tenor(self):
        assert TENORS.FORTY_ONE_YEAR.is_callable_tenor is True

    def test_forty_two_year_is_callable_tenor(self):
        assert TENORS.FORTY_TWO_YEAR.is_callable_tenor is True

    def test_forty_three_year_is_callable_tenor(self):
        assert TENORS.FORTY_THREE_YEAR.is_callable_tenor is True

    def test_forty_four_year_is_callable_tenor(self):
        assert TENORS.FORTY_FOUR_YEAR.is_callable_tenor is True

    def test_forty_five_year_is_callable_tenor(self):
        assert TENORS.FORTY_FIVE_YEAR.is_callable_tenor is True

    def test_forty_six_year_is_callable_tenor(self):
        assert TENORS.FORTY_SIX_YEAR.is_callable_tenor is True

    def test_forty_seven_year_is_callable_tenor(self):
        assert TENORS.FORTY_SEVEN_YEAR.is_callable_tenor is True

    def test_forty_eight_year_is_callable_tenor(self):
        assert TENORS.FORTY_EIGHT_YEAR.is_callable_tenor is True

    def test_forty_nine_year_is_callable_tenor(self):
        assert TENORS.FORTY_NINE_YEAR.is_callable_tenor is True

    def test_fifty_year_is_callable_tenor(self):
        assert TENORS.FIFTY_YEAR.is_callable_tenor is True


class TestTenorJsonDumps(TestCase):
    def test_dump_uses_label_instead_of_value(self):
        assert json.dumps(TENORS) == json.dumps([t.label for t in TENORS])


class TestTenorComparisons(TestCase):
    def test_less_than_tenor(self):
        assert TENORS.ONE_YEAR < TENORS.TWO_YEAR
        assert TENORS.TWO_YEAR <= TENORS.TWO_YEAR

    def test_less_than_timedelta(self):
        assert TENORS.ONE_YEAR < TENORS.TWO_YEAR.value
        assert TENORS.ONE_YEAR <= TENORS.TWO_YEAR.value
        assert TENORS.ONE_YEAR.value < TENORS.TWO_YEAR
        assert TENORS.TWO_YEAR.value <= TENORS.TWO_YEAR

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert TENORS.ONE_YEAR < 100
        with self.assertRaises(TypeError):
            assert TENORS.ONE_YEAR >= 1

    def test_greater_than_tenor(self):
        assert TENORS.TWO_YEAR > TENORS.ONE_YEAR
        assert TENORS.TWO_YEAR >= TENORS.TWO_YEAR

    def test_greater_than_timedelta(self):
        assert TENORS.TWO_YEAR.value > TENORS.ONE_YEAR
        assert TENORS.TWO_YEAR.value >= TENORS.ONE_YEAR
        assert TENORS.TWO_YEAR > TENORS.ONE_YEAR.value
        assert TENORS.TWO_YEAR >= TENORS.TWO_YEAR.value
