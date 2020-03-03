from random import choice
from unittest import TestCase

from origin_common.constants import CALENDARS


class TestCalendarValues(TestCase):
    def test_amsterdam(self):
        assert CALENDARS.AMSTERDAM.value == "Amsterdam"

    def test_auckland(self):
        assert CALENDARS.AUCKLAND.value == "Auckland"

    def test_beijing(self):
        assert CALENDARS.BEIJING.value == "Beijing"

    def test_brussels(self):
        assert CALENDARS.BRUSSELS.value == "Brussels"

    def test_bucharest(self):
        assert CALENDARS.BUCHAREST.value == "Bucharest"

    def test_copenhagen(self):
        assert CALENDARS.COPENHAGEN.value == "Copenhagen"

    def test_doha(self):
        assert CALENDARS.DOHA.value == "Doha"

    def test_dubai(self):
        assert CALENDARS.DUBAI.value == "Dubai"

    def test_dublin(self):
        assert CALENDARS.DUBLIN.value == "Dublin"

    def test_frankfurt(self):
        assert CALENDARS.FRANKFURT.value == "Frankfurt"

    def test_helsinki(self):
        assert CALENDARS.HELSINKI.value == "Helsinki"

    def test_hong_kong(self):
        assert CALENDARS.HONG_KONG.value == "Hong Kong"

    def test_istanbul(self):
        assert CALENDARS.ISTANBUL.value == "Istanbul"

    def test_johannesburg(self):
        assert CALENDARS.JOHANNESBURG.value == "Johannesburg"

    def test_london(self):
        assert CALENDARS.LONDON.value == "London"

    def test_luxembourg(self):
        assert CALENDARS.LUXEMBOURG.value == "Luxembourg"

    def test_madrid(self):
        assert CALENDARS.MADRID.value == "Madrid"

    def test_moscow(self):
        assert CALENDARS.MOSCOW.value == "Moscow"

    def test_macau(self):
        assert CALENDARS.MACAU.value == "Macau"

    def test_new_york(self):
        assert CALENDARS.NEW_YORK.value == "New York"

    def test_oslo(self):
        assert CALENDARS.OSLO.value == "Oslo"

    def test_paris(self):
        assert CALENDARS.PARIS.value == "Paris"

    def test_prague(self):
        assert CALENDARS.PRAGUE.value == "Prague"

    def test_reykjavik(self):
        assert CALENDARS.REYKJAVIK.value == "Reykjavik"

    def test_seoul(self):
        assert CALENDARS.SEOUL.value == "Seoul"

    def test_shanghai(self):
        assert CALENDARS.SHANGHAI.value == "Shanghai"

    def test_singapore(self):
        assert CALENDARS.SINGAPORE.value == "Singapore"

    def test_stockholm(self):
        assert CALENDARS.STOCKHOLM.value == "Stockholm"

    def test_sydney(self):
        assert CALENDARS.SYDNEY.value == "Sydney"

    def test_target2(self):
        assert CALENDARS.TARGET2.value == "TARGET2"

    def test_tokyo(self):
        assert CALENDARS.TOKYO.value == "Tokyo"

    def test_toronto(self):
        assert CALENDARS.TORONTO.value == "Toronto"

    def test_vienna(self):
        assert CALENDARS.VIENNA.value == "Vienna"

    def test_warsaw(self):
        assert CALENDARS.WARSAW.value == "Warsaw"

    def test_wellington(self):
        assert CALENDARS.WELLINGTON.value == "Wellington"

    def test_zurich(self):
        assert CALENDARS.ZURICH.value == "Zurich"


class TestCalendarLabels(TestCase):
    def test_label_is_same_as_value(self):
        calendar = choice(list(CALENDARS))
        assert calendar.label == calendar.value


