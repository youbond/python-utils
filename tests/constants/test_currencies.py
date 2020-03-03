from random import choice
from unittest import TestCase

from origin_common.better_test_mixins import LruCacheTestMixin
from origin_common.constants import CALENDARS, CURRENCIES


class TestCurrencyValues(TestCase):
    def test_aed_value(self):
        assert CURRENCIES.AED.value == "AED"

    def test_amd_value(self):
        assert CURRENCIES.AMD.value == "AMD"

    def test_ars_value(self):
        assert CURRENCIES.ARS.value == "ARS"

    def test_aud_value(self):
        assert CURRENCIES.AUD.value == "AUD"

    def test_brl_value(self):
        assert CURRENCIES.BRL.value == "BRL"

    def test_cad_value(self):
        assert CURRENCIES.CAD.value == "CAD"

    def test_chf_value(self):
        assert CURRENCIES.CHF.value == "CHF"

    def test_clp_value(self):
        assert CURRENCIES.CLP.value == "CLP"

    def test_cnh_value(self):
        assert CURRENCIES.CNH.value == "CNH"

    def test_cny_value(self):
        assert CURRENCIES.CNY.value == "CNY"

    def test_cop_value(self):
        assert CURRENCIES.COP.value == "COP"

    def test_czk_value(self):
        assert CURRENCIES.CZK.value == "CZK"

    def test_dkk_value(self):
        assert CURRENCIES.DKK.value == "DKK"

    def test_eur_value(self):
        assert CURRENCIES.EUR.value == "EUR"

    def test_eek_value(self):
        assert CURRENCIES.EEK.value == "EEK"

    def test_gbp_value(self):
        assert CURRENCIES.GBP.value == "GBP"

    def test_gel_value(self):
        assert CURRENCIES.GEL.value == "GEL"

    def test_hkd_value(self):
        assert CURRENCIES.HKD.value == "HKD"

    def test_huf_value(self):
        assert CURRENCIES.HUF.value == "HUF"

    def test_idr_value(self):
        assert CURRENCIES.IDR.value == "IDR"

    def test_inr_value(self):
        assert CURRENCIES.INR.value == "INR"

    def test_isk_value(self):
        assert CURRENCIES.ISK.value == "ISK"

    def test_jpy_value(self):
        assert CURRENCIES.JPY.value == "JPY"

    def test_kgs_value(self):
        assert CURRENCIES.KGS.value == "KGS"

    def test_krw_value(self):
        assert CURRENCIES.KRW.value == "KRW"

    def test_kzt_value(self):
        assert CURRENCIES.KZT.value == "KZT"

    def test_mxn_value(self):
        assert CURRENCIES.MXN.value == "MXN"

    def test_myr_value(self):
        assert CURRENCIES.MYR.value == "MYR"

    def test_nok_value(self):
        assert CURRENCIES.NOK.value == "NOK"

    def test_nzd_value(self):
        assert CURRENCIES.NZD.value == "NZD"

    def test_ntd_value(self):
        assert CURRENCIES.NTD.value == "NTD"

    def test_pen_value(self):
        assert CURRENCIES.PEN.value == "PEN"

    def test_php_value(self):
        assert CURRENCIES.PHP.value == "PHP"

    def test_pln_value(self):
        assert CURRENCIES.PLN.value == "PLN"

    def test_qar_value(self):
        assert CURRENCIES.QAR.value == "QAR"

    def test_ron_value(self):
        assert CURRENCIES.RON.value == "RON"

    def test_rsd_value(self):
        assert CURRENCIES.RSD.value == "RSD"

    def test_rub_value(self):
        assert CURRENCIES.RUB.value == "RUB"

    def test_sek_value(self):
        assert CURRENCIES.SEK.value == "SEK"

    def test_sgd_value(self):
        assert CURRENCIES.SGD.value == "SGD"

    def test_skk_value(self):
        assert CURRENCIES.SKK.value == "SKK"

    def test_try_value(self):
        assert CURRENCIES.TRY.value == "TRY"

    def test_uah_value(self):
        assert CURRENCIES.UAH.value == "UAH"

    def test_usd_value(self):
        assert CURRENCIES.USD.value == "USD"

    def test_uyu_value(self):
        assert CURRENCIES.UYU.value == "UYU"

    def test_vnd_value(self):
        assert CURRENCIES.VND.value == "VND"

    def test_zar_value(self):
        assert CURRENCIES.ZAR.value == "ZAR"

    def test_zmk_value(self):
        assert CURRENCIES.ZMK.value == "ZMK"


