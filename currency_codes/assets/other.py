from typing import List

from currency_codes.models import Currency


def get_other_currencies() -> List[Currency]:
    return _other_currencies


_other_currencies: List[Currency] = [
    Currency(name="Sucre", code="XSU", numeric_code="994", minor_units=None),
    Currency(name="CFP Franc", code="XPF", numeric_code="953", minor_units=0),
    Currency(name="CFA Franc BEAC", code="XAF", numeric_code="950", minor_units=0),
    Currency(name="US Dollar (Next day)", code="USN", numeric_code="997", minor_units=2),
    Currency(name="Unidad Previsional", code="UYW", numeric_code="927", minor_units=4),
    Currency(name="Mvdol", code="BOV", numeric_code="984", minor_units=2),
    Currency(name="Unidad de Fomento", code="CLF", numeric_code="990", minor_units=4),
    Currency(name="Unidad de Valor Real", code="COU", numeric_code="970", minor_units=2),
    Currency(name="SDR (Special Drawing Right)", code="XDR", numeric_code="960", minor_units=None),
    Currency(name="ADB Unit of Account", code="XUA", numeric_code="965", minor_units=None),
    Currency(name="WIR Euro", code="CHE", numeric_code="947", minor_units=2),
    Currency(name="WIR Franc", code="CHW", numeric_code="948", minor_units=2),
    Currency(
        name="Uruguay Peso en Unidades Indexadas (UI)",
        code="UYI",
        numeric_code="940",
        minor_units=0,
    ),
    Currency(
        name="Bond Markets Unit European Composite Unit (EURCO)",
        code="XBA",
        numeric_code="955",
        minor_units=None,
    ),
    Currency(
        name="Bond Markets Unit European Monetary Unit (E.M.U.-6)",
        code="XBB",
        numeric_code="956",
        minor_units=None,
    ),
    Currency(
        name="Bond Markets Unit European Unit of Account 9 (E.U.A.-9)",
        code="XBC",
        numeric_code="957",
        minor_units=None,
    ),
    Currency(
        name="Bond Markets Unit European Unit of Account 17 (E.U.A.-17)",
        code="XBD",
        numeric_code="958",
        minor_units=None,
    ),
    Currency(
        name="Mexican Unidad de Inversion (UDI)",
        code="MXV",
        numeric_code="979",
        minor_units=2,
    ),
    Currency(
        name="The codes assigned for transactions where no currency is involved",
        code="XXX",
        numeric_code="999",
        minor_units=None,
    ),
]
