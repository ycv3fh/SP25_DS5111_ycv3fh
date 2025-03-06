import sys
sys.path.append('.')
import bin.normalize_csv
import pandas as pd
import os 

def test_normalize_csv():
    data = {
        'symbol': ['AAPL', 'GOOG', 'AMZN'],
        'price': [150, 2700, 3400],
        'price_change': [1.5, 2.3, -5.2],
        'price_percent_change': [1.0, 0.09, -0.15],
    }
    df = pd.DataFrame(data)
    input_csv_path = 'test_data.csv'
    df.to_csv(input_csv_path, index=False)
    
    #run sample data into normalize_csv function
    output_csv_path = bin.normalize_csv.normalize_csv(input_csv_path)

    #Test that the output file was created
    assert os.path.exists(output_csv_path), "The normalized CSV file was not created."
    
    output_df = pd.read_csv(output_csv_path)

    #Test that output  columns match expected columns
    expected_columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    assert all(col in output_df.columns for col in expected_columns), f"Output CSV is missing columns:{output_df.columns}"
