from typing import Iterable

from currency_codes.assets.other import get_other_currencies


def test_get_other_currencies() -> None:
    # When
    currencies = get_other_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 23
