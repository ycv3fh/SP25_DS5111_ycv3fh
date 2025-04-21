"""
normalize_csv.py

This module contains a function to normalize stock data CSV files.
"""

import os
import re
import pandas as pd

def normalize_csv(input_path,source_type='yahoo'):
    """
    Reads a raw stock data CSV file, normalizes it to the expected format,
    and writes the transformed data to a new CSV file with `_norm` appended to the filename.
    """
    assert isinstance(input_path, str) and input_path.endswith('.csv'), "Invalid file path"

    # Define column mappings for Yahoo and WSJ
    column_mappings = {
        'yahoo': {
            'Symbol': 'symbol',
            'Price': 'price',
            'Change': 'price_change',
            'Change %': 'price_percent_change',
            'Volume': 'volume'
        },
        'wsj': {
            'Unnamed: 0': 'ticker',
            'Volume': 'volume',
            'Last': 'price',
            'Chg': 'price_change',
            '% Chg': 'price_percent_change'
        }
    }
    df = pd.read_csv(input_path)

    # Apply appropriate mapping
    mapping = column_mappings[source_type]
    # Rename columns based on the mapping for the specific source
    df = df.rename(columns=mapping)
    # Extract symbol for WSJ from 'symbol' column
    if source_type == 'wsj':
        df['symbol'] = df['symbol'].apply(lambda x: re.search(r'\((\w+)\)', str(x)).group(1)
                                          if isinstance(x, str) and '(' in x else x)

    # Normalize price_percent_change
    if 'price_percent_change' in df.columns:
        df['price_percent_change'] = df['price_percent_change'].replace('[%+]', '', regex=True).astype(float)

    # Only keep columns in dataframe that match with columns specified in the mapping
    df = df[[new_col for new_col in mapping.values() if new_col in df.columns]]

    # Normalize volume strings like "99.3M" or "314.2K"
    if 'volume' in df.columns:
        def parse_volume(val):
            if isinstance(val, str):
                val = val.strip()
                if val.endswith('M'):
                    return float(val[:-1]) * 1e6
                elif val.endswith('B'):
                    return float(val[:-1]) * 1e9
                elif val.endswith('K'):
                    return float(val[:-1]) * 1e3
            try:
                return float(val)
            except:
                return None
        df['volume'] = df['volume'].apply(parse_volume)

    # Keep only the normalized columns
    output_columns = ['symbol', 'price', 'price_change', 'price_percent_change', 'volume']
    df = df[[col for col in output_columns if col in df.columns]]

    # Normalize 'price_percent_change' column
    if 'price_percent_change' in df.columns:
        df['price_percent_change'] = (
            df['price_percent_change']
            .replace('%', '', regex=True)
            .astype(float)
        )

    # Save normalized csv file under new file name
    output_path = os.path.splitext(input_path)[0] + "_norm" + os.path.splitext(input_path)[1]
    df.to_csv(output_path, index=False)

    # Return normalized csv file path
    return output_path
