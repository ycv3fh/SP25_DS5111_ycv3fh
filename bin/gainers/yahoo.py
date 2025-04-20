'''
This file contains the Yahoo-specific implementations of both the downloader and process

Classes:
    GainerDownloadYahoo (Yahoo-specific implementation of GainerDownload)
    GainerProcessYahoo (Yahoo-specific implementation of GainerProcess)
'''
import os
import pandas as pd
from .base import GainerDownload, GainerProcess
import datetime

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        command = '''sudo google-chrome-stable --headless --disable-gpu --dump-dom \
--no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html'''
        os.system(command)
        command_2 = '''python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')" '''
        os.system(command_2)

class GainerProcessYahoo(GainerProcess):
    def __init__(self, input_file):
        self.input_file = input_file
        self.normalized_file = None
        super().__init__()

    def normalize(self):
        column_mapping = {
        'Symbol': 'symbol',
        'Price': 'price',
        'Change': 'price_change',
        'Change %': 'price_percent_change'
        }

        # read in the csv file
        df = pd.read_csv(self.input_file)
        # Rename columns based on the mapping
        df = df.rename(columns=column_mapping)
        # Only keep columns in dataframe that match with columns specified in headers
        df = df[[new_col for new_col in column_mapping.values() if new_col in df.columns]]
        #Convert the file from object datatype to float datatype
        df['price_percent_change'] = (
            df['price_percent_change']
            .replace('%', '', regex=True)
            .astype(float)
        )
        self.normalized_file = "normalized_temp.csv"
        df.to_csv(self.normalized_file,index=False)

    def save_with_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"yahoo_gainers_{timestamp}.csv"
        os.rename(self.normalized_file, new_filename)
        print("Saving Yahoo gainers")
