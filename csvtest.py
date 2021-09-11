import csv


def read_data():
    with open("data.csv" "r") as csv:
        reader = csv.DictReader(csv)

