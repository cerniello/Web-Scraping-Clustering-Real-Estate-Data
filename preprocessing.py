import pandas as pd
import numpy as np
import string

from nltk.stem.snowball import ItalianStemmer
from nltk.corpus import stopwords
#from nltk.stem import ItalianStemmer
from nltk.tokenize import word_tokenize

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



###### features functions (which preprocess single value)

# price_preprocessing
def price_prep(s):
    
    # removing punctuation and symbols
    s = s.replace('.','')
    s = s.replace('€','')
    s = s.strip(' ')
    s = s.split('-')

    # return first value
    # or the mean between the two
    if len(s) == 1:
        return float(s[0])
    else: # if we have two values, compute the average
        min_price = float(s[0])
        max_price = float(s[1])
    return (min_price+max_price)/2


# locali preprocessing
def locali_preproc(s):
    s = s.strip()
    s = s.replace('+','')
    return int(s[len(s)-1])



# no need superficie (already float values)

# bagni preproc on place


# piano preprocessing
def piano_preproc(x):
    
    x = str(x)
    x = x.strip()
    
    if x == 'T':
        return 0
    elif x == 'A' or x == '11+':
        return np.nan #return nan
    elif x == 'R':
        return 0.5
    elif x == 'S':
        return -1
    else:
        return float(x)


# description preprocessing DEPRECATED
def description_preproc(description):

    description = description.strip()
    description = description.replace("\n", " ")
    description = description.replace('\r', " ")
    description = description.replace('’', " ")
    
    sp = string.punctuation+'“”–’°•€'
    punctuation_remover = str.maketrans('', '', sp)
    
    description = description.split(' ')
    
    # removing punctuation
    description = [ word.translate(punctuation_remover) for word in description ]
    
    #removing empty spaces in the list 
    description = filter(None, description)
    
    # Italian stemmer
    stemmer = ItalianStemmer()
    # stemmed list
    stemmed_list = [stemmer.stem(word) for word in description]
    
    
    return ' '.join(stemmed_list)


# from previous hw, we can reuse our code
def remove_step(doc):
    """
    takes as input the string of the document
    removes stopwords, punctuation and makes stemming 
    input:
    - string of document
    output:
    - list of term after stemming process
    
    """
    
    # check if it's a nan value 

    if isinstance(doc, float):
        return str(doc)
    
    sp = string.punctuation+'“”–’°•€'
    
    doc=doc.replace("\\n", " ")
    # punctuations
    doc = [ c if c not in sp else " " for c in doc ]
    doc = ''.join(doc)
    # stopwords
    doc = [ word for word in doc.split() if word.lower() not in stopwords.words('italian') ]
    doc = ' '.join(doc)
    
    # stemming
    ps = ItalianStemmer()
    words = word_tokenize(doc)
    
    w_lst = []
    for w in words:
        w_lst.append(ps.stem(w))
    
    # something else
    
    return ' '.join(w_lst)


###### PREPROCESSING FUNCTION 

def preprocess_raw_data():
    
    # load csv file
    df = pd.read_csv('data/raw_data.csv')

    # delete rows with na values
    df.dropna(inplace=True)

    # price prep
    df = df[df.price.str.contains('[a-zA-Z]') == False]
    df.price = df.price.map(price_prep)
    df = df[df.price > 2000 ]

    # locali prep
    df.locali = df.locali.map(locali_preproc)

    # superficie doesn't needs prep

    # bagni prep
    df.bagni = df.bagni.map(lambda x: int(x[0]))

    # piano prep
    df.piano = df.piano.map(piano_preproc)

    # stemming description
    df['description_stemmed'] = df.description.map(description_preproc)
    #remove na
    df.dropna(inplace=True)
    #df.drop('Unnamed: 0', axis = 1, inplace=True) 

    df.to_csv('data/data_preprocessed.csv', index=False)
    
    return

