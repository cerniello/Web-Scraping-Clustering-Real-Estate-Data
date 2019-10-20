# Unsupervised_Learning

4th homework for Alogithm of Data Minig @LaSapienza University

Hw structured in two parts:
1) First part related on Unsupervised Learning (K-means application) related with house data scraped from interned
2) Find password duplicates - **this part has been updated in a new repository by my colleague [paologentleman](https://github.com/paologentleman/Bloom-FIlter-Algorithm) **

##  Lohith Machani Sreennivasalu
##  Michele Cernigliero
##  Paolo Gentile



![alt text](https://1sd06y38jhbh1xhqve6fqmc1-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/fallingwater-1440x640.jpg)


Since there were different and indipendent tasks, we decided to split our work in different files:

* ADM_HW4.ipynb 
* scraping.py
* preprocessing.py
* matrix_generator.py
* k_means.py
* Word_cloud_lib.py
* DuplicateModule.py
* SeekDuplicatesAlgorithm.py
* data/

***

**ADM_HW4.ipynb**:

The Jupyter notebook which contains the key steps of our work and where we explain each decision we have made. It shows our outcomes and our results.

**scraping.py**:

Module which contains the functions that scrape the information from the website www.immobiliare.it. Informations are stored into a csv file with path 'data/raw_data.csv'.

**preprocessing.py**

Module which contains the functions used to preprocess the raw data. The preprocessed dataframe will be stored into the csv file under the path 'data/data_preprocessed.csv'.


**matrix_generator.py**

Module which has the functions used to compute the two matrixes.

**k_means.py**

This set of functions are responsable to compute the clustering part using the kmeans++ algorithm with sklearn library.

**Word_cloud_lib.py**

Package of functions used for the Jaccard Similarity and for rendering the wordcloud frames.

**DuplicateModule.py & SeekDuplicatesAlgorithm.py**

The first file rapresents the module containing the functions to check the passwords set seeking for duplicates. The second file contains the class that builds the data structur and the hash function.

**data/**

Folder directory which contains all the data that we used/elaborated in this homework

- raw_data.csv 
- data_preprocessed.csv
- vocabulary.pkl (pikle (binary) format to store the dictionary of stemmed words)
	