class TestCurrencyLabels(TestCase):
    def test_aed_label(self):
        assert CURRENCIES.AED.label == "AED"

    def test_amd_label(self):
        assert CURRENCIES.AMD.label == "AMD"

    def test_ars_label(self):
        assert CURRENCIES.ARS.label == "ARS"

    def test_aud_label(self):
        assert CURRENCIES.AUD.label == "AUD"

    def test_brl_label(self):
        assert CURRENCIES.BRL.label == "BRL"

    def test_cad_label(self):
        assert CURRENCIES.CAD.label == "CAD"

    def test_chf_label(self):
        assert CURRENCIES.CHF.label == "CHF"

    def test_clp_label(self):
        assert CURRENCIES.CLP.label == "CLP"

    def test_cnh_label(self):
        assert CURRENCIES.CNH.label == "CNH"

    def test_cny_label(self):
        assert CURRENCIES.CNY.label == "CNY"

    def test_cop_label(self):
        assert CURRENCIES.COP.label == "COP"

    def test_czk_label(self):
        assert CURRENCIES.CZK.label == "CZK"

    def test_dkk_label(self):
        assert CURRENCIES.DKK.label == "DKK"

    def test_eur_label(self):
        assert CURRENCIES.EUR.label == "EUR"

    def test_eek_label(self):
        assert CURRENCIES.EEK.label == "EEK"

    def test_gbp_label(self):
        assert CURRENCIES.GBP.label == "GBP"

    def test_gel_label(self):
        assert CURRENCIES.GEL.label == "GEL"

    def test_hkd_label(self):
        assert CURRENCIES.HKD.label == "HKD"

    def test_huf_label(self):
        assert CURRENCIES.HUF.label == "HUF"

    def test_idr_label(self):
        assert CURRENCIES.IDR.label == "IDR"

    def test_inr_label(self):
        assert CURRENCIES.INR.label == "INR"

    def test_isk_label(self):
        assert CURRENCIES.ISK.label == "ISK"

    def test_jpy_label(self):
        assert CURRENCIES.JPY.label == "JPY"

    def test_kgs_label(self):
        assert CURRENCIES.KGS.label == "KGS"

    def test_krw_label(self):
        assert CURRENCIES.KRW.label == "KRW"

    def test_kzt_label(self):
        assert CURRENCIES.KZT.label == "KZT"

    def test_mxn_label(self):
        assert CURRENCIES.MXN.label == "MXN"

    def test_myr_label(self):
        assert CURRENCIES.MYR.label == "MYR"

    def test_nok_label(self):
        assert CURRENCIES.NOK.label == "NOK"

    def test_nzd_label(self):
        assert CURRENCIES.NZD.label == "NZD"

    def test_ntd_label(self):
        assert CURRENCIES.NTD.label == "NTD"

    def test_pen_label(self):
        assert CURRENCIES.PEN.label == "PEN"

    def test_php_label(self):
        assert CURRENCIES.PHP.label == "PHP"

    def test_pln_label(self):
        assert CURRENCIES.PLN.label == "PLN"

    def test_qar_label(self):
        assert CURRENCIES.QAR.label == "QAR"

    def test_ron_label(self):
        assert CURRENCIES.RON.label == "RON"

    def test_rsd_label(self):
        assert CURRENCIES.RSD.label == "RSD"

    def test_rub_label(self):
        assert CURRENCIES.RUB.label == "RUB"

    def test_sek_label(self):
        assert CURRENCIES.SEK.label == "SEK"

    def test_sgd_label(self):
        assert CURRENCIES.SGD.label == "SGD"

    def test_skk_label(self):
        assert CURRENCIES.SKK.label == "SKK"

    def test_try_label(self):
        assert CURRENCIES.TRY.label == "TRY"

    def test_uah_label(self):
        assert CURRENCIES.UAH.label == "UAH"

    def test_usd_label(self):
        assert CURRENCIES.USD.label == "USD"

    def test_uyu_label(self):
        assert CURRENCIES.UYU.label == "UYU"

    def test_vnd_label(self):
        assert CURRENCIES.VND.label == "VND"

    def test_zar_label(self):
        assert CURRENCIES.ZAR.label == "ZAR"

    def test_zmk_label(self):
        assert CURRENCIES.ZMK.label == "ZMK"


