#!/usr/bin/python


#import numpy as np


from sklearn.cluster import KMeans

from sklearn import datasets

# np.random.seed(5)

# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

# estimators = [('k_means_iris_8', KMeans(n_clusters=8)),
#               ('k_means_iris_3', KMeans(n_clusters=3)),
#               ('k_means_iris_bad_init', KMeans(n_clusters=3))]

# fignum = 1
# titles = ['8 clusters', '3 clusters', '3 clusters, bad initialization']
# for name, est in estimators:
#     est.fit_predict(X)
#     labels = est.labels_

#     fignum = fignum + 1
