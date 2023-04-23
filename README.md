## Description
Comprehensive Python package for managing currency codes across different types of assets. Having all the currency codes in one package can simplify the development process for applications that involve multiple currencies and assets. This package could also help to ensure consistency and accuracy in managing currency codes across different parts of an application  
The package provides currency codes for different types of assets. Such as 
- fiat (US dollar, UAE Dirham, ...)
- crypto (Bitcoin, Solana, ...)
- commodity (Palladium, Gold, ...)
- others (WIR Franc, CFP Franc, ...) 

## Sources
 - [Coinmarketcap website](https://coinmarketcap.com) for crypto
 - [ISO's website](https://www.iso.org/iso-4217-currency-codes.html) for rest

## Installation
Install the package with the following command:
```shell
pip install currency_codes
```

## How to use the package?
### Get a currency info by a currency code
You can get any currency info using the snippet below
```python
from currency_codes import get_currency_by_code, Currency

currency_code: str = "EUR"
currency: Currency = get_currency_by_code(currency_code)
```
if the package doesn't know a currency code you can raise a PR to extend the knowledge base but for now the `CurrencyNotFoundError` will be raised.

```python
from currency_codes import get_currency_by_code, CurrencyNotFoundError

# non-existent currency code
currency_code: str = "EUR000"
try:
    get_currency_by_code(currency_code)
except CurrencyNotFoundError:
    print("Non-existent code have been used")
```


### Get a currency info by a currency numeric code
To get a currency info you can also use the numeric code like in the example below
```python
from currency_codes import get_currency_by_numeric_code, Currency

# Euro has 978 numeric code
currency_numeric_code: str = "978"
currency: Currency = get_currency_by_numeric_code(currency_numeric_code)
```
if the package doesn't know a currency numeric code you can raise a PR to extend the knowledge base but for now the `CurrencyNotFoundError` will be raised.

```python
from currency_codes import get_currency_by_numeric_code, CurrencyNotFoundError

# non-existent currency numeric code
currency_numeric_code: str = "00000000"
try:
    get_currency_by_numeric_code(currency_numeric_code)
except CurrencyNotFoundError:
    print("Non-existent numeric code have been used")
```


### Get the list of all currencies
If you want to get information about all currencies, you can use `get_all_currencies` function
```python
from currency_codes import get_all_currencies, Currency

currencies: list[Currency] = get_all_currencies()
```

### Get the list of fiat currencies
If you want to get information only about fiat currencies, you can use `get_fiat_currencies` function
```python
from currency_codes import get_fiat_currencies, Currency

fiat_currencies: list[Currency] = get_fiat_currencies()
```

### Get the list of crypto currencies
If you want to get information only about crypto currencies, you can use `get_crypto_currencies` function
```python
from currency_codes import get_crypto_currencies, Currency

crypto_currencies: list[Currency] = get_crypto_currencies()
```

### Get the list of commodity currencies
If you want to get information only about commodity currencies, you can use `get_commodity_currencies` function
```python
from currency_codes import get_commodity_currencies, Currency

commodity_currencies: list[Currency] = get_commodity_currencies()
```

### Get the list of other currencies
If you want to get information only about other currencies, you can use `get_other_currencies` function
```python
from currency_codes import get_other_currencies, Currency

other_currencies: list[Currency] = get_other_currencies()
```
