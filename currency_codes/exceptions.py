class CurrencyNotFoundError(ValueError):
    """Raises then no currency have been found

    Args:
        property_name (str): name of currency's property
        given_value (str): the value used passed to a function
    """

    def __init__(self, property_name: str, given_value: str) -> None:
        full_message = f"No currency found when {property_name} equals {given_value}"
        super().__init__(full_message)
