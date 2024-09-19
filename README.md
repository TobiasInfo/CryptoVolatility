# Crypto Volatility Calculator

This Python command-line application calculates the daily volatility of cryptocurrencies against a fiat currency. It fetches data from a cryptocurrency exchange, processes it, and outputs the results in a CSV file or on the screen.

## Features

- **Exchange Support**: Currently supports Binance (via the CCXT library) for fetching market data.
- **Daily Volatility Calculation**: Calculates daily volatility using historical price data and a standard formula.
- **Configurable Parameters**: The exchange, fiat currency, and the number of days to analyze can be configured through a `config.json` file.
- **Logging**: Logs activities, such as data fetching and calculations, in the console.
- **CSV Output**: Optionally outputs results to a CSV file containing:
  - Cryptocurrency symbol
  - Fiat currency symbol
  - Calculated daily volatility
  - Last traded price
  - Average trading volume over the selected period

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Output](#output)
- [Logging](#logging)
- [Dependencies](#dependencies)
- [Acknowledgements](#acknowledgements)
- [Author](#author)

## Installation

1. **Install Required Packages**: The project uses `ccxt` for fetching data, `pandas` for data handling and `numpy` for calculation. Install these dependencies using pip:
   ```bash
    pip install ccxt pandas numpy
    ```
## Usage

To run the program, simply execute `main.py`:

```bash
python3 main.py
```

The script will fetch cryptocurrency data from the exchange (defined in the configuration file), calculate the daily volatility, and output the results.

## Configuration

The script reads parameters from a `config.json` file located in the root directory. Below is an example of the configuration file:

```json
{
  "exchange_name": "binance",
  "fiat_currency": "EUR",
  "days": 10
}
```

### Configuration Fields:

- `exchange_name`: The name of the exchange to fetch data from (e.g., "binance").
- `fiat_currency`: The fiat currency against which to calculate cryptocurrency volatility (e.g., "EUR").
- `days`: The number of days to use for calculating the volatility.

Ensure that you update these parameters as needed before running the script.


## Output
### Console Output:

The results, including cryptocurrency volatility, last price, and average volume, will be displayed on the console.

### CSV Output:

Optionally, the program can output the results to a CSV file. The file will include the following columns:

- `base`: The cryptocurrency symbol (e.g., BTC).
- `quote`: The fiat currency symbol (e.g., EUR).
- `daily_volatility`: The calculated daily volatility.
- `last_price`: The last traded price of the cryptocurrency.
- `average_volume`: The average trading volume over the selected period.

#### Sample CSV output:

```text
base,quote,daily_volatility,last_price,average_volume
GRT,EUR,0.003769628628923544,0.1347,180011.8
EOS,EUR,0.025981724346163023,0.762,34726.71
```
## Logging

All activities during execution are logged to the console. Example log messages include data fetching status, volatility calculations, and file output notifications.

## Dependencies

- `ccxt` for cryptocurrency market data fetching.
- `pandas` for data manipulation and CSV output.
- `numpy` for mathematical calculations.

## Acknowledgements

Special thanks to the team at Vesper Aerospace for the opportunity and proposition of this project.

## Author

- `Tobias SAVARY`