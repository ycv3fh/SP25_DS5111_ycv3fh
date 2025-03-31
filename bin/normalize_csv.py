"""
normalize_csv.py

This module contains a function to normalize stock data CSV files.
"""

import os
import pandas as pd

def normalize_csv(input_path):
    """
    Reads a raw stock data CSV file, normalizes it to the expected format,
    and writes the transformed data to a new CSV file with `_norm` appended to the filename.
    """
    assert isinstance(input_path, str) and input_path.endswith('.csv'), "Invalid file path"

    # The columns specified to keep
    headers = ['symbol','price','price_change','price_percent_change']
    # read in the csv file
    df = pd.read_csv(input_path)
    # Only keep columns in dataframe that match with columns specified in headers
    df = df[[col for col in headers if col in df.columns]]
    # Save normalized csv file under new file name
    output_path = os.path.splitext(input_path)[0]+"_norm"+os.path.splitext(input_path)[1]
    df.to_csv(output_path,index=False)
    # Returns normalized csv file
    return output_path
