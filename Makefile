all: common-forenames-by-country.json common-forenames.txt common-surnames-by-country.json common-surnames.txt

common-forenames-by-country.json: common-forenames-by-country.csv
	python3 forenames2json.py >common-forenames-by-country.json

common-forenames.txt: common-forenames-by-country.json
	cat common-forenames-by-country.json | jq -r 'values[][].names[]|.localized + .romanized|.[]' | sort | uniq >common-forenames.txt

common-surnames-by-country.json: common-surnames-by-country.csv
	python3 surnames2json.py >common-surnames-by-country.json

common-surnames.txt: common-surnames-by-country.json
	cat common-surnames-by-country.json | jq -r 'values[][]|.localized + .romanized|.[]' | sort | uniq >common-surnames.txt

clean:
	rm -f *.json *.txt
