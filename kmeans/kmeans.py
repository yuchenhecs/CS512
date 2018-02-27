#!/usr/bin/python


import numpy as np


from sklearn.cluster import KMeans
from sklearn import datasets


fname = 'phrase_YELP.txt'

with open(fname) as f:
    lines = f.readlines()

phrases = []
embeds = []

for l in lines:
    tokens = l.split()
    phrases.append(tokens[0])
    embeds.append(tokens[1:])

#print embeds

np.random.seed(5)

estimators = [('k_means_8', KMeans(n_clusters=8))]
labels = []
# fignum = 1
# titles = ['8 clusters', '3 clusters', '3 clusters, bad initialization']
for name, est in estimators:
    label = est.fit_predict(embeds)
    labels.append(label)
    print label
    print len(label)
#     fignum = fignum + 1

clusters = []
for label in labels:
    c = {}
    clusters.append(c)
    for i, l in enumerate(label):
        if l not in c:
            c[l] = []
        c[l].append(phrases[i])

print clusters[0][0]



