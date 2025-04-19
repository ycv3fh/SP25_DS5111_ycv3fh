'''
This file contains the WSJ-specific implementations of both the downloader and processor.

Classes:
    GainerDownloadWSJ (WSJ-specific implementation of GainerDownload)
    GainerProcessWSJ (WSJ-specific implementation of GainerProcess)
'''
import os
<<<<<<< HEAD
#if doesnt import then try with "bin.gainers.base import GainerDownload, GainerProcess"
from .base import GainerDownload, GainerProcess
import datetime
=======
from .base import GainerDownload, GainerProcess
from .normalize_csv import normalize_csv
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c

class GainerDownloadWSJ(GainerDownload):
    '''
    Handles the downloading the list of gainers from the WSJ
    '''
    def __init__(self):
<<<<<<< HEAD
        #super().__init__()
        pass

    def download(self):
        command = '''sudo google-chrome-stable --headless --disable-gpu --dump-dom \
 --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html'''
        os.system(command)
        command_2 = '''python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); \
 raw[0].to_csv('wsjgainers.csv')"'''
        os.system(command_2)
=======
        super().__init__()

    def download(self):
	os.system("make wsj.csv")
        print("Downloading WSJ gainers")
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c

class GainerProcessWSJ(GainerProcess):
    '''
    Normalizes and saves the WSJ gainer data
    '''
    def __init__(self,data):
<<<<<<< HEAD
        pass

    def normalize(self):
        #copy/paste normalizer_csv
        column_mapping = {
        'Symbol': 'symbol',
        'Price': 'price',
        'Change': 'price_change',
        'Change %': 'price_percent_change'
        }

        # read in the csv file
        df = pd.read_csv(self)

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
        output_path = "normalized_temp.csv"
        df.to_csv(output_path,index=False)

    def save_with_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H$M%S")
        new_filename = f"bin/gainers/data/wsj_gainers_{timestamp}.csv"
        os.rename(self.normalized_file, new_filename)
=======
        super().__init__()
        self.raw_data = raw_data
        self.norm_data = None

    def normalize(self):
        self.normalized_file = normalize_csv(self.raw_data)
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
	timestamp = datetime.datetime.now().strftime("%Y%m%d_%H$M%S")
	new_filename = f"wsj_gainers_{timestamp}.csv"
	os.rename(self.normalized_file, new_filename)
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
        print("Saving WSJ gainers")

