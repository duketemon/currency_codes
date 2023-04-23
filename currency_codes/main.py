from currency_codes.assets.commodity import get_commodity_currencies
from currency_codes.assets.crypto import get_crypto_currencies
from currency_codes.assets.fiat import get_fiat_currencies
from currency_codes.assets.other import get_other_currencies
from currency_codes.exceptions import CurrencyNotFoundError
from currency_codes.models import Currency


def get_all_currencies() -> list[Currency]:
    fiat = get_fiat_currencies()
    crypto = get_crypto_currencies()
    commodity = get_commodity_currencies()
    other = get_other_currencies()
    return fiat + crypto + commodity + other


def get_currency_by_code(code: str, case_sensitive: bool = False) -> Currency:
    """Provides a currency by a code

    Args:
        code (str): country code
        case_sensitive (bool): determines whether filters will be treated as case-sensitive for a given code

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


currencies: list[Currency] = get_all_currencies()