class TestCurrencyNames(TestCase):
    def test_aed_name(self):
        assert CURRENCIES.AED.name == "UAE Dirham (AED)"

    def test_amd_name(self):
        assert CURRENCIES.AMD.name == "Armenian Dram (AMD)"

    def test_ars_name(self):
        assert CURRENCIES.ARS.name == "Argentine Peso (ARS)"

    def test_aud_name(self):
        assert CURRENCIES.AUD.name == "Australian Dollar (AUD)"

    def test_brl_name(self):
        assert CURRENCIES.BRL.name == "Brazilian Real (BRL)"

    def test_cad_name(self):
        assert CURRENCIES.CAD.name == "Canadian Dollar (CAD)"

    def test_chf_name(self):
        assert CURRENCIES.CHF.name == "Swiss Franc (CHF)"

    def test_clp_name(self):
        assert CURRENCIES.CLP.name == "Chilean peso (CLP)"

    def test_cnh_name(self):
        assert CURRENCIES.CNH.name == "Yuan Renminbi (Offshore) (CNH)"

    def test_cny_name(self):
        assert CURRENCIES.CNY.name == "Yuan Renminbi (CNY)"

    def test_cop_name(self):
        assert CURRENCIES.COP.name == "Colombian peso (COP)"

    def test_czk_name(self):
        assert CURRENCIES.CZK.name == "Czech Koruna (CZK)"

    def test_dkk_name(self):
        assert CURRENCIES.DKK.name == "Danish Krone (DKK)"

    def test_eur_name(self):
        assert CURRENCIES.EUR.name == "Euro (EUR)"

    def test_eek_name(self):
        assert CURRENCIES.EEK.name == "Estonian Kroon (EEK)"

    def test_gbp_name(self):
        assert CURRENCIES.GBP.name == "Pound Sterling (GBP)"

    def test_gel_name(self):
        assert CURRENCIES.GEL.name == "Lari (GEL)"

    def test_hkd_name(self):
        assert CURRENCIES.HKD.name == "Hong Kong Dollar (HKD)"

    def test_huf_name(self):
        assert CURRENCIES.HUF.name == "Forint (HUF)"

    def test_idr_name(self):
        assert CURRENCIES.IDR.name == "Rupiah (IDR)"

    def test_inr_name(self):
        assert CURRENCIES.INR.name == "Indian Rupee (INR)"

    def test_isk_name(self):
        assert CURRENCIES.ISK.name == "Iceland Krona (ISK)"

    def test_jpy_name(self):
        assert CURRENCIES.JPY.name == "Yen (JPY)"

    def test_kgs_name(self):
        assert CURRENCIES.KGS.name == "Som (KGS)"

    def test_krw_name(self):
        assert CURRENCIES.KRW.name == "Won (KRW)"

    def test_kzt_name(self):
        assert CURRENCIES.KZT.name == "Tenge (KZT)"

    def test_mxn_name(self):
        assert CURRENCIES.MXN.name == "Mexican peso (MXN)"

    def test_myr_name(self):
        assert CURRENCIES.MYR.name == "Malaysian Ringgit (MYR)"

    def test_nok_name(self):
        assert CURRENCIES.NOK.name == "Norwegian Krone (NOK)"

    def test_nzd_name(self):
        assert CURRENCIES.NZD.name == "New Zealand Dollar (NZD)"

    def test_ntd_name(self):
        assert CURRENCIES.NTD.name == "New Taiwan dollar (NTD)"

    def test_pen_name(self):
        assert CURRENCIES.PEN.name == "Peruvian Sol (PEN)"

    def test_php_name(self):
        assert CURRENCIES.PHP.name == "Philippine Peso (PHP)"

    def test_pln_name(self):
        assert CURRENCIES.PLN.name == "Zloty (PLN)"

    def test_qar_name(self):
        assert CURRENCIES.QAR.name == "Qatari Rial (QAR)"

    def test_ron_name(self):
        assert CURRENCIES.RON.name == "Romanian Leu (RON)"

    def test_rsd_name(self):
        assert CURRENCIES.RSD.name == "Serbian Dinar (RSD)"

    def test_rub_name(self):
        assert CURRENCIES.RUB.name == "Russian Ruble (RUB)"

    def test_sek_name(self):
        assert CURRENCIES.SEK.name == "Swedish Krona (SEK)"

    def test_sgd_name(self):
        assert CURRENCIES.SGD.name == "Singapore Dollar (SGD)"

    def test_skk_name(self):
        assert CURRENCIES.SKK.name == "Slovak Koruna (SKK)"

    def test_try_name(self):
        assert CURRENCIES.TRY.name == "Turkish Lira (TRY)"

    def test_uah_name(self):
        assert CURRENCIES.UAH.name == "Hryvnia (UAH)"

    def test_usd_name(self):
        assert CURRENCIES.USD.name == "US Dollar (USD)"

    def test_uyu_name(self):
        assert CURRENCIES.UYU.name == "Uruguayan peso (UYU)"

    def test_vnd_name(self):
        assert CURRENCIES.VND.name == "Dong (VND)"

    def test_zar_name(self):
        assert CURRENCIES.ZAR.name == "Rand (ZAR)"

    def test_zmk_name(self):
        assert CURRENCIES.ZMK.name == "Zambian Kwacha (ZMK)"


