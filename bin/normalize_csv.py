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

    # The columns specified to keep and their new names
    column_mapping = {
        'Symbol': 'symbol',
        'Price': 'price',
        'Change': 'price_change',
        'Change %': 'price_percent_change'
    }

    # read in the csv file
    df = pd.read_csv(input_path)

    # Rename columns based on the mapping
    df = df.rename(columns=column_mapping)

    # Only keep columns in dataframe that match with columns specified in headers
    df = df[[new_col for new_col in column_mapping.values() if new_col in df.columns]]

<<<<<<< HEAD
    #Convert the file from object datatype to float datatype
    df['price_percent_change'] = (
        df['price_percent_change']
        .replace('%', '', regex=True)
        .astype(float)
        )

=======
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
    # Save normalized csv file under new file name
    output_path = os.path.splitext(input_path)[0]+"_norm"+os.path.splitext(input_path)[1]
    df.to_csv(output_path,index=False)

    # Returns normalized csv file
    return output_path
