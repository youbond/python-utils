from typing import Tuple

from origin_common.constants.base import Constant, Constants


class Currency(Constant[str]):
    def __init__(self, value: str, label: str, symbol: str = None, is_g10=False):
        label = "{} ({})".format(label, value)
        super().__init__(value, label)
        if symbol is None:
            symbol = value
        self.symbol = symbol
        self.is_g10 = is_g10

    @property
    def code(self):
        # alias for anyone coming from using moneyed
        return self.value


class Currencies(Constants[Currency]):
    USD = Currency(value="USD", label="US Dollar", symbol="$", is_g10=True,)
    EUR = Currency(value="EUR", label="Euro", symbol="€", is_g10=True,)
    GBP = Currency(value="GBP", label="Pound Sterling", symbol="£", is_g10=True,)
    JPY = Currency(value="JPY", label="Yen", symbol="¥", is_g10=True,)
    CHF = Currency(
        value="CHF",
        label="Swiss Franc",
        # symbol="₣",
        is_g10=True,
    )
    AUD = Currency(
        value="AUD",
        label="Australian Dollar",
        # symbol="$",
        is_g10=True,
    )
    NZD = Currency(
        value="NZD",
        label="New Zealand Dollar",
        # symbol="$",
        is_g10=True,
    )
    CAD = Currency(
        value="CAD",
        label="Canadian Dollar",
        # symbol="$",
        is_g10=True,
    )
    SEK = Currency(
        value="SEK",
        label="Swedish Krona",
        # symbol="kr",
        is_g10=True,
    )
    NOK = Currency(
        value="NOK",
        label="Norwegian Krone",
        # symbol="kr",
        is_g10=True,
    )

    HKD = Currency(
        value="HKD",
        label="Hong Kong Dollar",
        # symbol="$",
    )
    AED = Currency(
        value="AED",
        label="UAE Dirham",
        # symbol="د.إ",
    )
    AMD = Currency(
        value="AMD",
        label="Armenian Dram",
        # symbol="Դ",
    )
    ARS = Currency(
        value="ARS",
        label="Argentine Peso",
        # symbol="$",
    )
    BRL = Currency(
        value="BRL",
        label="Brazilian Real",
        # symbol="R$",
    )
    CLP = Currency(
        value="CLP",
        label="Chilean peso",
        # symbol="$",
    )
    CNH = Currency(
        value="CNH",  # same as CNY
        label="Yuan Renminbi (Offshore)",
        # symbol="¥",
    )
    CNY = Currency(
        value="CNY",
        label="Yuan Renminbi",
        # symbol="¥",
    )
    COP = Currency(
        value="COP",
        label="Colombian peso",
        # symbol="$",
    )
    CZK = Currency(
        value="CZK",
        label="Czech Koruna",
        # symbol="Kč",
    )
    DKK = Currency(
        value="DKK",
        label="Danish Krone",
        # symbol="kr",
    )
    EEK = Currency(
        value="EEK",
        label="Estonian Kroon",
        # symbol="kr",
    )
    GEL = Currency(
        value="GEL",
        label="Lari",
        # symbol="ლ",
    )
    HUF = Currency(
        value="HUF",
        label="Forint",
        # symbol="Ft",
    )
    IDR = Currency(
        value="IDR",
        label="Rupiah",
        # symbol="Rp",
    )
    INR = Currency(
        value="INR",
        label="Indian Rupee",
        # symbol="₹",
    )
    ISK = Currency(
        value="ISK",
        label="Iceland Krona",
        # symbol="Kr",
    )
    KGS = Currency(value="KGS", label="Som",)
    KRW = Currency(value="KRW", label="Won", symbol="₩",)
    KZT = Currency(
        value="KZT",
        label="Tenge",
        # symbol="〒",
    )
    MXN = Currency(
        value="MXN",
        label="Mexican peso",
        # symbol="$",
    )
    MYR = Currency(
        value="MYR",
        label="Malaysian Ringgit",
        # symbol="RM",
    )
    NTD = Currency(
        value="NTD",  # real one is TWD
        label="New Taiwan dollar",
        # symbol="NT$",
    )
    PEN = Currency(
        value="PEN",
        label="Peruvian Sol",
        # symbol="S/.",
    )
    PHP = Currency(
        value="PHP",
        label="Philippine Peso",
        # symbol="₱",
    )
    PLN = Currency(
        value="PLN",
        label="Zloty",
        # symbol="zł",
    )
    QAR = Currency(
        value="QAR",
        label="Qatari Rial",
        # symbol="ر.ق",
    )
    RON = Currency(
        value="RON",
        label="New Leu",
        # symbol="L",
    )
    RSD = Currency(
        value="RSD",
        label="Serbian Dinar",
        # symbol="din",
    )
    RUB = Currency(
        value="RUB",
        label="Russian Ruble",
        # symbol="р.",
    )
    SGD = Currency(
        value="SGD",
        label="Singapore Dollar",
        # symbol="$",
    )
    SKK = Currency(
        value="SKK",
        label="Slovak Koruna",
        # symbol="Sk",
    )
    TRY = Currency(
        value="TRY",
        label="Turkish Lira",
        # symbol="₤",
    )
    UAH = Currency(
        value="UAH",
        label="Hryvnia",
        # symbol="₴",
    )
    UYU = Currency(
        value="UYU",
        label="Uruguayan peso",
        # symbol="$",
    )
    VND = Currency(
        value="VND",
        label="Dong",
        # symbol="₫",
    )
    ZAR = Currency(
        value="ZAR",
        label="Rand",
        # symbol="R",
    )
    ZMK = Currency(
        value="ZMK",  # real one is ZMW
        label="Zambian Kwacha",
        # symbol="K",
    )

    def to_django_choices(self, only_g10=False) -> Tuple[Tuple[str, str]]:
        if only_g10:
            return tuple((attr.value, attr.label) for attr in self if attr.is_g10)
        return super().to_django_choices()


CURRENCIES = Currencies()