class TestCurrencySymbols(TestCase):
    def test_aed_symbol(self):
        assert CURRENCIES.AED.symbol == "AED"

    def test_amd_symbol(self):
        assert CURRENCIES.AMD.symbol == "AMD"

    def test_ars_symbol(self):
        assert CURRENCIES.ARS.symbol == "ARS"

    def test_aud_symbol(self):
        assert CURRENCIES.AUD.symbol == "AUD"

    def test_brl_symbol(self):
        assert CURRENCIES.BRL.symbol == "BRL"

    def test_cad_symbol(self):
        assert CURRENCIES.CAD.symbol == "CAD"

    def test_chf_symbol(self):
        assert CURRENCIES.CHF.symbol == "CHF"

    def test_clp_symbol(self):
        assert CURRENCIES.CLP.symbol == "CLP"

    def test_cnh_symbol(self):
        assert CURRENCIES.CNH.symbol == "CNH"

    def test_cny_symbol(self):
        assert CURRENCIES.CNY.symbol == "CNY"

    def test_cop_symbol(self):
        assert CURRENCIES.COP.symbol == "COP"

    def test_czk_symbol(self):
        assert CURRENCIES.CZK.symbol == "CZK"

    def test_dkk_symbol(self):
        assert CURRENCIES.DKK.symbol == "DKK"

    def test_eur_symbol(self):
        assert CURRENCIES.EUR.symbol == "€"

    def test_eek_symbol(self):
        assert CURRENCIES.EEK.symbol == "EEK"

    def test_gbp_symbol(self):
        assert CURRENCIES.GBP.symbol == "£"

    def test_gel_symbol(self):
        assert CURRENCIES.GEL.symbol == "GEL"

    def test_hkd_symbol(self):
        assert CURRENCIES.HKD.symbol == "HKD"

    def test_huf_symbol(self):
        assert CURRENCIES.HUF.symbol == "HUF"

    def test_idr_symbol(self):
        assert CURRENCIES.IDR.symbol == "IDR"

    def test_inr_symbol(self):
        assert CURRENCIES.INR.symbol == "INR"

    def test_isk_symbol(self):
        assert CURRENCIES.ISK.symbol == "ISK"

    def test_jpy_symbol(self):
        assert CURRENCIES.JPY.symbol == "¥"

    def test_kgs_symbol(self):
        assert CURRENCIES.KGS.symbol == "KGS"

    def test_krw_symbol(self):
        assert CURRENCIES.KRW.symbol == "₩"

    def test_kzt_symbol(self):
        assert CURRENCIES.KZT.symbol == "KZT"

    def test_mxn_symbol(self):
        assert CURRENCIES.MXN.symbol == "MXN"

    def test_myr_symbol(self):
        assert CURRENCIES.MYR.symbol == "MYR"

    def test_nok_symbol(self):
        assert CURRENCIES.NOK.symbol == "NOK"

    def test_nzd_symbol(self):
        assert CURRENCIES.NZD.symbol == "NZD"

    def test_ntd_symbol(self):
        assert CURRENCIES.NTD.symbol == "NTD"

    def test_pen_symbol(self):
        assert CURRENCIES.PEN.symbol == "PEN"

    def test_php_symbol(self):
        assert CURRENCIES.PHP.symbol == "PHP"

    def test_pln_symbol(self):
        assert CURRENCIES.PLN.symbol == "PLN"

    def test_qar_symbol(self):
        assert CURRENCIES.QAR.symbol == "QAR"

    def test_ron_symbol(self):
        assert CURRENCIES.RON.symbol == "RON"

    def test_rsd_symbol(self):
        assert CURRENCIES.RSD.symbol == "RSD"

    def test_rub_symbol(self):
        assert CURRENCIES.RUB.symbol == "RUB"

    def test_sek_symbol(self):
        assert CURRENCIES.SEK.symbol == "SEK"

    def test_sgd_symbol(self):
        assert CURRENCIES.SGD.symbol == "SGD"

    def test_skk_symbol(self):
        assert CURRENCIES.SKK.symbol == "SKK"

    def test_try_symbol(self):
        assert CURRENCIES.TRY.symbol == "TRY"

    def test_uah_symbol(self):
        assert CURRENCIES.UAH.symbol == "UAH"

    def test_usd_symbol(self):
        assert CURRENCIES.USD.symbol == "$"

    def test_uyu_symbol(self):
        assert CURRENCIES.UYU.symbol == "UYU"

    def test_vnd_symbol(self):
        assert CURRENCIES.VND.symbol == "VND"

    def test_zar_symbol(self):
        assert CURRENCIES.ZAR.symbol == "ZAR"

    def test_zmk_symbol(self):
        assert CURRENCIES.ZMK.symbol == "ZMK"


