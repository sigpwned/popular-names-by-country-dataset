from csv import DictReader
from itertools import groupby
from json import dumps

data = None
with open("common-forenames-by-country.csv", mode="r", encoding="utf-8-sig") as input:
    data = list(DictReader(input))

countries = {}
for (country, rows1) in groupby(data, lambda row: row["Country"]):
    rows1 = list(rows1)

    country_groups = []
    for (country_group, rows2) in groupby(rows1, lambda row: row["Country Group"]):
        rows2 = list(rows2)

        region = "All" if rows2[0]["Region"] == "" else rows2[0]["Region"]
        population = "All" if rows2[0]["Population"] == "" else rows2[0]["Population"]
        note = None if rows2[0]["Note"] == "" else rows2[0]["Note"]

        country_group_names = []
        for (name_group, rows3) in groupby(rows2, lambda row: row["Name Group"]):
            rows3 = list(rows3)

            gender = rows3[0]["Gender"]
            localized = list(
                set(
                    [
                        row["Localized Name"]
                        for row in rows3
                        if row["Localized Name"] != ""
                    ]
                )
            )
            romanized = list(
                set(
                    [
                        row["Romanized Name"]
                        for row in rows3
                        if row["Romanized Name"] != ""
                    ]
                )
            )
            rank = max(
                [int(row["Index"]) for row in rows3 if row["Index"] != ""], default=None
            )

            country_group_names.append(
                {
                    "id": name_group,
                    "rank": rank,
                    "gender": gender,
                    "localized": localized,
                    "romanized": romanized,
                }
            )

        country_groups.append(
            {
                "region": region,
                "population": population,
                "note": note,
                "names": country_group_names,
            }
        )

    countries[country] = country_groups

print(dumps(countries, ensure_ascii=False, indent=2))

