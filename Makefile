all: common-forenames-by-country.json common-surnames-by-country.json

common-forenames-by-country.json: common-forenames-by-country.csv
	python3 forenames2json.py >common-forenames-by-country.json

common-surnames-by-country.json: common-surnames-by-country.csv
	python3 surnames2json.py >common-surnames-by-country.json

clean:
	rm -f *.json
