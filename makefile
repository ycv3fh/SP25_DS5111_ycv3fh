default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

lint: env
	. env/bin/activate; pylint bin/normalize_csv.py

test: lint
	. env/bin/activate && pytest -vv tests

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox \
	--timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox \
	 --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	. env/bin/activate; python -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

gainers:
	. env/bin/activate; python get_gainer.py $(SRC)
