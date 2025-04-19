default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

lint: env
	. env/bin/activate; pylint bin/normalize_csv.py

test: lint
	pytest -vv tests

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox \
	--timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wjsgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox \
	 --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wjsgainers.html

wjsgainers.csv: wjsgainers.html
	python -c "import pandas as pd; raw = pd.read_html('wjsgainers.html'); raw[0].to_csv('wjsgainers.csv')"

gainers:
	@if [ -z "$(SRC)" ]; then \
            echo "SRC not set. Usage: make gainers SRC=<yahoo|wsj>"; \
            exit 1; \
        fi; \
<<<<<<< HEAD
        . env/bin/activate;
	python get_gainer.py $(SRC)
=======
	python bin/get_gainer.py $(SRC)
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
