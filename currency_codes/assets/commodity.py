from typing import List

from currency_codes.models import Currency


def get_commodity_currencies() -> List[Currency]:
    """Provides a list of commodity currencies

    Returns:
        List of Currency: list of commodity currencies
    """

    return _commodity_currencies


_commodity_currencies: List[Currency] = [
    Currency(name="Palladium", code="XPD", numeric_code="964", minor_units=None),
    Currency(name="Platinum", code="XPT", numeric_code="962", minor_units=None),
    Currency(name="Gold", code="XAU", numeric_code="959", minor_units=None),
    Currency(name="Silver", code="XAG", numeric_code="961", minor_units=None),
]
