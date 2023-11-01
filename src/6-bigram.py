from nltk.util import bigrams
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import re, csv, nltk

stememer = PorterStemmer()
freq_dist = FreqDist()
text = "I received your invitation, I will be attending the party"

#* download the necessary packages
# nltk.download()

with open("../assets/dataset-limited.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        for word in word_tokenize(row[6]):
            freq_dist[word.lower()] += 1
    
print(f"the statement is {text}")
print("enter the words you wish to test separated by a comma")
test_words = input("> ").split(",")

words = text.lower().split(" ")
for index, word in enumerate(words):
    word = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", word)
    words[index] = stememer.stem(word)
    
for pair in bigrams(words):
    print(pair)
    #TODO: how to get the frequency distribution of words and statements? 
    
