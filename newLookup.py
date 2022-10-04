import os, re, string, csv
from nltk import word_tokenize 
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

bigramList = []

transDict = {}

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    bigram = list(ngrams(tokens, 2))
    bigramList.append(bigram)


# print(bigramList)

for pairList in bigramList:
    for pair in pairList:
        bigram = pair[0] + " " + pair[1]
        if pair[0] == "transgender":
            if bigram not in transDict.keys():
                transDict[bigram] = 1
            if bigram in transDict.keys():
                transDict[bigram] = transDict[bigram] + 1

# print(transDict)

headers = ["n-gram","count"]

with open("transgenderOutput.csv","w", newline="") as DictCsv:
    w = csv.writer(DictCsv)
    w.writerow(headers)
    for key, value in transDict.items():
        w.writerow([key, value])


### Identifies as 5-gram

# identifyAsDict = {}

# bigramList = []

# for line in filesText:
#     tokens = word_tokenize(line)
#     tokens = list(filter(lambda token: token not in string.punctuation, tokens))
#     tokens = list(filter(lambda token: token not in ignoreList, tokens))
#     tokens = [i.strip(".") for i in tokens]
#     bigram = list(ngrams(tokens, 4))
#     bigramList.append(bigram)


# # print(bigramList)

# for pairList in bigramList:
#     for pair in pairList:
#         bigram = convertTuple(pair)
#         if pair[0] == "identifies" and pair[1] == "as":
#             if bigram not in identifyAsDict.keys():
#                 identifyAsDict[bigram] = 1
#             if bigram in identifyAsDict.keys():
#                 identifyAsDict[bigram] = identifyAsDict[bigram] + 1

# # print(transDict)

# with open("identifyAsDictOutput.csv","w") as DictCsv:
#     for key in identifyAsDict.keys():
#         DictCsv.write("%s, %s\n" % (key, identifyAsDict[key]))


### trans dict

TransDict = {}

bigramList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    bigram = list(ngrams(tokens, 2))
    bigramList.append(bigram)


# print(bigramList)

for pairList in bigramList:
    for pair in pairList:
        bigram = convertTuple(pair)
        if pair[0] == "trans" :
            if bigram not in TransDict.keys():
                TransDict[bigram] = 1
            if bigram in TransDict.keys():
                TransDict[bigram] = TransDict[bigram] + 1

# print(transDict)

with open("TransDictOutput.csv","w") as DictCsv:
    for key in TransDict.keys():
        DictCsv.write("%s, %s\n" % (key, TransDict[key]))


### trans dict

# BiologicallyDict = {}

# bigramList = []

# for line in filesText:
#     tokens = word_tokenize(line)
#     tokens = list(filter(lambda token: token not in string.punctuation, tokens))
#     tokens = list(filter(lambda token: token not in ignoreList, tokens))
#     tokens = [i.strip(".") for i in tokens]
#     bigram = list(ngrams(tokens, 2))
#     bigramList.append(bigram)


# # print(bigramList)

# for pairList in bigramList:
#     for pair in pairList:
#         bigram = convertTuple(pair)
#         if pair[0] == "biologically" :
#             if bigram not in BiologicallyDict.keys():
#                 BiologicallyDict[bigram] = 1
#             if bigram in BiologicallyDict.keys():
#                 BiologicallyDict[bigram] = BiologicallyDict[bigram] + 1

# # print(transDict)

# with open("BiologicallyDictOutput.csv","w") as DictCsv:
#     for key in BiologicallyDict.keys():
#         DictCsv.write("%s, %s\n" % (key, BiologicallyDict[key]))


#BiologicalDict 

BiologicalDict = {}

bigramList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    bigram = list(ngrams(tokens, 2))
    bigramList.append(bigram)


# print(bigramList)

for pairList in bigramList:
    for pair in pairList:
        bigram = convertTuple(pair)
        if pair[0] == "biological" :
            if bigram not in BiologicalDict.keys():
                BiologicalDict[bigram] = 1
            if bigram in BiologicalDict.keys():
                BiologicalDict[bigram] = BiologicalDict[bigram] + 1

with open("BiologicalDictOutput.csv","w", newline="") as DictCsv:
    w = csv.writer(DictCsv)
    w.writerow(headers)
    for key, value in BiologicalDict.items():
        w.writerow([key, value])

#Non-binary 

# NonBinaryDict = {}

# bigramList = []

# for line in filesText:
#     tokens = word_tokenize(line)
#     tokens = list(filter(lambda token: token not in string.punctuation, tokens))
#     tokens = list(filter(lambda token: token not in ignoreList, tokens))
#     tokens = [i.strip(".") for i in tokens]
#     bigram = list(ngrams(tokens, 2))
#     bigramList.append(bigram)


# # print(bigramList)

# for pairList in bigramList:
#     for pair in pairList:
#         bigram = convertTuple(pair)
#         if pair[0] == "non-binary" or pair[0]== "nonbinary":
#             if bigram not in NonBinaryDict.keys():
#                 NonBinaryDict[bigram] = 1
#             if bigram in NonBinaryDict.keys():
#                 NonBinaryDict[bigram] = NonBinaryDict[bigram] + 1

# # print(transDict)

# with open("NonBinaryDictOutput.csv","w") as DictCsv:
#     for key in NonBinaryDict.keys():
#         DictCsv.write("%s, %s\n" % (key, NonBinaryDict[key]))

##Assigned at birth

AssignedDict = {}

bigramList = []

for line in filesText:
    tokens = word_tokenize(line)
    tokens = list(filter(lambda token: token not in string.punctuation, tokens))
    tokens = list(filter(lambda token: token not in ignoreList, tokens))
    tokens = [i.strip(".") for i in tokens]
    bigram = list(ngrams(tokens, 4))
    bigramList.append(bigram)


# print(bigramList)

for pairList in bigramList:
    for pair in pairList:
        bigram = convertTuple(pair)
        if pair[0] == "assigned" and pair[2] == "at" and pair[3] == "birth":
            if bigram not in AssignedDict.keys():
                AssignedDict[bigram] = 1
            if bigram in AssignedDict.keys():
                AssignedDict[bigram] = AssignedDict[bigram] + 1

with open("AssignedDictOutput.csv","w", newline="") as DictCsv:
    w = csv.writer(DictCsv)
    w.writerow(headers)
    for key, value in AssignedDict.items():
        w.writerow([key, value])
