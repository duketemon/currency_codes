from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Currency:
    """Currency information

    Args:
        name (str): currency name
        code (str): three-letter code
        numeric_code (str): three-digit numeric code
            None for cryptos
        minor_units (int): shows the relationship between the minor unit and the currency itself
            None for commodities
    """

    name: str
    code: str
    numeric_code: Optional[str]
    minor_units: Optional[int]
