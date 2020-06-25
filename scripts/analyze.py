import pandas as pd
import re

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models

from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *

import numpy as np
np.random.seed(2020)

stemmer = SnowballStemmer('english')

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    result = []
    document = text
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

    for token in gensim.utils.simple_preprocess(document):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


femaleDataPath = '/home/mforkin/LOR/data/all-split/bigTxtFemale/data.csv'
maleDataPath = '/home/mforkin/LOR/data/all-split/bigTxtMale/data.csv'
resultsDirTfidf = '/home/mforkin/LOR/data/all-split/bigTxtFemale/resultsTfIdf.txt'
resultsDirBow = '/home/mforkin/LOR/data/all-split/bigTxtFemale/resultsBOW.txt'

femaleData = pd.read_csv(femaleDataPath, quotechar='"', escapechar='\\', doublequote=False)
data_text = femaleData[['content']]
data_text['index'] = data_text.index
documents = data_text

print("Num Female Documents --------------")
print(len(documents))

processed_docs = documents['content'].map(preprocess)

dictionary = gensim.corpora.Dictionary(processed_docs)

count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 10:
        break

dictionary.filter_extremes(no_below=50, no_above=0.65, keep_n=100000)

bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = models.TfidfModel(bow_corpus)

corpus_tfidf = tfidf[bow_corpus]

lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=15, id2word=dictionary, passes=2, workers=2)

print('Bag Of Words ------------------')
with open(resultsDirBow, 'w') as bowOut:
    for idx, topic in lda_model.print_topics(-1):
        bowOut.write('Topic:')
        bowOut.write(str(idx))
        bowOut.write('Words:')
        bowOut.write(topic)
        bowOut.write('\n')
        print('Topic: {} \nWords: {}'.format(idx, topic))

print('TFIDF --------------------------')
lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=15, id2word=dictionary, passes=2, workers=4)

with open(resultsDirTfidf, 'a') as tfidfOut:
    for idx, topic in lda_model_tfidf.print_topics(-1):
        tfidfOut.write('Topic:')
        tfidfOut.write(str(idx))
        tfidfOut.write('Words:')
        tfidfOut.write(topic)
        tfidfOut.write('\n')
        print('Topic: {} \nWords: {}'.format(idx, topic))