class TestCalendarOrder(TestCase):
    def test_order(self):
        expected = [
            CALENDARS.AMSTERDAM,
            CALENDARS.AUCKLAND,
            CALENDARS.BEIJING,
            CALENDARS.BRUSSELS,
            CALENDARS.BUCHAREST,
            CALENDARS.COPENHAGEN,
            CALENDARS.DOHA,
            CALENDARS.DUBAI,
            CALENDARS.DUBLIN,
            CALENDARS.FRANKFURT,
            CALENDARS.HELSINKI,
            CALENDARS.HONG_KONG,
            CALENDARS.ISTANBUL,
            CALENDARS.JOHANNESBURG,
            CALENDARS.LONDON,
            CALENDARS.LUXEMBOURG,
            CALENDARS.MADRID,
            CALENDARS.MOSCOW,
            CALENDARS.MACAU,
            CALENDARS.NEW_YORK,
            CALENDARS.OSLO,
            CALENDARS.PARIS,
            CALENDARS.PRAGUE,
            CALENDARS.REYKJAVIK,
            CALENDARS.SEOUL,
            CALENDARS.SHANGHAI,
            CALENDARS.SINGAPORE,
            CALENDARS.STOCKHOLM,
            CALENDARS.SYDNEY,
            CALENDARS.TARGET2,
            CALENDARS.TOKYO,
            CALENDARS.TORONTO,
            CALENDARS.VIENNA,
            CALENDARS.WARSAW,
            CALENDARS.WELLINGTON,
            CALENDARS.ZURICH,
        ]
        assert list(CALENDARS) == expected

    def test_django_choices(self):
        expected = (
            (CALENDARS.AMSTERDAM.value, CALENDARS.AMSTERDAM.label),
            (CALENDARS.AUCKLAND.value, CALENDARS.AUCKLAND.label),
            (CALENDARS.BEIJING.value, CALENDARS.BEIJING.label),
            (CALENDARS.BRUSSELS.value, CALENDARS.BRUSSELS.label),
            (CALENDARS.BUCHAREST.value, CALENDARS.BUCHAREST.label),
            (CALENDARS.COPENHAGEN.value, CALENDARS.COPENHAGEN.label),
            (CALENDARS.DOHA.value, CALENDARS.DOHA.label),
            (CALENDARS.DUBAI.value, CALENDARS.DUBAI.label),
            (CALENDARS.DUBLIN.value, CALENDARS.DUBLIN.label),
            (CALENDARS.FRANKFURT.value, CALENDARS.FRANKFURT.label),
            (CALENDARS.HELSINKI.value, CALENDARS.HELSINKI.label),
            (CALENDARS.HONG_KONG.value, CALENDARS.HONG_KONG.label),
            (CALENDARS.ISTANBUL.value, CALENDARS.ISTANBUL.label),
            (CALENDARS.JOHANNESBURG.value, CALENDARS.JOHANNESBURG.label),
            (CALENDARS.LONDON.value, CALENDARS.LONDON.label),
            (CALENDARS.LUXEMBOURG.value, CALENDARS.LUXEMBOURG.label),
            (CALENDARS.MADRID.value, CALENDARS.MADRID.label),
            (CALENDARS.MOSCOW.value, CALENDARS.MOSCOW.label),
            (CALENDARS.MACAU.value, CALENDARS.MACAU.label),
            (CALENDARS.NEW_YORK.value, CALENDARS.NEW_YORK.label),
            (CALENDARS.OSLO.value, CALENDARS.OSLO.label),
            (CALENDARS.PARIS.value, CALENDARS.PARIS.label),
            (CALENDARS.PRAGUE.value, CALENDARS.PRAGUE.label),
            (CALENDARS.REYKJAVIK.value, CALENDARS.REYKJAVIK.label),
            (CALENDARS.SEOUL.value, CALENDARS.SEOUL.label),
            (CALENDARS.SHANGHAI.value, CALENDARS.SHANGHAI.label),
            (CALENDARS.SINGAPORE.value, CALENDARS.SINGAPORE.label),
            (CALENDARS.STOCKHOLM.value, CALENDARS.STOCKHOLM.label),
            (CALENDARS.SYDNEY.value, CALENDARS.SYDNEY.label),
            (CALENDARS.TARGET2.value, CALENDARS.TARGET2.label),
            (CALENDARS.TOKYO.value, CALENDARS.TOKYO.label),
            (CALENDARS.TORONTO.value, CALENDARS.TORONTO.label),
            (CALENDARS.VIENNA.value, CALENDARS.VIENNA.label),
            (CALENDARS.WARSAW.value, CALENDARS.WARSAW.label),
            (CALENDARS.WELLINGTON.value, CALENDARS.WELLINGTON.label),
            (CALENDARS.ZURICH.value, CALENDARS.ZURICH.label),
        )
        assert CALENDARS.to_django_choices() == expected


