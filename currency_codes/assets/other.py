from typing import List

from currency_codes.models import Currency


def get_other_currencies() -> List[Currency]:
    """Provides a list of other currencies

    Returns:
        List of Currency: list of other currencies
    """

    return _other_currencies


_other_currencies: List[Currency] = [
    Currency(
        name="Palladium",
        code="XPD",
        state="active",
        numeric_code="964",
        minor_units=None,
    ),
    Currency(
        name="Platinum",
        code="XPT",
        state="active",
        numeric_code="962",
        minor_units=None,
    ),
    Currency(
        name="Gold",
        code="XAU",
        state="active",
        numeric_code="959",
        minor_units=None,
    ),
    Currency(
        name="Silver",
        code="XAG",
        state="active",
        numeric_code="961",
        minor_units=None,
    ),
    Currency(
        name="Sucre",
        code="XSU",
        state="active",
        numeric_code="994",
        minor_units=2,
        launched_in=2009,
    ),
    Currency(
        name="SDR (Special Drawing Right)",
        code="XDR",
        state="active",
        numeric_code="960",
        minor_units=None,
        launched_in=1969,
    ),
    Currency(
        name="ADB Unit of Account",
        code="XUA",
        state="active",
        numeric_code="965",
        minor_units=None,
        launched_in=1969,
    ),
    Currency(
        name="Bond Markets Unit European Composite Unit (EURCO)",
        code="XBA",
        state="active",
        numeric_code="955",
        minor_units=None,
        launched_in=1979,
    ),
    Currency(
        name="Bond Markets Unit European Monetary Unit (E.M.U.-6)",
        code="XBB",
        state="active",
        numeric_code="956",
        minor_units=None,
        launched_in=1979,
    ),
    Currency(
        name="Bond Markets Unit European Unit of Account 9 (E.U.A.-9)",
        code="XBC",
        state="active",
        numeric_code="957",
        minor_units=None,
        launched_in=1979,
    ),
    Currency(
        name="Bond Markets Unit European Unit of Account 17 (E.U.A.-17)",
        code="XBD",
        state="active",
        numeric_code="958",
        minor_units=None,
        launched_in=1979,
    ),
    Currency(
        name="The codes assigned for transactions where no currency is involved",
        code="XXX",
        state="active",
        numeric_code="999",
        minor_units=None,
    ),
    Currency(
        name="Mexican Unidad de Inversion (UDI)",
        code="MXV",
        state="active",
        numeric_code="979",
        minor_units=2,
        launched_in=1993,
    ),
    Currency(
        name="US Dollar (Next day)",
        code="USN",
        state="active",
        numeric_code="997",
        minor_units=2,
    ),
    Currency(
        name="Unidad Previsional",
        code="UYW",
        state="active",
        numeric_code="927",
        minor_units=4,
    ),
    Currency(
        name="WIR Euro",
        code="CHE",
        state="active",
        numeric_code="947",
        minor_units=2,
        launched_in=2004,
    ),
    Currency(
        name="WIR Franc",
        code="CHW",
        state="active",
        numeric_code="948",
        minor_units=2,
        launched_in=2004,
    ),
    Currency(
        name="Uruguay Peso en Unidades Indexadas (UI)",
        code="UYI",
        state="active",
        numeric_code="940",
        minor_units=0,
        launched_in=1993,
    ),
    Currency(
        name="MVDOL",
        code="BOV",
        state="active",
        minor_units=2,
        numeric_code="984",
        launched_in=1993,
    ),
    Currency(
        name="Unidad de Fomento",
        code="CLF",
        state="active",
        minor_units=4,
        numeric_code="990",
        launched_in=1967,
    ),
    Currency(
        name="Unidad de Valor Real",
        code="COU",
        state="active",
        minor_units=2,
        numeric_code="970",
        launched_in=1994,
    ),
]
