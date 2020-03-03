from origin_common.constants.base import Constant, Constants, add_sorting_functions


class Calendar(Constant[str]):
    def __init__(self, value: str):
        label = value
        super().__init__(value, label)


class Calendars(Constants[Calendar]):
    AMSTERDAM = Calendar("Amsterdam")
    AUCKLAND = Calendar("Auckland")
    BEIJING = Calendar("Beijing")
    BRUSSELS = Calendar("Brussels")
    BUCHAREST = Calendar("Bucharest")
    COPENHAGEN = Calendar("Copenhagen")
    DOHA = Calendar("Doha")
    DUBAI = Calendar("Dubai")
    DUBLIN = Calendar("Dublin")
    FRANKFURT = Calendar("Frankfurt")
    HELSINKI = Calendar("Helsinki")
    HONG_KONG = Calendar("Hong Kong")
    ISTANBUL = Calendar("Istanbul")
    JOHANNESBURG = Calendar("Johannesburg")
    LONDON = Calendar("London")
    LUXEMBOURG = Calendar("Luxembourg")
    MADRID = Calendar("Madrid")
    MOSCOW = Calendar("Moscow")
    MACAU = Calendar("Macau")
    NEW_YORK = Calendar("New York")
    OSLO = Calendar("Oslo")
    PARIS = Calendar("Paris")
    PRAGUE = Calendar("Prague")
    REYKJAVIK = Calendar("Reykjavik")
    SEOUL = Calendar("Seoul")
    SHANGHAI = Calendar("Shanghai")
    SINGAPORE = Calendar("Singapore")
    STOCKHOLM = Calendar("Stockholm")
    SYDNEY = Calendar("Sydney")
    TARGET2 = Calendar("TARGET2")
    TOKYO = Calendar("Tokyo")
    TORONTO = Calendar("Toronto")
    VIENNA = Calendar("Vienna")
    WARSAW = Calendar("Warsaw")
    WELLINGTON = Calendar("Wellington")
    ZURICH = Calendar("Zurich")


CALENDARS = Calendars()
CALENDARS.make_immutable()
add_sorting_functions(Calendar, CALENDARS)
