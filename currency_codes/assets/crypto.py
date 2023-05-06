from typing import List

from currency_codes.models import Currency


def get_crypto_currencies() -> List[Currency]:
    """Provides a list of crypto currencies

    Returns:
        List of Currency: list of crypto currencies
    """

    return _crypto_currencies


_crypto_currencies: List[Currency] = [
    # launched in 2009
    ## active
    Currency(name="Bitcoin", code="BTC", launched_in=2009, state="active", minor_units=8),
    Currency(name="Bitcoin", code="XBT", launched_in=2009, state="active", minor_units=8),
    # launched in 2011
    ## active
    Currency(name="Litecoin", code="LTC", launched_in=2011, state="active", minor_units=8),
    Currency(name="Namecoin", code="NMC", launched_in=2011, state="active", minor_units=8),
    # launched in 2012
    ## active
    Currency(name="Peercoin", code="PPC", launched_in=2012, state="active", minor_units=3),
    Currency(name="Ripple", code="XRP", launched_in=2012, state="active", minor_units=6),
    # launched in 2013
    ## active
    Currency(name="Dogecoin", code="DOGE", launched_in=2013, state="active", minor_units=8),
    Currency(name="Gridcoin", code="GRC", launched_in=2013, state="active", minor_units=8),
    Currency(name="Primecoin", code="XPM", launched_in=2013, state="active", minor_units=8),
    Currency(name="OMG Network", code="OMG", launched_in=2013, state="active", minor_units=18),
    Currency(name="Nxt", code="NXT", launched_in=2013, state="active", minor_units=6),
    # launched in 2014
    ## active
    Currency(name="Auroracoin", code="AUR", launched_in=2014, state="active", minor_units=6),
    Currency(name="Bluzelle", code="BLZ", launched_in=2014, state="active", minor_units=18),
    Currency(name="Dash", code="DASH", launched_in=2014, state="active", minor_units=8),
    Currency(name="Neo", code="NEO", launched_in=2014, state="active", minor_units=8),
    Currency(name="MazaCoin", code="MZC", launched_in=2014, state="active", minor_units=2),
    Currency(name="Monero", code="XMR", launched_in=2014, state="active", minor_units=12),
    Currency(name="Titcoin", code="TIT", launched_in=2014, state="active", minor_units=8),
    Currency(name="Verge", code="XVG", launched_in=2014, state="active", minor_units=8),
    Currency(name="Vertcoin", code="VTC", launched_in=2014, state="active", minor_units=8),
    Currency(name="Stellar", code="XLM", launched_in=2014, state="active", minor_units=7),
    ## inactive
    Currency(name="Coinye", code=None, launched_in=2014, state="inactive", minor_units=None),
    # launched in 2015
    ## active
    Currency(name="Ethereum", code="ETH", launched_in=2015, state="active", minor_units=18),
    Currency(
        name="Ethereum Classic", code="ETC", launched_in=2015, state="active", minor_units=18
    ),
    Currency(name="Nano", code="XNO", launched_in=2015, state="active", minor_units=30),
    Currency(name="Tether", code="USDT", launched_in=2015, state="active", minor_units=2),
    ## inactive
    Currency(name="OneCoin", code=None, launched_in=2015, state="inactive", minor_units=None),
    # launched in 2016
    ## active
    Currency(name="Firo", code="FIRO", launched_in=2016, state="active", minor_units=8),
    Currency(name="Zcash", code="ZEC", launched_in=2016, state="active", minor_units=8),
    # launched in 2017
    ## active
    Currency(name="0x", code="ZRX", launched_in=2017, state="active", minor_units=18),
    Currency(name="Aave", code="AAVE", launched_in=2017, state="active", minor_units=18),
    Currency(name="Bancor", code="BNT", launched_in=2017, state="active", minor_units=18),
    Currency(
        name="Basic Attention Token", code="BAT", launched_in=2017, state="active", minor_units=18
    ),
    Currency(name="Bitcoin Cash", code="BCH", launched_in=2017, state="active", minor_units=8),
    Currency(name="Bitcoin Gold", code="BTG", launched_in=2017, state="active", minor_units=8),
    Currency(name="Binance Coin", code="BNB", launched_in=2017, state="active", minor_units=18),
    Currency(name="Cardano", code="ADA", launched_in=2017, state="active", minor_units=6),
    Currency(name="COTI", code="COTI", launched_in=2017, state="active", minor_units=12),
    Currency(name="Chainlink", code="LINK", launched_in=2017, state="active", minor_units=8),
    Currency(name="Decentraland", code="MANA", launched_in=2017, state="active", minor_units=8),
    Currency(
        name="Ethereum Name Service", code="ENS", launched_in=2017, state="active", minor_units=8
    ),
    Currency(name="EOS.IO", code="EOS", launched_in=2017, state="active", minor_units=8),
    Currency(name="Enjin", code="ENJ", launched_in=2017, state="active", minor_units=8),
    Currency(name="Fetch.ai", code="FET", launched_in=2017, state="active", minor_units=9),
    Currency(name="Numeraire", code="NMR", launched_in=2017, state="active", minor_units=8),
    Currency(name="Melon", code="MLN", launched_in=2017, state="active", minor_units=8),
    Currency(name="Polygon", code="MATIC", launched_in=2017, state="active", minor_units=18),
    Currency(name="Storj", code="STORJ", launched_in=2017, state="active", minor_units=8),
    Currency(name="Loopring", code="LRC", launched_in=2017, state="active", minor_units=8),
    ## inactive
    Currency(name="Bitconnect", code="BCC", launched_in=2017, state="inactive", minor_units=8),
    # launched in 2018
    ## active
    Currency(name="AmbaCoin", code=None, launched_in=2018, state="active", minor_units=4),
    Currency(name="Alchemy Pay", code="ACH", launched_in=2018, state="active", minor_units=18),
    Currency(name="Bitcoin SV", code="BSV", launched_in=2018, state="active", minor_units=8),
    Currency(name="Cronos", code="CRO", launched_in=2018, state="active", minor_units=8),
    Currency(name="Fantom", code="FTM", launched_in=2019, state="active", minor_units=18),
    Currency(name="Nervos Network", code="CKB", launched_in=2018, state="active", minor_units=8),
    Currency(name="TerraClassicUSD", code="USTC", launched_in=2018, state="active", minor_units=2),
    Currency(name="Terra", code="LUNA", launched_in=2018, state="active", minor_units=6),
    Currency(name="USD Coin", code="USDC", launched_in=2018, state="active", minor_units=2),
    Currency(name="Uniswap", code="UNI", launched_in=2018, state="active", minor_units=18),
    Currency(
        name="Measurable Data Token", code="MDT", launched_in=2018, state="active", minor_units=18
    ),
    Currency(name="Synthetix", code="SNX", launched_in=2018, state="active", minor_units=8),
    Currency(name="Quant", code="QNT", launched_in=2018, state="active", minor_units=8),
    ## inactive
    Currency(name="KODAKCoin", code=None, launched_in=2018, state="inactive", minor_units=None),
    Currency(name="Petro", code="PTR", launched_in=2018, state="inactive", minor_units=8),
    # launched in 2019
    ## active
    Currency(name="Algorand", code="ALGO", launched_in=2019, state="active", minor_units=6),
    Currency(name="Ankr", code="ANKR", launched_in=2019, state="active", minor_units=18),
    Currency(name="Axie Infinity", code="AXS", launched_in=2019, state="active", minor_units=18),
    Currency(name="Band Protocol", code="BAND", launched_in=2019, state="active", minor_units=18),
    Currency(name="Biconomy", code="BICO", launched_in=2019, state="active", minor_units=18),
    Currency(name="Binance USD", code="BUSD", launched_in=2019, state="active", minor_units=2),
    Currency(name="Cosmos", code="ATOM", launched_in=2019, state="active", minor_units=6),
    Currency(name="Chiliz", code="CHZ", launched_in=2019, state="active", minor_units=8),
    Currency(name="Orchid", code="OXT", launched_in=2019, state="active", minor_units=8),
    Currency(name="Tellor", code="TRB", launched_in=2019, state="active", minor_units=18),
    Currency(name="Wrapped Bitcoin", code="WBTC", launched_in=2019, state="active", minor_units=8),
    # launched in 2020
    ## active
    Currency(name="1inch Network", code="1INCH", launched_in=2020, state="active", minor_units=18),
    Currency(name="Avalanche", code="AVAX", launched_in=2020, state="active", minor_units=8),
    Currency(name="API3", code="API3", launched_in=2020, state="active", minor_units=18),
    Currency(name="Amp", code="AMP", launched_in=2020, state="active", minor_units=18),
    Currency(name="Balancer", code="BAL", launched_in=2020, state="active", minor_units=18),
    Currency(name="BarnBridge", code="BOND", launched_in=2020, state="active", minor_units=18),
    Currency(name="Bonfida", code="FIDA", launched_in=2020, state="active", minor_units=8),
    Currency(
        name="Bitcoin Cash ABC", code="BCHA", launched_in=2020, state="active", minor_units=8
    ),
    Currency(name="Celo", code="CELO", launched_in=2020, state="active", minor_units=8),
    Currency(name="Compound", code="COMP", launched_in=2020, state="active", minor_units=8),
    Currency(name="Curve", code="CRV", launched_in=2020, state="active", minor_units=8),
    Currency(name="Filecoin", code="FIL", launched_in=2020, state="active", minor_units=18),
    Currency(name="PancakeSwap", code="CAKE", launched_in=2020, state="active", minor_units=18),
    Currency(name="Polkadot", code="DOT", launched_in=2020, state="active", minor_units=16),
    Currency(name="Mirror Protocol", code="MIR", launched_in=2020, state="active", minor_units=6),
    Currency(name="The Graph", code="GRT", launched_in=2020, state="active", minor_units=8),
    Currency(name="Shiba Inu", code="SHIB", launched_in=2020, state="active", minor_units=8),
    Currency(name="Solana", code="SOL", launched_in=2020, state="active", minor_units=8),
    Currency(name="SushiSwap", code="SUSHI", launched_in=2020, state="active", minor_units=18),
    Currency(name="Yearn.finance", code="YFI", launched_in=2020, state="active", minor_units=8),
    # launched in 2021
    ## active
    Currency(
        name="Ampleforth Governance Token",
        code="FORTH",
        launched_in=2021,
        state="active",
        minor_units=18,
    ),
    Currency(name="BitDAO", code="BIT", launched_in=2021, state="active", minor_units=18),
    Currency(name="Cartesi", code="CTSI", launched_in=2021, state="active", minor_units=8),
    Currency(
        name="Decentralized Social", code="DESO", launched_in=2021, state="active", minor_units=8
    ),
    Currency(name="SafeMoon", code="SFM", launched_in=2021, state="active", minor_units=12),
    # launched in 2022
    ## active
    Currency(name="ApeCoin", code="APE", launched_in=2022, state="active", minor_units=18),
    Currency(name="Aptos", code="APT", launched_in=2022, state="active", minor_units=18),
]
