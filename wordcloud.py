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