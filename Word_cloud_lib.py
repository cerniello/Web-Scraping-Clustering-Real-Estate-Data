import numpy as np
import pandas as pd
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def jaccard_similarity(set1, set2):
    
    set1 = set(set1)
    set2 = set(set2)
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    jaccard_similarity = len(intersection)/float(len(union))
    return jaccard_similarity



def compute_jaccard_similarities(features_clusters, TFIDF_clusters):
    
    lst_of_clusters_1 = features_clusters.keys()
    lst_of_clusters_2 = TFIDF_clusters.keys()
    
    jaccard_scores_list = []
    
    for cl1 in lst_of_clusters_1:
        for cl2 in lst_of_clusters_2:
            
            
            j_score = jaccard_similarity(features_clusters[cl1], TFIDF_clusters[cl2])
            
            jaccard_scores_list.append(tuple([cl1,cl2,j_score]))
    
    jaccard_scores_list.sort(key = lambda x: x[2], reverse=True)
    return jaccard_scores_list


def doWordcloud(text):
    #text = " ".join(words for words in w)
    # Create stopword list:
    stopwords = set(STOPWORDS)

    house_mask = np.array(Image.open("house.png"))


    wc = WordCloud(background_color="white", max_words=500, mask=house_mask,
                   stopwords=stopwords, contour_width=3, contour_color='firebrick')
    # Generate a wordcloud
    wc.generate(text)

    # show
    fig = plt.figure(figsize=[20,10])
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.axis("off")
    fig.show()
    
    return

def setWordcloud (Jdf, lista_cluster1, lista_cluster2):
    annunci = []
    annunci += lista_cluster1
    annunci += lista_cluster2
    annunci = set(annunci)

    des = str()
    for i in annunci:
        des += str(Jdf.iloc[i]['description'])
    
    print(len(des))
    print(des[:100])
    doWordcloud(des)
    
    return