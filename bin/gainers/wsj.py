'''
This file contains the WSJ-specific implementations of both the downloader and processor.

Classes:
    GainerDownloadWSJ (WSJ-specific implementation of GainerDownload)
    GainerProcessWSJ (WSJ-specific implementation of GainerProcess)
'''
import os
import pandas as pd
#if doesnt import then try with "bin.gainers.base import GainerDownload, GainerProcess"
from .base import GainerDownload, GainerProcess
import datetime
from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    '''
    Handles the downloading the list of gainers from the WSJ
    '''
    def __init__(self):
        pass

    def download(self):
        command = '''sudo google-chrome-stable --headless --disable-gpu --dump-dom \
 --no-sandbox --timeout=10000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html'''
        os.system(command)
        command_2 = '''python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); \
 raw[0].to_csv('wsjgainers.csv')"'''
        os.system(command_2)
        super().__init__()

class GainerProcessWSJ(GainerProcess):
    '''
    Normalizes and saves the WSJ gainer data
    '''
    def __init__(self, input_file):
        self.input_file = input_file
        self.normalized_file = None
        super().__init__()

    def normalize(self):
        df = pd.read_csv(self.input_file)

        column_mapping = {
        'Unnamed: 0': 'index',
        'Volume': 'volume',
        'Last': 'price',
        'Chg': 'price_change',
        '% Chg': 'price_percent_change'
        }
        # Rename the columns according to the mapping
        df = df.rename(columns=column_mapping)
        df.rename(columns={df.columns[1]: 'name'}, inplace=True)
        # Keep only the relevant columns
        df = df[['name', 'price', 'price_change', 'price_percent_change', 'volume']]
        df['price_percent_change'] = pd.to_numeric(df['price_percent_change'], errors='coerce')

        # Normalize volume if present
        def parse_volume(val):
            try:
                val = str(val).strip().replace(',', '')
                if val.endswith('K'):
                    return float(val[:-1]) * 1_000
                elif val.endswith('M'):
                    return float(val[:-1]) * 1_000_000
                elif val.endswith('B'):
                    return float(val[:-1]) * 1_000_000_000
                return float(val)
            except Exception as e:
                print(f"Error parsing volume: {val} ({e})")
                return None
        df['volume'] = df['volume'].map(parse_volume)

        if 'volume' in df.columns:
            # If volume is in millions or billions, convert to the base unit
            df['volume'] = df['volume'].replace({
                r'M': '*1e6',  # Million
                r'B': '*1e9',  # Billion
            }, regex=True)
        df['volume'] = df['volume'].map(pd.eval).astype(float)

        self.normalized_file = "normalized_temp.csv"
        df.to_csv(self.normalized_file,index=False)

    def save_with_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"bin/gainers/data/wsj_gainers_{timestamp}.csv"
        os.rename(self.normalized_file, new_filename)
        print("Saving WSJ gainers")

