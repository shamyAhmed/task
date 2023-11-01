from nltk.stem import PorterStemmer
import csv

lines = open("../assets/dataset-limited.csv", mode="r").readlines()
reader = csv.reader(lines)

stemmer = PorterStemmer()
            
with open("../assets/dataset-limited.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    headlines = next(reader).copy()
    headlines.append("stemmed_text")
    writer.writerow(headlines)
    for row in reader:
        words = row[5].split(" ")
        for index, word in enumerate(words):
            words[index] = stemmer.stem(word)
        newRow = row.copy()
        newRow.append(" ".join(words))
        writer.writerow(newRow)