class TestCurrencyRelatedCalendars(TestCase):
    def test_aed_related_calendars(self):
        assert CURRENCIES.AED.related_calendars == (CALENDARS.DUBAI,)

    def test_amd_related_calendars(self):
        assert CURRENCIES.AMD.related_calendars == tuple()

    def test_ars_related_calendars(self):
        assert CURRENCIES.ARS.related_calendars == tuple()

    def test_aud_related_calendars(self):
        assert CURRENCIES.AUD.related_calendars == (CALENDARS.SYDNEY,)

    def test_brl_related_calendars(self):
        assert CURRENCIES.BRL.related_calendars == tuple()

    def test_cad_related_calendars(self):
        assert CURRENCIES.CAD.related_calendars == (CALENDARS.TORONTO,)

    def test_chf_related_calendars(self):
        assert CURRENCIES.CHF.related_calendars == (CALENDARS.ZURICH,)

    def test_clp_related_calendars(self):
        assert CURRENCIES.CLP.related_calendars == tuple()

    def test_cnh_related_calendars(self):
        assert CURRENCIES.CNH.related_calendars == (CALENDARS.BEIJING,)

    def test_cny_related_calendars(self):
        assert CURRENCIES.CNY.related_calendars == (CALENDARS.SHANGHAI,)

    def test_cop_related_calendars(self):
        assert CURRENCIES.COP.related_calendars == tuple()

    def test_czk_related_calendars(self):
        assert CURRENCIES.CZK.related_calendars == (CALENDARS.PRAGUE,)

    def test_dkk_related_calendars(self):
        assert CURRENCIES.DKK.related_calendars == (CALENDARS.COPENHAGEN,)

    def test_eur_related_calendars(self):
        assert CURRENCIES.EUR.related_calendars == (CALENDARS.TARGET2,)

    def test_eek_related_calendars(self):
        assert CURRENCIES.EEK.related_calendars == tuple()

    def test_gbp_related_calendars(self):
        assert CURRENCIES.GBP.related_calendars == (CALENDARS.LONDON,)

    def test_gel_related_calendars(self):
        assert CURRENCIES.GEL.related_calendars == tuple()

    def test_hkd_related_calendars(self):
        assert CURRENCIES.HKD.related_calendars == (CALENDARS.HONG_KONG,)

    def test_huf_related_calendars(self):
        assert CURRENCIES.HUF.related_calendars == tuple()

    def test_idr_related_calendars(self):
        assert CURRENCIES.IDR.related_calendars == tuple()

    def test_inr_related_calendars(self):
        assert CURRENCIES.INR.related_calendars == tuple()

    def test_isk_related_calendars(self):
        assert CURRENCIES.ISK.related_calendars == (CALENDARS.REYKJAVIK,)

    def test_jpy_related_calendars(self):
        assert CURRENCIES.JPY.related_calendars == (CALENDARS.TOKYO,)

    def test_kgs_related_calendars(self):
        assert CURRENCIES.KGS.related_calendars == tuple()

    def test_krw_related_calendars(self):
        assert CURRENCIES.KRW.related_calendars == (CALENDARS.SEOUL,)

    def test_kzt_related_calendars(self):
        assert CURRENCIES.KZT.related_calendars == tuple()

    def test_mxn_related_calendars(self):
        assert CURRENCIES.MXN.related_calendars == tuple()

    def test_myr_related_calendars(self):
        assert CURRENCIES.MYR.related_calendars == tuple()

    def test_nok_related_calendars(self):
        assert CURRENCIES.NOK.related_calendars == (CALENDARS.OSLO,)

    def test_nzd_related_calendars(self):
        assert CURRENCIES.NZD.related_calendars == (
            CALENDARS.AUCKLAND,
            CALENDARS.WELLINGTON,
        )

    def test_ntd_related_calendars(self):
        assert CURRENCIES.NTD.related_calendars == tuple()

    def test_pen_related_calendars(self):
        assert CURRENCIES.PEN.related_calendars == tuple()

    def test_php_related_calendars(self):
        assert CURRENCIES.PHP.related_calendars == tuple()

    def test_pln_related_calendars(self):
        assert CURRENCIES.PLN.related_calendars == (CALENDARS.WARSAW,)

    def test_qar_related_calendars(self):
        assert CURRENCIES.QAR.related_calendars == (CALENDARS.DOHA,)

    def test_ron_related_calendars(self):
        assert CURRENCIES.RON.related_calendars == (CALENDARS.BUCHAREST,)

    def test_rsd_related_calendars(self):
        assert CURRENCIES.RSD.related_calendars == tuple()

    def test_rub_related_calendars(self):
        assert CURRENCIES.RUB.related_calendars == (CALENDARS.MOSCOW,)

    def test_sek_related_calendars(self):
        assert CURRENCIES.SEK.related_calendars == (CALENDARS.STOCKHOLM,)

    def test_sgd_related_calendars(self):
        assert CURRENCIES.SGD.related_calendars == (CALENDARS.SINGAPORE,)

    def test_skk_related_calendars(self):
        assert CURRENCIES.SKK.related_calendars == tuple()

    def test_try_related_calendars(self):
        assert CURRENCIES.TRY.related_calendars == (CALENDARS.ISTANBUL,)

    def test_uah_related_calendars(self):
        assert CURRENCIES.UAH.related_calendars == tuple()

    def test_usd_related_calendars(self):
        assert CURRENCIES.USD.related_calendars == (CALENDARS.NEW_YORK,)

    def test_uyu_related_calendars(self):
        assert CURRENCIES.UYU.related_calendars == tuple()

    def test_vnd_related_calendars(self):
        assert CURRENCIES.VND.related_calendars == tuple()

    def test_zar_related_calendars(self):
        assert CURRENCIES.ZAR.related_calendars == (CALENDARS.JOHANNESBURG,)

    def test_zmk_related_calendars(self):
        assert CURRENCIES.ZMK.related_calendars == tuple()


