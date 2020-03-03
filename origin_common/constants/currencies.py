from functools import lru_cache
from typing import Tuple, Union

from origin_common.constants.base import Constant, Constants, add_sorting_functions
from origin_common.constants.calendars import CALENDARS, Calendar


class Currency(Constant[str]):
    def __init__(
        self,
        value: str,
        name: str,
        symbol: str = None,
        is_g10=False,
        related_calendars: Tuple[Calendar, ...] = None,
    ):
        super().__init__(value, value)
        self.name = f"{name} ({value})"
        if symbol is None:
            symbol = value
        self.symbol = symbol
        self.is_g10 = is_g10
        self.related_calendars = tuple(related_calendars or [])

    @property
    def code(self):
        # alias for anyone coming from using moneyed
        return self.value


class Currencies(Constants[Currency]):
    USD = Currency(
        value="USD",
        name="US Dollar",
        symbol="$",
        is_g10=True,
        related_calendars=(CALENDARS.NEW_YORK,),
    )
    EUR = Currency(
        value="EUR",
        name="Euro",
        symbol="€",
        is_g10=True,
        related_calendars=(CALENDARS.TARGET2,),
    )
    GBP = Currency(
        value="GBP",
        name="Pound Sterling",
        symbol="£",
        is_g10=True,
        related_calendars=(CALENDARS.LONDON,),
    )
    JPY = Currency(
        value="JPY",
        name="Yen",
        symbol="¥",
        is_g10=True,
        related_calendars=(CALENDARS.TOKYO,),
    )
    CHF = Currency(
        value="CHF",
        name="Swiss Franc",
        # symbol="₣",
        is_g10=True,
        related_calendars=(CALENDARS.ZURICH,),
    )
    AUD = Currency(
        value="AUD",
        name="Australian Dollar",
        # symbol="$",
        is_g10=True,
        related_calendars=(CALENDARS.SYDNEY,),
    )
    NZD = Currency(
        value="NZD",
        name="New Zealand Dollar",
        # symbol="$",
        is_g10=True,
        related_calendars=(CALENDARS.AUCKLAND, CALENDARS.WELLINGTON),
    )
    CAD = Currency(
        value="CAD",
        name="Canadian Dollar",
        # symbol="$",
        is_g10=True,
        related_calendars=(CALENDARS.TORONTO,),
    )
    SEK = Currency(
        value="SEK",
        name="Swedish Krona",
        # symbol="kr",
        is_g10=True,
        related_calendars=(CALENDARS.STOCKHOLM,),
    )
    NOK = Currency(
        value="NOK",
        name="Norwegian Krone",
        # symbol="kr",
        is_g10=True,
        related_calendars=(CALENDARS.OSLO,),
    )

    HKD = Currency(
        value="HKD",
        name="Hong Kong Dollar",
        # symbol="$",
        related_calendars=(CALENDARS.HONG_KONG,),
    )
    AED = Currency(
        value="AED",
        name="UAE Dirham",
        # symbol="د.إ",
        related_calendars=(CALENDARS.DUBAI,),
    )
    AMD = Currency(
        value="AMD",
        name="Armenian Dram",
        # symbol="Դ",
    )
    ARS = Currency(
        value="ARS",
        name="Argentine Peso",
        # symbol="$",
    )
    BRL = Currency(
        value="BRL",
        name="Brazilian Real",
        # symbol="R$",
    )
    CLP = Currency(
        value="CLP",
        name="Chilean peso",
        # symbol="$",
    )
    CNH = Currency(
        value="CNH",  # same as CNY
        name="Yuan Renminbi (Offshore)",
        # symbol="¥",
        related_calendars=(CALENDARS.BEIJING,),
    )
    CNY = Currency(
        value="CNY",
        name="Yuan Renminbi",
        # symbol="¥",
        related_calendars=(CALENDARS.SHANGHAI,),
    )
    COP = Currency(
        value="COP",
        name="Colombian peso",
        # symbol="$",
    )
    CZK = Currency(
        value="CZK",
        name="Czech Koruna",
        # symbol="Kč",
        related_calendars=(CALENDARS.PRAGUE,),
    )
    DKK = Currency(
        value="DKK",
        name="Danish Krone",
        # symbol="kr",
        related_calendars=(CALENDARS.COPENHAGEN,),
    )
    EEK = Currency(
        value="EEK",
        name="Estonian Kroon",
        # symbol="kr",
    )
    GEL = Currency(
        value="GEL",
        name="Lari",
        # symbol="ლ",
    )
    HUF = Currency(
        value="HUF",
        name="Forint",
        # symbol="Ft",
    )
    IDR = Currency(
        value="IDR",
        name="Rupiah",
        # symbol="Rp",
    )
    INR = Currency(
        value="INR",
        name="Indian Rupee",
        # symbol="₹",
    )
    ISK = Currency(
        value="ISK",
        name="Iceland Krona",
        # symbol="Kr",
        related_calendars=(CALENDARS.REYKJAVIK,),
    )
    KGS = Currency(value="KGS", name="Som",)
    KRW = Currency(
        value="KRW", name="Won", symbol="₩", related_calendars=(CALENDARS.SEOUL,),
    )
    KZT = Currency(
        value="KZT",
        name="Tenge",
        # symbol="〒",
    )
    MXN = Currency(
        value="MXN",
        name="Mexican peso",
        # symbol="$",
    )
    MYR = Currency(
        value="MYR",
        name="Malaysian Ringgit",
        # symbol="RM",
    )
    NTD = Currency(
        value="NTD",  # real one is TWD
        name="New Taiwan dollar",
        # symbol="NT$",
    )
    PEN = Currency(
        value="PEN",
        name="Peruvian Sol",
        # symbol="S/.",
    )
    PHP = Currency(
        value="PHP",
        name="Philippine Peso",
        # symbol="₱",
    )
    PLN = Currency(
        value="PLN",
        name="Zloty",
        # symbol="zł",
        related_calendars=(CALENDARS.WARSAW,),
    )
    QAR = Currency(
        value="QAR",
        name="Qatari Rial",
        # symbol="ر.ق",
        related_calendars=(CALENDARS.DOHA,),
    )
    RON = Currency(
        value="RON",
        name="Romanian Leu",
        # symbol="L",
        related_calendars=(CALENDARS.BUCHAREST,),
    )
    RSD = Currency(
        value="RSD",
        name="Serbian Dinar",
        # symbol="din",
    )
    RUB = Currency(
        value="RUB",
        name="Russian Ruble",
        # symbol="р.",
        related_calendars=(CALENDARS.MOSCOW,),
    )
    SGD = Currency(
        value="SGD",
        name="Singapore Dollar",
        # symbol="$",
        related_calendars=(CALENDARS.SINGAPORE,),
    )
    SKK = Currency(
        value="SKK",
        name="Slovak Koruna",
        # symbol="Sk",
    )
    TRY = Currency(
        value="TRY",
        name="Turkish Lira",
        # symbol="₤",
        related_calendars=(CALENDARS.ISTANBUL,),
    )
    UAH = Currency(
        value="UAH",
        name="Hryvnia",
        # symbol="₴",
    )
    UYU = Currency(
        value="UYU",
        name="Uruguayan peso",
        # symbol="$",
    )
    VND = Currency(
        value="VND",
        name="Dong",
        # symbol="₫",
    )
    ZAR = Currency(
        value="ZAR",
        name="Rand",
        # symbol="R",
        related_calendars=(CALENDARS.JOHANNESBURG,),
    )
    ZMK = Currency(
        value="ZMK",  # real one is ZMW
        name="Zambian Kwacha",
        # symbol="K",
    )

    @lru_cache()
    def to_django_choices(self, only_g10=False) -> Tuple[Tuple[str, str]]:
        if only_g10:
            return tuple((attr.value, attr.label) for attr in self if attr.is_g10)
        return super().to_django_choices()

    def get_name(self, value: Union[str, Currency]) -> str:
        return self[value].name


CURRENCIES = Currencies()
add_sorting_functions(Currency, CURRENCIES)
