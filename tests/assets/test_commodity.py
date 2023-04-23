from typing import Iterable

from currency_codes.assets.commodity import get_commodity_currencies


def test_get_commodity_currencies() -> None:
    # When
    currencies = get_commodity_currencies()

    # Then
    assert isinstance(currencies, Iterable)
    assert len(currencies) == 4


def test_when_no_commodities_have_minor_units(commodity_currencies) -> None:
    for currency in commodity_currencies:
        assert currency.minor_units is None
