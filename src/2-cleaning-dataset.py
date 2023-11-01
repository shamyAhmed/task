import csv
file = open("../assets/dataset-limited.csv", mode="r+", newline="")
lines = file.readlines()
file.close()
reader = csv.reader(lines, delimiter=",")
globals()["lines"] = None
globals()["file"] = None

with open('../assets/dataset-limited.csv', mode="w", newline="") as file:
    writer = csv.writer(file)
    headlines = next(reader)
    headlines.append("lower_case")
    writer.writerow(headlines)
    for row in reader:
        new_row = row.copy()
        bo = row[3].split(" ")
        new_row.append(" ".join([x for x in bo if x != ""]).lower())
        writer.writerow(new_row)
    