class TestCurrenciesOrder(LruCacheTestMixin, TestCase):
    def test_order(self):
        expected = [
            # G10
            CURRENCIES.USD,
            CURRENCIES.EUR,
            CURRENCIES.GBP,
            CURRENCIES.JPY,
            CURRENCIES.CHF,
            CURRENCIES.AUD,
            CURRENCIES.NZD,
            CURRENCIES.CAD,
            CURRENCIES.SEK,
            CURRENCIES.NOK,
            # others
            CURRENCIES.HKD,
            CURRENCIES.AED,
            CURRENCIES.AMD,
            CURRENCIES.ARS,
            CURRENCIES.BRL,
            CURRENCIES.CLP,
            CURRENCIES.CNH,
            CURRENCIES.CNY,
            CURRENCIES.COP,
            CURRENCIES.CZK,
            CURRENCIES.DKK,
            CURRENCIES.EEK,
            CURRENCIES.GEL,
            CURRENCIES.HUF,
            CURRENCIES.IDR,
            CURRENCIES.INR,
            CURRENCIES.ISK,
            CURRENCIES.KGS,
            CURRENCIES.KRW,
            CURRENCIES.KZT,
            CURRENCIES.MXN,
            CURRENCIES.MYR,
            CURRENCIES.NTD,
            CURRENCIES.PEN,
            CURRENCIES.PHP,
            CURRENCIES.PLN,
            CURRENCIES.QAR,
            CURRENCIES.RON,
            CURRENCIES.RSD,
            CURRENCIES.RUB,
            CURRENCIES.SGD,
            CURRENCIES.SKK,
            CURRENCIES.TRY,
            CURRENCIES.UAH,
            CURRENCIES.UYU,
            CURRENCIES.VND,
            CURRENCIES.ZAR,
            CURRENCIES.ZMK,
        ]
        assert list(CURRENCIES) == expected

    def test_django_choices(self):
        expected = (
            # G10
            (CURRENCIES.USD.value, CURRENCIES.USD.label),
            (CURRENCIES.EUR.value, CURRENCIES.EUR.label),
            (CURRENCIES.GBP.value, CURRENCIES.GBP.label),
            (CURRENCIES.JPY.value, CURRENCIES.JPY.label),
            (CURRENCIES.CHF.value, CURRENCIES.CHF.label),
            (CURRENCIES.AUD.value, CURRENCIES.AUD.label),
            (CURRENCIES.NZD.value, CURRENCIES.NZD.label),
            (CURRENCIES.CAD.value, CURRENCIES.CAD.label),
            (CURRENCIES.SEK.value, CURRENCIES.SEK.label),
            (CURRENCIES.NOK.value, CURRENCIES.NOK.label),
            # others
            (CURRENCIES.HKD.value, CURRENCIES.HKD.label),
            (CURRENCIES.AED.value, CURRENCIES.AED.label),
            (CURRENCIES.AMD.value, CURRENCIES.AMD.label),
            (CURRENCIES.ARS.value, CURRENCIES.ARS.label),
            (CURRENCIES.BRL.value, CURRENCIES.BRL.label),
            (CURRENCIES.CLP.value, CURRENCIES.CLP.label),
            (CURRENCIES.CNH.value, CURRENCIES.CNH.label),
            (CURRENCIES.CNY.value, CURRENCIES.CNY.label),
            (CURRENCIES.COP.value, CURRENCIES.COP.label),
            (CURRENCIES.CZK.value, CURRENCIES.CZK.label),
            (CURRENCIES.DKK.value, CURRENCIES.DKK.label),
            (CURRENCIES.EEK.value, CURRENCIES.EEK.label),
            (CURRENCIES.GEL.value, CURRENCIES.GEL.label),
            (CURRENCIES.HUF.value, CURRENCIES.HUF.label),
            (CURRENCIES.IDR.value, CURRENCIES.IDR.label),
            (CURRENCIES.INR.value, CURRENCIES.INR.label),
            (CURRENCIES.ISK.value, CURRENCIES.ISK.label),
            (CURRENCIES.KGS.value, CURRENCIES.KGS.label),
            (CURRENCIES.KRW.value, CURRENCIES.KRW.label),
            (CURRENCIES.KZT.value, CURRENCIES.KZT.label),
            (CURRENCIES.MXN.value, CURRENCIES.MXN.label),
            (CURRENCIES.MYR.value, CURRENCIES.MYR.label),
            (CURRENCIES.NTD.value, CURRENCIES.NTD.label),
            (CURRENCIES.PEN.value, CURRENCIES.PEN.label),
            (CURRENCIES.PHP.value, CURRENCIES.PHP.label),
            (CURRENCIES.PLN.value, CURRENCIES.PLN.label),
            (CURRENCIES.QAR.value, CURRENCIES.QAR.label),
            (CURRENCIES.RON.value, CURRENCIES.RON.label),
            (CURRENCIES.RSD.value, CURRENCIES.RSD.label),
            (CURRENCIES.RUB.value, CURRENCIES.RUB.label),
            (CURRENCIES.SGD.value, CURRENCIES.SGD.label),
            (CURRENCIES.SKK.value, CURRENCIES.SKK.label),
            (CURRENCIES.TRY.value, CURRENCIES.TRY.label),
            (CURRENCIES.UAH.value, CURRENCIES.UAH.label),
            (CURRENCIES.UYU.value, CURRENCIES.UYU.label),
            (CURRENCIES.VND.value, CURRENCIES.VND.label),
            (CURRENCIES.ZAR.value, CURRENCIES.ZAR.label),
            (CURRENCIES.ZMK.value, CURRENCIES.ZMK.label),
        )
        assert CURRENCIES.to_django_choices() == expected
        self.assert_has_lru_cache(CURRENCIES.to_django_choices)

    def test_django_choices_only_g10(self):
        expected = (
            # G10
            (CURRENCIES.USD.value, CURRENCIES.USD.label),
            (CURRENCIES.EUR.value, CURRENCIES.EUR.label),
            (CURRENCIES.GBP.value, CURRENCIES.GBP.label),
            (CURRENCIES.JPY.value, CURRENCIES.JPY.label),
            (CURRENCIES.CHF.value, CURRENCIES.CHF.label),
            (CURRENCIES.AUD.value, CURRENCIES.AUD.label),
            (CURRENCIES.NZD.value, CURRENCIES.NZD.label),
            (CURRENCIES.CAD.value, CURRENCIES.CAD.label),
            (CURRENCIES.SEK.value, CURRENCIES.SEK.label),
            (CURRENCIES.NOK.value, CURRENCIES.NOK.label),
        )
        assert CURRENCIES.to_django_choices(only_g10=True) == expected
        self.assert_has_lru_cache(CURRENCIES.to_django_choices)


