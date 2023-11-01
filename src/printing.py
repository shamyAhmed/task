import csv

with open("../assets/dataset-limited.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)