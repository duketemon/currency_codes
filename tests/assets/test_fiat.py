from typing import Iterable

from currency_codes.assets.fiat import get_fiat_currencies


def test_get_fiat_currencies_when_function_returns_all_currencies() -> None:
    # When
    currencies = get_fiat_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 159
