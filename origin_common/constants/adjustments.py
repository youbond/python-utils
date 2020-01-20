from origin_common.constants.base import Constant, Constants


class Adjustment(Constant[str]):
    def __init__(self, value: str):
        super().__init__(value, value)


class Adjustments(Constants):
    ADJUSTED = Adjustment("Adjusted")
    UNADJUSTED = Adjustment("Unadjusted")


ADJUSTMENTS = Adjustments()
ADJUSTMENTS.make_immutable()
