from random import choice
from unittest import TestCase

from origin_common.constants import CURRENCIES, DAY_COUNTS


class TestDayCountValues(TestCase):
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


class TestDayCountLabels(TestCase):
    def test_aed_label(self):
        assert CURRENCIES.AED.label == "UAE Dirham (AED)"

    def test_amd_label(self):
        assert CURRENCIES.AMD.label == "Armenian Dram (AMD)"

    def test_ars_label(self):
        assert CURRENCIES.ARS.label == "Argentine Peso (ARS)"

    def test_aud_label(self):
        assert CURRENCIES.AUD.label == "Australian Dollar (AUD)"

    def test_brl_label(self):
        assert CURRENCIES.BRL.label == "Brazilian Real (BRL)"

    def test_cad_label(self):
        assert CURRENCIES.CAD.label == "Canadian Dollar (CAD)"

    def test_chf_label(self):
        assert CURRENCIES.CHF.label == "Swiss Franc (CHF)"

    def test_clp_label(self):
        assert CURRENCIES.CLP.label == "Chilean peso (CLP)"

    def test_cnh_label(self):
        assert CURRENCIES.CNH.label == "Yuan Renminbi (Offshore) (CNH)"

    def test_cny_label(self):
        assert CURRENCIES.CNY.label == "Yuan Renminbi (CNY)"

    def test_cop_label(self):
        assert CURRENCIES.COP.label == "Colombian peso (COP)"

    def test_czk_label(self):
        assert CURRENCIES.CZK.label == "Czech Koruna (CZK)"

    def test_dkk_label(self):
        assert CURRENCIES.DKK.label == "Danish Krone (DKK)"

    def test_eur_label(self):
        assert CURRENCIES.EUR.label == "Euro (EUR)"

    def test_eek_label(self):
        assert CURRENCIES.EEK.label == "Estonian Kroon (EEK)"

    def test_gbp_label(self):
        assert CURRENCIES.GBP.label == "Pound Sterling (GBP)"

    def test_gel_label(self):
        assert CURRENCIES.GEL.label == "Lari (GEL)"

    def test_hkd_label(self):
        assert CURRENCIES.HKD.label == "Hong Kong Dollar (HKD)"

    def test_huf_label(self):
        assert CURRENCIES.HUF.label == "Forint (HUF)"

    def test_idr_label(self):
        assert CURRENCIES.IDR.label == "Rupiah (IDR)"

    def test_inr_label(self):
        assert CURRENCIES.INR.label == "Indian Rupee (INR)"

    def test_isk_label(self):
        assert CURRENCIES.ISK.label == "Iceland Krona (ISK)"

    def test_jpy_label(self):
        assert CURRENCIES.JPY.label == "Yen (JPY)"

    def test_kgs_label(self):
        assert CURRENCIES.KGS.label == "Som (KGS)"

    def test_krw_label(self):
        assert CURRENCIES.KRW.label == "Won (KRW)"

    def test_kzt_label(self):
        assert CURRENCIES.KZT.label == "Tenge (KZT)"

    def test_mxn_label(self):
        assert CURRENCIES.MXN.label == "Mexican peso (MXN)"

    def test_myr_label(self):
        assert CURRENCIES.MYR.label == "Malaysian Ringgit (MYR)"

    def test_nok_label(self):
        assert CURRENCIES.NOK.label == "Norwegian Krone (NOK)"

    def test_nzd_label(self):
        assert CURRENCIES.NZD.label == "New Zealand Dollar (NZD)"

    def test_ntd_label(self):
        assert CURRENCIES.NTD.label == "New Taiwan dollar (NTD)"

    def test_pen_label(self):
        assert CURRENCIES.PEN.label == "Peruvian Sol (PEN)"

    def test_php_label(self):
        assert CURRENCIES.PHP.label == "Philippine Peso (PHP)"

    def test_pln_label(self):
        assert CURRENCIES.PLN.label == "Zloty (PLN)"

    def test_qar_label(self):
        assert CURRENCIES.QAR.label == "Qatari Rial (QAR)"

    def test_ron_label(self):
        assert CURRENCIES.RON.label == "New Leu (RON)"

    def test_rsd_label(self):
        assert CURRENCIES.RSD.label == "Serbian Dinar (RSD)"

    def test_rub_label(self):
        assert CURRENCIES.RUB.label == "Russian Ruble (RUB)"

    def test_sek_label(self):
        assert CURRENCIES.SEK.label == "Swedish Krona (SEK)"

    def test_sgd_label(self):
        assert CURRENCIES.SGD.label == "Singapore Dollar (SGD)"

    def test_skk_label(self):
        assert CURRENCIES.SKK.label == "Slovak Koruna (SKK)"

    def test_try_label(self):
        assert CURRENCIES.TRY.label == "Turkish Lira (TRY)"

    def test_uah_label(self):
        assert CURRENCIES.UAH.label == "Hryvnia (UAH)"

    def test_usd_label(self):
        assert CURRENCIES.USD.label == "US Dollar (USD)"

    def test_uyu_label(self):
        assert CURRENCIES.UYU.label == "Uruguayan peso (UYU)"

    def test_vnd_label(self):
        assert CURRENCIES.VND.label == "Dong (VND)"

    def test_zar_label(self):
        assert CURRENCIES.ZAR.label == "Rand (ZAR)"

    def test_zmk_label(self):
        assert CURRENCIES.ZMK.label == "Zambian Kwacha (ZMK)"


class TestDayCountSymbols(TestCase):
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


class TestCurrenciesOrder(TestCase):
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


class TestCurrencyCode(TestCase):
    def test_code_is_alias_for_value(self):
        constant = choice(list(CURRENCIES))
        assert constant.code == constant.value
