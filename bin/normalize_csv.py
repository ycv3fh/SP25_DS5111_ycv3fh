import pandas as pd
import os


def normalize_csv(input_csv_path):
    """
    Reads a raw stock data CSV file, normalizes it to the expected format,
    and writes the transformed data to a new CSV file with `_norm` appended to the filename.
    """
    assert isinstance(input_csv_path, str) and input_csv_path.endswith('.csv'), "Input must be a valid CSV file path"

    # The columns specified to keep
    headers = ['symbol','price','price_change','price_percent_change']
    # read in the csv file
    dataframe = pd.read_csv(input_csv_path)
    # Only keep columns in dataframe that match with columns specified in headers
    dataframe = dataframe[[col for col in headers if col in dataframe.columns]]

    # Save normaized csv file under new file name
    output_csv_path = f'{input_csv_path}_norm'
    dataframe.to_csv(output_csv_path, index=False)
    assert os.path.exists(output_csv_path), "Output CSV file was not created successfully" 

    return output_csv_path

