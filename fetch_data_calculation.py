"""
This module contains functions for fetching data from an exchange and calculating daily volatility.
"""

import numpy as np
import pandas as pd
import ccxt
from input_output import log_activity


def fetch_data(exchange_name, fiat_currency, days):
    """
    Fetches data from the specified exchange for the given fiat currency and the number of days.

    Parameters:
    exchange_name (str): The name of the exchange to fetch data from.
    fiat_currency (str): The fiat currency to fetch data for.
    days (int): The number of days to fetch data for.

    Returns:
    pd.DataFrame: A DataFrame containing the fetched data.
    """
    # Create an instance of the exchange
    # to get the list of available markets
    exchange = getattr(ccxt, exchange_name)()  # here binance
    markets = exchange.fetch_markets()
    crypto_data = []

    for market in markets:
        if market["quote"] == fiat_currency:
            # Fetch OHLCV data for the specified number of days
            # (Open, High, Low, Close, Volume) with a daily timeframe
            ohlcv = exchange.fetch_ohlcv(market["symbol"], "1d", limit=days)
            log_activity(
                f"[fetch_data] Fetched {len(ohlcv)} data points for {market['base']}/{fiat_currency}"
            )

            # Extract the close prices from the OHLCV data
            close_prices = [data[4] for data in ohlcv]

            crypto_data.append(
                {
                    "base": market["base"],
                    "quote": fiat_currency,
                    "last_price": close_prices[-1],
                    # Calculate the average volume over the specified number of days
                    "average_volume": np.mean([data[5] for data in ohlcv]),
                    "close_prices": close_prices,
                }
            )

    # Check if the exchange has markets
    if len(crypto_data) == 0:
        raise ValueError(
            f"No markets found for the specified fiat currency: {fiat_currency}"
        )

    log_activity(f"[fetch_data] Fetched data for {len(crypto_data)} cryptocurrencies")
    return pd.DataFrame(crypto_data)


def calculate_daily_volatility(close_prices, crypto, fiat_currency):
    """
    Calculates the daily volatility of a cryptocurrency based on its close prices.
    using the formula given in :
    https://www.wallstreetmojo.com/volatility-formula/

    Parameters:
    close_prices (list): A list of close prices for the cryptocurrency.
    crypto (str): The symbol of the cryptocurrency.

    Returns:
    float: The daily volatility of the cryptocurrency.
    """
    log_activity(
        f"[calculate_daily_volatility] Calculating volatility for {crypto}/{fiat_currency}"
    )
    p_avg = np.mean(close_prices)
    deviations = [p_avg - p_i for p_i in close_prices]
    squared_deviations = [deviation**2 for deviation in deviations]
    sum_squared_deviations = np.sum(squared_deviations)
    number_daily_stock_prices = len(close_prices)
    variance = sum_squared_deviations / number_daily_stock_prices
    daily_volatility = np.sqrt(variance)
    return daily_volatility
