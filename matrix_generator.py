# make vocabulary

import pandas as pd
import numpy as np
from collections import Counter
import pickle # pickle to save vocabulary
from math import log


##### ----- Pickle functions ------ 

# functions that will save the vocabulary or 
# into a pickle (binary) format, using the 
# module 'pickle'


def save_obj(obj,name):
    """
    Save the obj with in the path:
    'data/name.pkl'
    """

    with open ('data/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
        
def load_obj (name):
    """
    load the object from data/name.pkl
    """
    
    with open ('data/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
        


##### Make a vocabulary

def make_vocabulary(df):
    """
    takes as input a dataframe with a column
    called 'description stemmed' and creates
    a dictionary vocabulary in 'data/vocabuary.pkl' 
    """
    # vocabulary dict
    voc = {}
    # term_id initialized to 0
    cnt = 0
    
    for i in range(len(df)):
        
        # get the list 
        word_list = set(df.iloc[i].description_stemmed.split())
        
        for word in word_list:
            if word not in voc:
                voc[word] = cnt 
                cnt += 1
                
    save_obj(voc,'vocabulary')
    return


def make_TFIDF (df):
    """
    make from df.description_stemmed a TFIDF matrix
    input:
    - df, with a column named 'description_stemmed'
    output:
    - TFIDF as numpy matrix
    """

    # call the vocabulary
    voc = load_obj('vocabulary')

    # initialize a numpy matrix to zero
    n = len(df) # number of announcements
    tot_words = len(voc) # number of words
    s = (n, tot_words) # nrow and ncol
    TF_matrix = np.zeros(s)

    # words in all the announcements (with repetitions, max 1 word for each announcement)
    total_words_occurrencies = []

    # for each announcement
    for i in range(len(df)):

        # empty words_list
        words_list = []
        # create the list from the description (stemmed) string
        words_list = (df.iloc[i].description_stemmed).split()

        # map all the words to their vocabulary term_id  
        words_list = list(map(lambda x: voc[x], words_list))

        # the term_id is the index pointing the columns of TF matrix, IDF array and TFIDF matrix
        # use counter to count the TF with a dictionary
        counter_dict = Counter(words_list)

        # for each term_id in the dict, put into the current announcement (row(i))
        # the relative frequence of the word in the single announcement
        for term_id in counter_dict.keys():
            TF_matrix[i][term_id] = counter_dict[term_id] / len(words_list)

        # set the words (max 1 word for each announcement!) and add it the main list
        total_words_occurrencies += list(set(words_list))

    # Count the occurrencies 
    counter_dict = Counter(total_words_occurrencies)

    # initialize IDF_array
    IDF_array = np.zeros(tot_words)

    # for each term_id, fill IDF_array[term_id] with its occurrencies in counter_dict[term_id]
    for term_id in counter_dict.keys():
        IDF_array[term_id] = log(n/counter_dict[term_id])

    # broadcast operation: we can multiply each TFIDF row element wise with IDF_array
    TFIDF_matrix = TF_matrix*IDF_array
    
    return TFIDF_matrix


        