class TestCalendarComparisons(TestCase):
    def test_less_than_calendar(self):
        assert CALENDARS.AMSTERDAM < CALENDARS.OSLO
        assert CALENDARS.OSLO <= CALENDARS.OSLO

    def test_less_than_string(self):
        assert CALENDARS.AMSTERDAM < CALENDARS.OSLO.value
        assert CALENDARS.AMSTERDAM <= CALENDARS.OSLO.value
        assert CALENDARS.AMSTERDAM.value < CALENDARS.OSLO
        assert CALENDARS.OSLO.value <= CALENDARS.OSLO

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert CALENDARS.AMSTERDAM < 100
        with self.assertRaises(TypeError):
            assert CALENDARS.AMSTERDAM >= 1

    def test_cannot_compare_to_non_calendar_strings(self):
        with self.assertRaises(TypeError):
            assert CALENDARS.AMSTERDAM < "FOO"
        with self.assertRaises(TypeError):
            assert CALENDARS.AMSTERDAM >= "BAR"

    def test_greater_than_calendar(self):
        assert CALENDARS.OSLO > CALENDARS.AMSTERDAM
        assert CALENDARS.OSLO >= CALENDARS.OSLO

    def test_greater_than_string(self):
        assert CALENDARS.OSLO.value > CALENDARS.AMSTERDAM
        assert CALENDARS.OSLO.value >= CALENDARS.AMSTERDAM
        assert CALENDARS.OSLO > CALENDARS.AMSTERDAM.value
        assert CALENDARS.OSLO >= CALENDARS.OSLO.value


# class TestGetCalendarForFixing(TestCase):
#     def test_returns_funding_basis_calendar_for_fixing(self):
#         basis = choice([basis for basis in FUNDING_BASES if basis.calendar_for_fixing])
#         assert CALENDARS.get_calendar_for_fixing(basis) == basis.calendar_for_fixing
#
#     def test_works_with_funding_basis_value(self):
#         basis = choice([basis for basis in FUNDING_BASES if basis.calendar_for_fixing])
#         actual = CALENDARS.get_calendar_for_fixing(basis.value)
#         assert actual == basis.calendar_for_fixing
#
#     def test_works_with_funding_basis_label(self):
#         basis = choice([basis for basis in FUNDING_BASES if basis.calendar_for_fixing])
#         actual = CALENDARS.get_calendar_for_fixing(basis.label)
#         assert actual == basis.calendar_for_fixing
#
#
# class TestGetCalendarsForPayment(TestCase):
#     country_to_calendar_mappings_keys = list(COUNTRY_TO_CALENDAR_MAPPINGS.keys())
#     # currency_to_calendar_mapping_keys = list(CURRENCY_TO_CALENDAR_MAPPING.keys())
#
#     def test_filters_by_issuer_country(self):
#         country = choice(self.country_to_calendar_mappings_keys)
#         expected = set(COUNTRY_TO_CALENDAR_MAPPINGS[country])
#         actual = CALENDARS.get_calendars_for_payment(country=country)
#         assert actual == expected
#
#     def test_filters_by_basis(self):
#         basis = choice(
#             [basis for basis in FUNDING_BASES if basis.calendars_for_payment]
#         )
#         expected = set(basis.calendars_for_payment)
#         actual = CALENDARS.get_calendars_for_payment(funding_basis=basis)
#         assert actual == expected
#
#     # def test_filters_by_currency(self):
#     #     currency = choice(self.currency_to_calendar_mapping_keys)
#     #     expected = set(CURRENCY_TO_CALENDAR_MAPPING[currency])
#     #     actual = CALENDARS.get_calendars_for_payment(currency=currency)
#     #     assert actual == expected
#
#     def test_filters_all_together(self):
#         country = choice(self.country_to_calendar_mappings_keys)
#         basis = choice(
#             [basis for basis in FUNDING_BASES if basis.calendars_for_payment]
#         )
#
#         # currency = choice(self.currency_to_calendar_mapping_keys)
#         currency = None
#         expected = (
#             set(COUNTRY_TO_CALENDAR_MAPPINGS[country])
#             | set(basis.calendars_for_payment)
#             # | set(CURRENCY_TO_CALENDAR_MAPPING[currency])
#         )
#         actual = CALENDARS.get_calendars_for_payment(
#             currency=currency, funding_basis=basis, country=country
#         )
#         assert actual == expected