class TestCurrencyCode(TestCase):
    def test_code_is_alias_for_value(self):
        constant = choice(list(CURRENCIES))
        assert constant.code == constant.value


class TestCurrenciesGetName(TestCase):
    def test_returns_name_of_given_currency_constant(self):
        constant = choice(list(CURRENCIES))
        assert CURRENCIES.get_name(constant) == constant.name

    def test_returns_name_of_given_currency_value(self):
        constant = choice(list(CURRENCIES))
        assert CURRENCIES.get_name(constant.value) == constant.name


class TestCurrencyComparisons(TestCase):
    def test_less_than_currency(self):
        assert CURRENCIES.USD < CURRENCIES.EUR
        assert CURRENCIES.EUR <= CURRENCIES.EUR

    def test_less_than_string(self):
        assert CURRENCIES.USD < CURRENCIES.EUR.value
        assert CURRENCIES.USD <= CURRENCIES.EUR.value
        assert CURRENCIES.USD.value < CURRENCIES.EUR
        assert CURRENCIES.EUR.value <= CURRENCIES.EUR

    def test_cannot_compare_to_other_objects(self):
        with self.assertRaises(TypeError):
            assert CURRENCIES.USD < 100
        with self.assertRaises(TypeError):
            assert CURRENCIES.USD >= 1

    def test_cannot_compare_to_non_currency_strings(self):
        with self.assertRaises(TypeError):
            assert CURRENCIES.USD < "FOO"
        with self.assertRaises(TypeError):
            assert CURRENCIES.USD >= "BAR"

    def test_greater_than_currency(self):
        assert CURRENCIES.EUR > CURRENCIES.USD
        assert CURRENCIES.EUR >= CURRENCIES.EUR

    def test_greater_than_string(self):
        assert CURRENCIES.EUR.value > CURRENCIES.USD
        assert CURRENCIES.EUR.value >= CURRENCIES.USD
        assert CURRENCIES.EUR > CURRENCIES.USD.value
        assert CURRENCIES.EUR >= CURRENCIES.EUR.value
