from typing import Iterable

import pytest

from currency_codes.exceptions import CurrencyNotFoundError
from currency_codes.main import (
    get_all_currencies,
    get_currency_by_code,
    get_currency_by_numeric_code,
)

crypto_test_cases = (
    # name, code, state, minor units, launched in
    ("Solana", "SOL", "active", 8, 2020),
    ("Binance Coin", "BNB", "active", 18, 2017),
    ("Algorand", "ALGO", "active", 6, 2019),
)


fiat_test_cases = (
    # name, code, numeric_code, state, minor_units, launched in
    ("Euro", "EUR", "978", "active", 2, 1999),
    ("Bahraini Dinar", "BHD", "048", "active", 3, 1965),
    ("Chilean Peso", "CLP", "152", "active", 0, 1925),
)


other_test_cases = (
    # name, code, state, numeric_code, launched in
    ("Palladium", "XPD", "964", "active", None, None),
    ("Silver", "XAG", "961", "active", None, None),
    ("Uruguay Peso en Unidades Indexadas (UI)", "UYI", "940", "active", 0, 1993),
    ("WIR Euro", "CHE", "947", "active", 2, 2004),
    ("Unidad de Fomento", "CLF", "990", "active", 4, 1967),
)


def test_get_all_currencies() -> None:
    # When
    currencies = get_all_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 283


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
    argnames="name, code, state, minor_units, launched_in",
)
def test_get_currency_by_code_when_currency_is_crypto(
    name, code, state, minor_units, launched_in
) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.state == state
    assert currency.launched_in == launched_in
    assert currency.minor_units == minor_units
    assert currency.numeric_code is None


@pytest.mark.parametrize(
    ids=(c[0] for c in fiat_test_cases),
    argvalues=fiat_test_cases,
    argnames="name, code, numeric_code, state, minor_units, launched_in",
)
def test_get_currency_by_code_when_currency_is_fiat(
    name, code, numeric_code, state, minor_units, launched_in
) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.state == state
    assert currency.launched_in == launched_in
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units


@pytest.mark.parametrize(
    ids=(c[0] for c in other_test_cases),
    argvalues=other_test_cases,
    argnames="name, code, numeric_code, state, minor_units, launched_in",
)
def test_get_currency_by_code_when_currency_is_other(
    name, code, numeric_code, state, minor_units, launched_in
) -> None:
    # When
    currency = get_currency_by_code(code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.state == state
    assert currency.launched_in == launched_in
    assert currency.numeric_code == numeric_code
    if minor_units is None:
        assert currency.minor_units is minor_units
    else:
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
    argnames="name, code, numeric_code, state, minor_units, launched_in",
)
def test_get_currency_by_numeric_code_when_currency_is_fiat(
    name, code, numeric_code, state, minor_units, launched_in
) -> None:
    # When
    currency = get_currency_by_numeric_code(numeric_code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.state == state
    assert currency.launched_in == launched_in
    assert currency.numeric_code == numeric_code
    assert currency.minor_units == minor_units


@pytest.mark.parametrize(
    ids=(c[0] for c in other_test_cases),
    argvalues=other_test_cases,
    argnames="name, code, numeric_code, state, minor_units, launched_in",
)
def test_get_currency_by_numeric_code_when_currency_is_other(
    name, code, numeric_code, state, minor_units, launched_in
) -> None:
    # When
    currency = get_currency_by_numeric_code(numeric_code)

    # Then
    assert currency.name == name
    assert currency.code == code
    assert currency.state == state
    assert currency.launched_in == launched_in
    assert currency.numeric_code == numeric_code
    if minor_units is None:
        assert currency.minor_units is minor_units
    else:
        assert currency.minor_units == minor_units
