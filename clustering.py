# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:12:42 2019

@author: Devdarshan
"""

#import modules
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


#read data
df = pd.read_csv('final1.csv')
corpus=[]
for index,row in df.iterrows():
    corpus.append(row['data'])

#vectorisation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
#vectorizer.get_feature_names()
#print(X.toarray())     
transformer = TfidfTransformer(smooth_idf=False)
tfidf = transformer.fit_transform(X)
print(tfidf.shape )                        

# K-means clustering
num_clusters = 8 #found using elbow method
k = KMeans(n_clusters=num_clusters)
k.fit(tfidf)
clusters = k.labels_.tolist()

#Creating dict having doc with the corresponding cluster number
idea={'data':corpus, 'Cluster':clusters} 
frame=pd.DataFrame(idea,index=[clusters], columns=['data','Cluster']).values.tolist()
dt = pd.DataFrame(frame,columns=['data','Cluster'])

#Print the doc with the labeled cluster number
print(dt) 
#Print the counts of doc belonging to each cluster
print(dt['Cluster'].value_counts()) 

#saving final results as csv
dt.to_csv('results.csv', index = False)
