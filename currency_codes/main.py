from typing import List

from currency_codes.assets.crypto import get_crypto_currencies
from currency_codes.assets.fiat import get_fiat_currencies
from currency_codes.assets.other import get_other_currencies
from currency_codes.exceptions import CurrencyNotFoundError
from currency_codes.models import Currency


def get_all_currencies() -> List[Currency]:
    """Provides a list of all currencies

    Returns:
        List of Currency: list of all currencies
    """

    fiat = get_fiat_currencies()
    crypto = get_crypto_currencies()
    other = get_other_currencies()
    return fiat + crypto + other


def get_currency_by_code(code: str, case_sensitive: bool = False) -> Currency:
    """Provides a currency by a code

    Args:
        code (str): country code
        case_sensitive (bool): determines whether filters will be treated as a case-sensitive
            for a given currency code

    Returns:
        Currency: a corresponding currency

    Raises:
        CurrencyNotFoundError: if there's no corresponding currency
    """

    if not case_sensitive:
        code = code.upper()
    for currency in currencies:
        if currency.code == code:
            return currency
    raise CurrencyNotFoundError("code", code)


def get_currency_by_numeric_code(numeric_code: str) -> Currency:
    """Provides a currency by a code

    Args:
        numeric_code (str): numeric code

    Returns:
        Currency: a corresponding currency

    Raises:
        CurrencyNotFoundError: if there's no corresponding currency
    """

    for currency in currencies:
        if currency.numeric_code == numeric_code:
            return currency
    raise CurrencyNotFoundError("numeric code", numeric_code)


currencies: List[Currency] = get_all_currencies()
