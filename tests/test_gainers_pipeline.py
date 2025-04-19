<<<<<<< HEAD

import pandas as pd
import sys
sys.path.append('.')
from bin.gainers.yahoo import GainerDownloadYahoo
from bin.gainers.wsj import GainerDownloadWSJ
=======
import sys
sys.path.append('.')
from bin.gainers.yahoo import get_yahoo_gainers
from bin.gainers.wsj import get_wsj_gainers
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
from bin.normalize_csv import normalize_csv

def test_pipeline_yahoo_data():

<<<<<<< HEAD
    # Create Yahoo-specific processor using your factory
    print("Initializing Yahoo gainer processor...")
    x = factory.GainerFactory("yahoo")

    print("Getting downloader...")
    downloader = x.get_downloader()
    downloader.download()  # This should create ygainers.csv

    raw_file = "ygainers.csv"
    assert os.path.exists(raw_file), "Download failed: raw file not found."

    print("Getting normalizer...")
    normalizer = x.get_normalizer()
    normalizer.input_file = raw_file  # if needed, set file path

    print("Running normalization...")
    normalizer.normalize()

    # Save normalized file (and assume it sets the filename internally)
    normalizer.save_with_timestamp()
    normalized_file = normalizer.normalized_file
    assert os.path.exists(normalized_file), "Normalized file not saved."

def test_pipeline_wsj_data():

    downloader = GainerDownloadWSJ()
    downloader.download()

    raw_file = "wgainers.csv"
=======
    raw_file = get_yahoo_gainers()
    normalized_file = normalize_csv(raw_file)

    df = pd.read_csv(normalized_file)

    # Basic checks
    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float

def test_pipeline_wsj_data():

    raw_file = get_wsj_gainers()
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
    normalized_file = normalize_csv(raw_file)

    df = pd.read_csv(normalized_file)

    # Basic checks
    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float
