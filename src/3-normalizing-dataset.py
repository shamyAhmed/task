import re, csv

lines = open("../assets/dataset-limited.csv", mode="r").readlines()
reader = csv.reader(lines)
with open("../assets/dataset-limited.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    headlines = next(reader)
    headlines.append("cleaned_text")
    writer.writerow(headlines)
    for row in reader:
        text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", row[4])
        newRow = row.copy()
        newRow.append(text)
        writer.writerow(newRow)