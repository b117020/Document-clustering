# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:32:29 2019

@author: Devdarshan
"""
#import modules
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from clustering import *

#Using elbow method to find the optimum number of k
X=tfidf
Sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X)
    Sum_of_squared_distances.append(km.inertia_)

plt.plot(K, Sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum_of_squared_distances')
plt.title('Elbow Method For Optimal k')
plt.show()