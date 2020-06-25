import fasttext
import pandas as pd
import numpy as np
import re
import csv
import math

model_filepath = '/home/mforkin/LOR/fasttext/crawl-300d-2M-subword.bin'
maleDataPath = '/home/mforkin/LOR/data/all-split/bigTxtMale/data.csv'
femaleDataPath = '/home/mforkin/LOR/data/all-split/bigTxtFemale/data.csv'

model = fasttext.load_model(model_filepath)

#femaleData = pd.read_csv(femaleDataPath, quotechar='"', escapechar='\\', doublequote=False)
#maleData = pd.read_csv(maleDataPath, quotechar='"', escapechar='\\', doublequote=False)
maleDocs = {}
femaleDocs = {}
maleEmbedding = np.array([0]*300, dtype='f')
femaleEmbedding = np.array([0]*300, dtype='f')

with open(maleDataPath) as csvf:
    r = csv.reader(csvf, delimiter=',', quotechar='"', escapechar='\\', doublequote=False)
    for row in r:
        document = row[1]
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(document))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()
        maleDocs[row[0]] = [word for word in document.split(' ') if len(word) > 3]

with open(femaleDataPath) as csvf:
    r = csv.reader(csvf, delimiter=',', quotechar='"', escapechar='\\', doublequote=False)
    for row in r:
        document = row[1]
        # Remove all the special characters
        document = re.sub(r'\W', ' ', str(document))

        # remove all single characters
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

        # Remove single characters from the start
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

        # Substituting multiple spaces with single space
        document = re.sub(r'\s+', ' ', document, flags=re.I)

        # Removing prefixed 'b'
        document = re.sub(r'^b\s+', '', document)

        # Converting to Lowercase
        document = document.lower()
        femaleDocs[row[0]] = [word for word in document.split(' ') if len(word) > 3]

i = 0
md = 0
fd = 0
print('mdl: ' + str(len(maleDocs)))
for k in maleDocs:
    v = maleDocs[k]
    i = i + 1
    if i < (len(maleDocs) / 2):
        md = md + 1
        for w in v:
            vec = model[w]
            for idx, e in enumerate(vec):
                maleEmbedding[idx] = maleEmbedding[idx] + e

for i, e in enumerate(maleEmbedding):
    maleEmbedding[i] = e / md

i = 0
for k in femaleDocs:
    v = femaleDocs[k]
    i = i + 1
    if i < (len(femaleDocs) / 2):
        fd = fd + 1
        for w in v:
            vec = model[w]
            for idx, e in enumerate(vec):
                femaleEmbedding[idx] = femaleEmbedding[idx] + e

for i, e in enumerate(femaleEmbedding):
    femaleEmbedding[i] = e / fd

mt = 0
ft = 0
i = 0

cm = 0
incm = 0
cf = 0
incf = 0

def getDiff(v, vec):
    res = 0
    for idx, e in enumerate(v):
        res = res + math.sqrt((e - vec[idx]) * (e - vec[idx]))
    return res

print ('mfdif: ' + str(getDiff(maleEmbedding, femaleEmbedding)))

for k in maleDocs:
    v = maleDocs[k]
    i = i + 1
    if i > (len(maleDocs) / 2) or True:
        docVec = np.array([0]*300, dtype='f')
        dl = 0
        for w in v:
            vec = model[w]
            dl = dl + 1
            for idx, e in enumerate(vec):
                docVec[idx] = docVec[idx] + e
        for idx, e in enumerate(docVec):
            docVec[idx] = docVec[idx] / dl
        malediff = getDiff(docVec, maleEmbedding)
        femalediff = getDiff(docVec, femaleEmbedding)
        if malediff < femalediff:
            cm = cm + 1
        else:
            incm = incm + 1

i = 0
for k in femaleDocs:
    v = femaleDocs[k]
    i = i + 1
    if i > (len(femaleDocs) / 2):
        docVec = np.array([0]*300, dtype='f')
        dl = 0
        for w in v:
            vec = model[w]
            dl = dl + 1
            for idx, e in enumerate(vec):
                docVec[idx] = docVec[idx] + e
        for idx, e in enumerate(docVec):
            docVec[idx] = docVec[idx] / dl
        if getDiff(docVec, femaleEmbedding) < getDiff(docVec, maleEmbedding):
            cf = cf + 1
        else:
            incf = incf + 1

print('cm: ' + str(cm) + '\n')
print('incm: ' + str(incm) + '\n')
print('cf: ' + str(cf) + '\n')
print('incf: ' + str(incf) + '\n')




