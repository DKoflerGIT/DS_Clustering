import os, random, numpy as np
from functions import f_kMeans as km, f_createRandomDatapoints as crd, f_clusterPlot as plt

dpts = []
dpts = crd.createDatapoints(500, 2) #currently 2+ work with kMeans, 2&3 with plot
kmeans = km.AssignClusters(dpts,2)
plt.plot(kmeans, 'k-Means clustering')