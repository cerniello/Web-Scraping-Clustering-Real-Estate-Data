import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import math

# transform data

def transform_data(df_features):
    """
    function used to transform data
    """
    
    mms = StandardScaler()
    mms.fit(df_features)
    data_transformed = mms.transform(df_features)
    
    return data_transformed


def elbow_method (data, max_clusters = 10, TFIDF = False, figsize=(12,8)):
    
    n_ann = len(data)
    n_features = len(data.iloc[0])
    plot_labels = [ ['Number of clusters', 'Inertia (ssd)', 'Elbow-Method for features_dataframe'],
                    ['Number of clusters', 'Inertia (ssd)',
                     'Elbow Method for %d announcements based on %d features'%(n_ann,n_features)]]
    
    labels_idx = 0
    
    if TFIDF == True:
        labels_idx = 1
       
                                                               
    sd = {}
    
    K_trials = range(2,max_clusters)
    
    for k in K_trials:
        model = KMeans(n_clusters=k, init='k-means++')
        model = model.fit(data)
        sd[k] = model.inertia_
        
        
    # plotting the elbow method
    
    fig = plt.figure(figsize=figsize)
    x = list(sd.keys())
    y = list(sd.values())
    
    plt.plot(x, y, 'bx-')
    plt.xlabel(plot_labels[labels_idx][0], size=15)
    plt.ylabel(plot_labels[labels_idx][1], size=13)
    plt.title(plot_labels[labels_idx][2], size=15)
    plt.grid(linestyle='--', linewidth=2,color='lightgray', zorder = 0)    
    
    
    # in case of features dataframe we already know that the appropriate
    # number of clusters is 8 so we put a circle on that position
    if TFIDF is False:
        plt.plot(x[3], y[3], 'o', ms = 30, mec='r', mfc='none', mew=2)
        plt.xticks(np.arange(2,max_clusters))
    
    plt.show()
    
    return 




def count_plot_words_occurrencies (df, figsize=(15,8), xstart=None, xend=None):
    """
    for each word in tfidf dataframe it counts the occurencies
    of the words in all the announcements
    input:
    - df: dataframe (TFIDF_dataframe)
    - figsize: dimension of the plot
    - xticks_start: axis x attribute for the plot (default value: 0)
    - xticks_end:   axis x attribute for the plot (default value: number of columns)
    - steps:        axis x attribute for the plot (default value: 1000)
   
    """
         
    words_counting = []

    # put NaN values if there's 0
    df = df.where(df != 0)
 
    for i in df:
        # count values != from 0 (!= from NaN)
        cnt_word = df.loc[:,i].count()
        words_counting.append(int(cnt_word))
        
    # if there is no input about axis x attributes
    # assign to axix attributes default values 
    if xstart is None:
        xstart = 0 
    if xend is None:
        xend = len(df.iloc[0])

    f = plt.figure(figsize=figsize)
 
    x = range(xstart, xend)

    plt.plot(x,words_counting,'ro')
    
    plt.xlabel('Word_ID', size = 15)
    plt.ylabel('Announcements containing the word_ID', size = 10)
    plt.title('Distribution of the words over the announcements', size=12)
    
    plt.grid(linestyle='--', linewidth=2,color='lightgray', zorder = 0)    

    plt.show()
    plt.close()
    
    return




def detect_weak_features (df, threshold=2):
    """
    function used in clean_TFIDF.
    it returns the list of df's features (columns) 
    that don't respect the threshold:
    
    input:
    - df: TFIDF_dataframe with m features (m columns - words)
    - threshold: minimum number of announcements in which 
                 the feature (word) occurs
    
    output:
    - list of features (words) that recurs in announcements 
      less times than the threshold
    """
    
    col_to_delete = []
    n_features = len(df.iloc[0])
    n_announcements = len(df)
    
    # pick all the values != 0 and leave the other
    # cells putting NaN instead of 0 
    df = df.where(df != 0)

    for col_id in df:

        # count() counts all the !(NaN) values in the i-column,
        # which are the announcement which contains the term
        cnt_word = df.loc[:,col_id].count()
        if  cnt_word < threshold :
            col_to_delete.append(col_id)

    return col_to_delete


def clean_TFIDF(TFIDF_dataframe, threshold = None, messages = True):
    """
    remove words under a certain threshold
    input:
    - TFIDF_dataframe
    - threshold: default None, if None, the default value
                 is the 1% of the columnlen of TFIDF
    - messages: if True it shows how many features you're removing
    output:
    - a new df with less columns
    this function is used also in TFIDF_elbow_method_scenarios
    """
    
    total_announcements = len(TFIDF_dataframe)
    n_features = len(TFIDF_dataframe.iloc[0]) 
    
    if threshold == None:
        threshold = total_announcements * 0.01
        
    col_to_delete = detect_weak_features(TFIDF_dataframe, threshold = threshold)
    
    if messages == True:
        print('We drop out %d (over %d) features which recurs in less than %d announcements (over %d)'
               %(len(col_to_delete),n_features, threshold, total_announcements))
    
    return TFIDF_dataframe.drop(columns=col_to_delete, axis=1)
    

# plot 5 elbow-methods

def TFIDF_elbow_method_scenarios (TFIDF_dataframe):
    """
    Function that plots 4 different scenarios
    changing the value of th threshold
    
    """
    
    total_announcements = len(TFIDF_dataframe)
    
    
    # 0. Elbow method with 3000 features, words that recurs in less than 5% of the announcements
    threshold = int(total_announcements) * 0.05
    new_TFIDF = clean_TFIDF(TFIDF_dataframe, threshold)
    #elbow method with a new_TFIDF
    elbow_method(new_TFIDF, max_clusters=10, TFIDF=True, figsize=(12,6))
    
    
    
    ## 1. Elbow method with 500 features, words that recurs in less than 3% of the announcements
    threshold = int(total_announcements * 0.03)
    new_TFIDF = clean_TFIDF(TFIDF_dataframe, threshold)
    #elbow method with a new_TFIDF
    elbow_method(new_TFIDF, max_clusters=10, TFIDF=True, figsize=(12,6))
    
    
    ## 2. Elbow method with 1000 features, words that recurs in less than 1% of the announcements
    threshold = int(total_announcements * 0.01)
    new_TFIDF = clean_TFIDF(TFIDF_dataframe, threshold)
    #elbow method with a new_TFIDF
    elbow_method(new_TFIDF, max_clusters=10, TFIDF=True, figsize=(12,6))
    
    
    ## 3. Elbow method with 2000 features, words that recurs in less than 4 announcements
    threshold = 4
    new_TFIDF = clean_TFIDF(TFIDF_dataframe, threshold)
    #elbow method with a new_TFIDF
    elbow_method(new_TFIDF, max_clusters=10, TFIDF=True, figsize=(12,6))
    
    
    ## 4. Elbow method with 1000 features, words that recurs in less than 2 announcements
  
    threshold = 2
    new_TFIDF = clean_TFIDF(TFIDF_dataframe, threshold)
    #elbow method with a new_TFIDF
    elbow_method(new_TFIDF, max_clusters=10, TFIDF=True, figsize=(12,6))
    

    return





