from typing import Iterable

import pytest

from currency_codes.assets.commodity import get_commodity_currencies
from currency_codes.assets.crypto import get_crypto_currencies
from currency_codes.assets.fiat import get_fiat_currencies
from currency_codes.assets.other import get_other_currencies
from currency_codes.models import Currency


@pytest.fixture
def fiat_currencies() -> Iterable[Currency]:
    return get_fiat_currencies()


@pytest.fixture
def crypto_currencies() -> Iterable[Currency]:
    return get_crypto_currencies()


@pytest.fixture
def commodity_currencies() -> Iterable[Currency]:
    return get_commodity_currencies()


@pytest.fixture
def other_currencies() -> Iterable[Currency]:
    return get_other_currencies()
