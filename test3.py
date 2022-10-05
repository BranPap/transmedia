import os, re, string, csv
import nltk
from nltk import word_tokenize, FreqDist
from nltk.util import ngrams
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
import shutil

def convertTuple(tup):
# initialize an empty string
    str = ''
    for item in tup:
        str = str + item + " "
    return str.strip(" ")

ignoreList = ["'",".",",","”","’","''","“","‘","’","―"]

filesText = []

directory = "text/"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename),encoding="utf-8") as myfile:
        content = myfile.read().lower()
        filesText.append(content)

newList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)

newList = [item for sublist in newList for item in sublist]

finalList = " ".join(newList)

print(len(finalList))

transgender_filter = lambda *w: 'transgender' not in w
biological_filter = lambda *w: 'biological' not in w

finder = BigramCollocationFinder.from_words(word_tokenize(finalList))

finder.apply_freq_filter(10)
finder.apply_ngram_filter(transgender_filter)

headers = ["n-gram","PMI"]

with open("transgenderBigramPMI.csv","w", newline="") as PMICsv:
    w = csv.writer(PMICsv)
    w.writerow(headers)
    for i in finder.score_ngrams(bigram_measures.pmi):
        i = list(i)
        i[0] = " ".join(i[0])
        if i[1] < 0:
            i[1] = 0
        w.writerow(i)

finder = BigramCollocationFinder.from_words(word_tokenize(finalList))

finder.apply_freq_filter(10)
finder.apply_ngram_filter(biological_filter)

headers = ["n-gram","PMI"]

with open("biologicalBigramPMI.csv","w", newline="") as PMICsv:
    w = csv.writer(PMICsv)
    w.writerow(headers)
    for i in finder.score_ngrams(bigram_measures.pmi):
        i = list(i)
        i[0] = " ".join(i[0])
        if i[1] < 0:
            i[1] = 0
        w.writerow(i)

finder = TrigramCollocationFinder.from_words(word_tokenize(finalList))

finder.apply_freq_filter(10)
finder.apply_ngram_filter(transgender_filter)

headers = ["n-gram","PMI"]

with open("transgenderTrigramPMI.csv","w", newline="") as PMICsv:
    w = csv.writer(PMICsv)
    w.writerow(headers)
    for i in finder.score_ngrams(trigram_measures.pmi):
        i = list(i)
        i[0] = " ".join(i[0])
        if i[1] < 0:
            i[1] = 0
        w.writerow(i)

finder = TrigramCollocationFinder.from_words(word_tokenize(finalList))

finder.apply_freq_filter(10)
finder.apply_ngram_filter(biological_filter)

with open("biologicalTrigramPMI.csv","w", newline="") as PMICsv:
    w = csv.writer(PMICsv)
    w.writerow(headers)
    for i in finder.score_ngrams(trigram_measures.pmi):
        i = list(i)
        i[0] = " ".join(i[0])
        if i[1] < 0:
            i[1] = 0
        w.writerow(i)

