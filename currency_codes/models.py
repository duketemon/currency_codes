from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Currency:
    """Currency information

    Args:
        name (str): currency name
        code (str): three-letter code
            None if a currency never went public
        numeric_code (str): three-digit numeric code
        minor_units (int): shows the relationship between the minor unit and the currency itself
    """

    name: str
    code: Optional[str]
    numeric_code: Optional[str]
    minor_units: Optional[int]
