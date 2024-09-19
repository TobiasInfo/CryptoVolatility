"""
This module contains functions for reading configuration from a JSON file, 
logging activity, and outputting results.
"""

import json
import time
import os


def read_config(file_path):
    """
    Reads the configuration from a JSON file.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: A dictionary containing the configuration.
    """

    # Check if the file is OK
    if not file_path.endswith(".json"):
        raise ValueError("Configuration file must be a JSON file")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"Configuration file is not a file: {file_path}")

    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Configuration file is not readable: {file_path}")

    # Read the configuration from the file
    with open(file_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Validate required fields
    required_fields = ["exchange_name", "fiat_currency", "days"]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required configuration field: {field}")

    if not isinstance(config["days"], int) or config["days"] <= 0:
        raise ValueError(f"'days' must be a positive integer, got: {config['days']}")

    return config


def log_activity(message):
    """
    Logs the current activity of the program to the screen.

    Parameters:
    message (str): The message to log.
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def output_results(data, file_name="volatility_output.csv", output_csv=False):
    """
    Outputs the results of the program.

    Parameters:
    data (pd.DataFrame): The results to output.
    file_name (str): The name of the output file.
    output_csv (bool): Whether to output the results to a CSV file.
    """
    if output_csv:
        data.to_csv(file_name, index=False)
        log_activity(f"[output_results] Results saved to {file_name}")
    else:
        print(data)
