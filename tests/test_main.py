from typing import Iterable

import pytest

from currency_codes.exceptions import CurrencyNotFoundError
from currency_codes.main import (
    get_all_currencies,
    get_currency_by_code,
    get_currency_by_numeric_code,
)

crypto_test_cases = (
    # name, code, minor units
    ("Solana", "SOL", 9),
    ("Binance Coin", "BNB", 18),
    ("Algorand", "ALGO", 6),
    ("Siacoin", "SC", 24),
)


fiat_test_cases = (
    # name, code, numeric_code, minor_units
    ("Euro", "EUR", "978", 2),
    ("Bahraini Dinar", "BHD", "048", 3),
    ("Chilean Peso", "CLP", "152", 0),
)

commodity_test_cases = (
    # name, code, numeric_code
    ("Palladium", "XPD", "964"),
    ("Platinum", "XPT", "962"),
    ("Gold", "XAU", "959"),
    ("Silver", "XAG", "961"),
)

other_test_cases = (
    # name, code, numeric_code
    ("Uruguay Peso en Unidades Indexadas (UI)", "UYI", "940", 0),
    ("WIR Euro", "CHE", "947", 2),
    ("Unidad de Fomento", "CLF", "990", 4),
)


def test_get_all_currencies() -> None:
    # When
    currencies = get_all_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 268


def test_get_currency_by_code_when_currency_is_not_found() -> None:
    # Given
    currency_code = "non-existed-currency-code"

    # When
    with pytest.raises(CurrencyNotFoundError) as err_msg:
        get_currency_by_code(currency_code)

        # Then
        assert "code" in err_msg


def test_get_currency_by_code_when_currency_is_not_found_because_of_case_sensitivity() -> None:
    # Given
    currency_code = "bTc"

    # When
    with pytest.raises(CurrencyNotFoundError) as err_msg:
        get_currency_by_code(currency_code, case_sensitive=True)

        # Then
        assert "code" in err_msg


@pytest.mark.parametrize(
    ids=(c[0] for c in crypto_test_cases),
    argvalues=crypto_test_cases,
    argnames="name, code, minor_units",
)
def test_get_currency_by_code_when_currency_is_crypto(name, code, minor_units) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.minor_units == minor_units
    assert currency.numeric_code is None


@pytest.mark.parametrize(
    ids=(c[0] for c in fiat_test_cases),
    argvalues=fiat_test_cases,
    argnames="name, code, numeric_code, minor_units",
)
def test_get_currency_by_code_when_currency_is_fiat(name, code, numeric_code, minor_units) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units


@pytest.mark.parametrize(
    ids=(c[0] for c in commodity_test_cases),
    argvalues=commodity_test_cases,
    argnames="name, code, numeric_code",
)
def test_get_currency_by_code_when_currency_is_commodity(name, code, numeric_code) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units is None


@pytest.mark.parametrize(
    ids=(c[0] for c in other_test_cases),
    argvalues=other_test_cases,
    argnames="name, code, numeric_code, minor_units",
)
def test_get_currency_by_code_when_currency_is_other(
    name, code, numeric_code, minor_units
) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units


def test_get_currency_by_numeric_code_when_currency_is_not_found() -> None:
    # Given
    currency_numeric_code = "non-existed-currency-numeric-code"

    # When
    with pytest.raises(CurrencyNotFoundError) as err_msg:
        get_currency_by_numeric_code(currency_numeric_code)

        # Then
        assert "numeric code" in err_msg


@pytest.mark.parametrize(
    ids=(c[0] for c in fiat_test_cases),
    argvalues=fiat_test_cases,
    argnames="name, code, numeric_code, minor_units",
)
def test_get_currency_by_numeric_code_when_currency_is_fiat(
    name, code, numeric_code, minor_units
) -> None:
    # When
    currency = get_currency_by_numeric_code(numeric_code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units


@pytest.mark.parametrize(
    ids=(c[0] for c in commodity_test_cases),
    argvalues=commodity_test_cases,
    argnames="name, code, numeric_code",
)
def test_get_currency_by_numeric_code_when_currency_is_commodity(name, code, numeric_code) -> None:
    # When
    currency = get_currency_by_numeric_code(numeric_code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units is None


@pytest.mark.parametrize(
    ids=(c[0] for c in other_test_cases),
    argvalues=other_test_cases,
    argnames="name, code, numeric_code, minor_units",
)
def test_get_currency_by_numeric_code_when_currency_is_other(
    name, code, numeric_code, minor_units
) -> None:
    # When
    currency = get_currency_by_numeric_code(numeric_code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units
