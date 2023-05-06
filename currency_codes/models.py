from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Currency:
    """Currency information

    Args:
        name (str): currency name
        code (str): three-letter code
            None if a currency never went public
        state (str): what current state of the currency
        launched_in (int): currency launch year
        numeric_code (str): three-digit numeric code
        minor_units (int): shows the relationship between the minor unit and the currency itself
    """

    name: str
    code: Optional[str]
    minor_units: Optional[int]
    state: str = "active"
    launched_in: Optional[int] = None
    numeric_code: Optional[str] = None
