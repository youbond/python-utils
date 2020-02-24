from origin_common.constants.base import Constant, Constants, add_sorting_functions


class BusinessDayConvention(Constant[str]):
    def __init__(self, value: str):
        super().__init__(value, value)


class BusinessDayConventions(Constants):
    FOLLOWING = BusinessDayConvention("Following")
    PRECEDING = BusinessDayConvention("Preceding")
    MODIFIED_FOLLOWING = BusinessDayConvention("Modified Following")
    MODIFIED_PRECEDING = BusinessDayConvention("Modified Preceding")
    HALF_MONTH_MODIFIED_FOLLOWING = BusinessDayConvention(
        "Half Month Modified Following"
    )


BUSINESS_DAY_CONVENTIONS = BusinessDayConventions()
BUSINESS_DAY_CONVENTIONS.make_immutable()
add_sorting_functions(BusinessDayConvention, BUSINESS_DAY_CONVENTIONS)
