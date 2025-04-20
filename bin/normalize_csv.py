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
            'Volume': 'volume',
            'Last': 'price',
            'Chg': 'price_change',
            '% Chg': 'price_percent_change',
            'Name': 'symbol'  # For WSJ, we need to extract the ticker from 'Name'
        }
    }

    # read in the csv file
    df = pd.read_csv(input_path)

    # Get the column mapping based on the source type
    mapping = column_mappings[source_type]

    # Rename columns based on the mapping for the specific source
    df = df.rename(columns=mapping)

    # Extract ticker abbreviation from 'Name' for WSJ
    if source_type == 'wsj' and 'symbol' in df.columns:
        df['symbol'] = df['symbol'].apply(lambda x: re.search(r'\((\w+)\)', str(x)).group(1) if isinstance(x, str) and '(' in x else x)

    # Only keep columns in dataframe that match with columns specified in the mapping
    df = df[[new_col for new_col in mapping.values() if new_col in df.columns]]

    # Normalize 'price_percent_change' column
    if 'price_percent_change' in df.columns:
        df['price_percent_change'] = (
            df['price_percent_change']
            .replace('%', '', regex=True)
            .astype(float)
        )

    # Normalize volume if present
    if 'volume' in df.columns:
        # If volume is in millions or billions, convert to the base unit
        df['volume'] = df['volume'].replace({
            r'M': '*1e6',  # Million
            r'B': '*1e9',  # Billion
        }, regex=True)
        df['volume'] = df['volume'].map(pd.eval).astype(float)

    # Save normalized csv file under new file name
    output_path = os.path.splitext(input_path)[0] + "_norm" + os.path.splitext(input_path)[1]
    df.to_csv(output_path, index=False)

    # Return normalized csv file path
    return output_path
