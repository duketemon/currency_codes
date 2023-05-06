from typing import Iterable

from currency_codes.models import Currency


def assert_no_code_duplicates_found(currencies: Iterable[Currency]) -> None:
    codes = set()
    for currency in currencies:
        if currency.code is not None:
            assert currency.code not in codes
            codes.add(currency.code)


def test_when_no_code_duplicates_found_for_cryptos(crypto_currencies) -> None:
    assert_no_code_duplicates_found(crypto_currencies)


def test_when_no_code_duplicates_found_for_fiats(fiat_currencies) -> None:
    assert_no_code_duplicates_found(fiat_currencies)


def test_when_no_code_duplicates_found_for_others(other_currencies) -> None:
    assert_no_code_duplicates_found(other_currencies)


def assert_no_numeric_code_duplicates_found(currencies: Iterable[Currency]) -> None:
    codes = set()
    for currency in currencies:
        assert currency.numeric_code not in codes
        codes.add(currency.numeric_code)


def test_when_no_numeric_code_duplicates_found_for_fiats(fiat_currencies) -> None:
    assert_no_numeric_code_duplicates_found(fiat_currencies)


def assert_no_name_duplicates_found(currencies: Iterable[Currency]) -> None:
    names = set()
    for currency in currencies:
        if currency.name is not None:
            assert currency.name not in names
            names.add(currency.name)


def test_when_no_name_duplicates_found_for_others(other_currencies) -> None:
    assert_no_name_duplicates_found(other_currencies)
