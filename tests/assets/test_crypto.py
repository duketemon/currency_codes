from typing import Iterable

from currency_codes.assets.crypto import get_crypto_currencies


def test_get_crypto_currencies() -> None:
    # When
    currencies = get_crypto_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 103


def test_when_no_crypto_currencies_have_numeric_code(crypto_currencies) -> None:
    for currency in crypto_currencies:
        assert currency.numeric_code is None
