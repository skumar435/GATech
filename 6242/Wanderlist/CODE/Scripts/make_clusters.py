## make the clusters

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

df = coordinates[[0, 1, 2]]

kmeans = KMeans(n_clusters = 3)
kmeans.fit(df[[1,2]])

clusters = pd.concat([df, pd.DataFrame(kmeans.labels_)], axis=1)
clusters
# # clusters.to_csv('atlantapoi_cluster.csv', index=False, header=None)
# plt.scatter(df[1], df[2], c= kmeans.labels_.astype(float))
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red')