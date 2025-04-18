import sys
sys.path.append('.')
import bin.normalize_csv
import pandas as pd
import os

def test_normalize_csv():

    input = 'tests/data/test_data.csv'
    #run sample data into normalize_csv function
    output_file = bin.normalize_csv.normalize_csv(input)

    #Test that the output file was created
    assert os.path.exists(output_file), "The normalized CSV file was not created."

    output = pd.read_csv(output_file)

    #Test that output  columns match expected columns
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert all(col in output.columns for col in expected_columns), f"Output CSV is missing columns:{output.columns}"
