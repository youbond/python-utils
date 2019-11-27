from origin_common.constants.base import Constant, Constants


class PaymentFrequency(Constant[int]):
    pass


class PaymentFrequencies(Constants):
    AT_MATURITY = PaymentFrequency(0, "At Maturity")
    QUARTERLY = PaymentFrequency(3, "Quarterly")
    SEMI_ANNUALLY = PaymentFrequency(6, "Semi-Annually")
    ANNUALLY = PaymentFrequency(12, "Annually")


PAYMENT_FREQUENCIES = PaymentFrequencies()
