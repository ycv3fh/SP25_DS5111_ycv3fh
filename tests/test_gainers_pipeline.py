import os
import sys
import glob
import pandas as pd
# Ensure path includes local package
sys.path.append('.')
from bin.gainers.factory import GainerFactory
#Function to clean up files are test runs
def cleanup_files(patterns):
    for pattern in patterns:
        for file in glob.glob(pattern):
            try:
                os.remove(file)
            except Exception as e:
                print(f"Warning: Failed to remove {file}: {e}")

def test_yahoo_pipeline():
    print("Running WSJ pipeline test...")
    factory = GainerFactory("yahoo")
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    downloader.download()

    assert os.path.exists("ygainers.csv"), "Download failed: raw file not found."

    normalizer.normalize()
    normalizer.save_with_timestamp()

    saved_files = glob.glob("yahoo_gainers_*.csv")
    assert saved_files, "No Yahoo gainer file saved with timestamp."

    df = pd.read_csv(saved_files[-1])
    assert not df.empty, "Yahoo normalized DataFrame is empty."
    assert "symbol" in df.columns
    assert "price_percent_change" in df.columns
    assert df["price_percent_change"].dtype in [float, "float64"]

    cleanup_files(["ygainers.html","ygainers.csv", "yahoo_gainers_*.csv"])

def test_wsj_pipeline():
    #remove files before running tests
    print("Running WSJ pipeline test...")
    factory = GainerFactory("wsj")
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    downloader.download()

    assert os.path.exists("wsjgainers.csv"), "Raw WSJ gainer file not found."

    normalizer.normalize()
    normalizer.save_with_timestamp()

    saved_files = glob.glob("bin/gainers/data/wsj_gainers_*.csv")
    assert saved_files, "No WSJ gainer file saved with timestamp."

    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float

    cleanup_files(["wsjgainers.html","wsjgainers.csv", "normalized_temp.csv", "bin/gainers/data/wsj_gainers_*.csv"])
