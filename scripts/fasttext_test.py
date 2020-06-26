import fasttext
import pandas as pd
import numpy as np
import re
import csv
import math
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import gensim

np.random.seed(2020)
stemmer = SnowballStemmer('english')

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

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def tokenize_document(doc_content):
    return [lemmatize_stemming(token) for token in gensim.utils.simple_preprocess(doc_content, deacc=True) if len(token) > 3 and token not in gensim.parsing.preprocessing.STOPWORDS]

def generate_embedding(doc):
    doc_embedding = np.array([0]*300, dtype='f')
    for word in doc:
        vector = model[word]
        for dim, emb_val in enumerate(vector):
            doc_embedding[dim] = doc_embedding[dim] + emb_val
    for dim, emb_val in enumerate(doc_embedding):
        doc_embedding[dim] = doc_embedding[dim] / len(doc)
    return doc_embedding

def generate_average_embedding(docs):
    average_embedding = np.array([0]*300, dtype='f')
    i = 0
    d = 0
    for k in docs:
        if (i < len(docs) / 2):
            i = i + 1
            d = d + 1
            doc_emb = generate_embedding(docs[k])
            for dim, emb_val in enumerate(doc_emb):
                average_embedding[dim] = average_embedding[dim] + emb_val
    for dim, emb_val in enumerate(average_embedding):
        average_embedding[dim] = emb_val / d
    return average_embedding

with open(maleDataPath) as csvf:
    r = csv.reader(csvf, delimiter=',', quotechar='"', escapechar='\\', doublequote=False)
    for row in r:
        document = row[1]
        maleDocs[row[0]] = tokenize_document(document)

with open(femaleDataPath) as csvf:
    r = csv.reader(csvf, delimiter=',', quotechar='"', escapechar='\\', doublequote=False)
    for row in r:
        document = row[1]
        femaleDocs[row[0]] = tokenize_document(document)

maleEmbedding = generate_average_embedding(maleDocs)
femaleEmbedding = generate_average_embedding(femaleDocs)

def getDiff(v, vec):
    res = 0
    for idx, e in enumerate(v):
        res = res + math.sqrt((e - vec[idx]) * (e - vec[idx]))
    return res

print ('diff male_general_emb vs female_general_emb: ' + str(getDiff(maleEmbedding, femaleEmbedding)))

def evaluate (docs, correct_vector, incorrect_vector):
    i = 0
    result = {}
    result['incorrect'] = 0
    result['correct'] = 0
    for k in docs:
        if i > len(docs) / 2:
            document_vector = generate_embedding(docs[k])
            correct_diff = getDiff(document_vector, correct_vector)
            incorrect_diff = getDiff(document_vector, incorrect_vector)
            if correct_diff < incorrect_diff:
                result['correct'] = result['correct'] + 1
            else:
                result['incorrect'] = result['incorrect'] + 1
        i = i + 1
    return result

male_results = evaluate(maleDocs, maleEmbedding, femaleEmbedding)
female_results = evaluate(femaleDocs, femaleEmbedding, maleEmbedding)

print('female_correct: ' + str(female_results['correct']) + '\n')
print('female_incorrect: ' + str(female_results['incorrect']) + '\n')
print('female percent_correct: ' + str(female_results['correct'] / (female_results['correct'] + female_results['incorrect'])))
print('male_correct: ' + str(male_results['correct']) + '\n')
print('male_incorrect: ' + str(male_results['incorrect']) + '\n')
print('male_percent_correct: ' + str(male_results['correct'] / (male_results['correct'] + male_results['incorrect'])))


