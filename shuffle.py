import csv
import random

input_path = r"teste.csv"
output_path = r"dataset.csv"

with open(input_path, "rb") as file:
    rows = list(csv.reader(file, delimiter=","))

random.shuffle(rows)

with open(output_path, "wb") as file:
    csv.writer(file, delimiter=",").writerows(rows)
