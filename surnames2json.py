from csv import DictReader
from itertools import groupby
from json import dumps

data = None
with open("common-surnames-by-country.csv", mode="r", encoding="utf-8-sig") as input:
    data = list(DictReader(input))

countries = {}
for country, rows1 in groupby(data, lambda row: row["Country"]):
    rows1 = list(rows1)

    country_names = []
    for name_group, rows2 in groupby(rows1, lambda row: row["Name Group"]):
        rows2 = list(rows2)
        count = max(
            [int(row["Count"]) for row in rows2 if row["Count"] != ""], default=None
        )
        localized = list(
            set([row["Localized Name"] for row in rows2 if row["Localized Name"] != ""])
        )
        romanized = list(
            set([row["Romanized Name"] for row in rows2 if row["Romanized Name"] != ""])
        )
        rank = max(
            [int(row["Rank"]) for row in rows2 if row["Rank"] != ""], default=None
        )
        country_names.append(
            {
                "id": name_group,
                "rank": rank,
                "localized": localized,
                "romanized": romanized,
                "count": count,
            }
        )

    countries[country] = country_names

print(dumps(countries, ensure_ascii=False, indent=2))

