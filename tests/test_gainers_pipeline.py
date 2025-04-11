
import pandas as pd
import sys
sys.path.append('.')
from bin.gainers.yahoo import GainerDownloadYahoo
from bin.gainers.wsj import GainerDownloadWSJ
from bin.normalize_csv import normalize_csv

def test_pipeline_yahoo_data():

    downloader = GainerDownloadYahoo()
    downloader.download()

    raw_file = "ygainers.csv" 
    normalized_file = normalize_csv(raw_file)

    df = pd.read_csv(normalized_file)

    # Basic checks
    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float

def test_pipeline_wsj_data():

    downloader = GainerDownloadWSJ()
    downloader.download()

    raw_file = "wgainers.csv"
    normalized_file = normalize_csv(raw_file)

    df = pd.read_csv(normalized_file)

    # Basic checks
    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float
