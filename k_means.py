import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans


# transform data

def transform_data(df_features):
    """
    function used to transform data
    """
    
    mms = StandardScaler()
    mms.fit(df_features)
    data_transformed = mms.transform(df_features)
    
    return data_transformed


def elbow_method (data, max_clusters = 10, TFIDF = False, threshold=2, figsize=(12,8)):
    
    n_ann = len(data)
    n_features = len(data)
    plot_labels = [ ['Number of clusters', 'Inertia', 'Elbow-Method for features dataframe'],
                    ['Number of clusters', 'Inertia',
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
    plt.ylabel(plot_labels[labels_idx][1], size=10)
    plt.title(plot_labels[labels_idx][2], size=15)
    plt.grid(linestyle='--', linewidth=2,color='lightgray', zorder = 0)    
    
    
    # in case of features dataframe we already know that the appropriate
    # number of clusters is 8 so we put a circle on that position
    if TFIDF is False:
        plt.plot(x[2], y[2], 'o', ms = 30, mec='r', mfc='none', mew=2)
        plt.xticks(np.arange(2,max_clusters))
    
    plt.show()
    
    return 




def count_plot_words_occurrencies (df, figsize=(15,8)):
    """
    for each word in tfidf dataframe it counts the occurencies
    of the words
    """
    words_counting = []

    # put NaN values if there's 0
    df = df.where(df != 0)

    for i in df:
        # count values != from 0 (!= from NaN)
        cnt_word = df.loc[:,i].count()
        words_counting.append(cnt_word)

    f = plt.figure(figsize=figsize)
    plt.plot(words_counting,'ro')

    plt.xlabel('Word_ID')
    plt.ylabel('Announcements containing the word_ID')
    plt.title('Distribution of the words over the announcements')

    plt.plot()
    
    return




    
    
    
    
    
    
    


def detect_weak_features (df, threshold=2):
    """
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

