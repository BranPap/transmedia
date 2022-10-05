import os, re, string, csv
import nltk
from nltk import word_tokenize, FreqDist
from nltk.util import ngrams




def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item + " "
    return str.strip(" ")
# var = 0

ignoreList = ["'",".",",","”","’","''","“","‘","’","―"]

filesText = []

directory = "text/"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename),encoding="utf-8") as myfile:
        content = myfile.read().lower()
        filesText.append(content)
    # var += 1
    # if var == 10:
    #     break


newList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    newList.append(tokens)

newList = [item for sublist in newList for item in sublist]


# print(newList)

with open("wordLookupOutput.txt","w") as outputFile:
    frequencies = FreqDist(newList)
    print(frequencies.most_common(100))