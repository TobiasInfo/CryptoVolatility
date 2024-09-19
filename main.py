"""
Main script to calculate the daily volatility of cryptocurrencies.
"""

from input_output import read_config, log_activity, output_results
from fetch_data_calculation import fetch_data, calculate_daily_volatility


def main():
    # Recover the parameters from the configuration file
    try:
        config = read_config("config.json")
    except (ValueError, FileNotFoundError, PermissionError) as e:
        print(f"Error reading configuration file: {e}")
        return
    
    exchange_name = config["exchange_name"]
    fiat_currency = config["fiat_currency"]
    days = config["days"]

    # Fetch data from the exchange
    log_activity(f"[main] Fetching data from {exchange_name} for {fiat_currency}")
    try:
        data = fetch_data(exchange_name, fiat_currency, days)
    except ValueError as e:
        log_activity(f"[main] Error fetching data: {e}")
        return

    # Calculate the daily volatility of the cryptocurrencies
    log_activity(f"[main] Calculating volatility over {days} days")
    data["daily_volatility"] = data.apply(
        lambda row: calculate_daily_volatility(
            row["close_prices"], row["base"], fiat_currency
        ),
        axis=1,
    )

    # Output the results
    log_activity("[main] Outputting results")
    output_results(
        data[["base", "quote", "daily_volatility", "last_price", "average_volume"]],
        output_csv=True,
    )


if __name__ == "__main__":
    main()
