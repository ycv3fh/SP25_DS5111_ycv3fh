from bin.gainers.yahoo import get_yahoo_gainers
from bin.gainers.wsj import get_wsj_gainers
from bin.normalize_csv import normalize_csv

def test_pipeline_yahoo_data():

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
    normalized_file = normalize_csv(raw_file)

    df = pd.read_csv(normalized_file)

    # Basic checks
    assert not df.empty
    assert 'symbol' in df.columns
    assert 'price_percent_change' in df.columns
    assert df['price_percent_change'].dtype == float
