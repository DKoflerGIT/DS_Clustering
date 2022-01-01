from functions import kMeans as km

dpts = []
dpts = km.createRandomDatapoints(500, 2) #kMeans works for 2+ dimensions, for 1 dimension not always. plot works for 2 or 3 dimensions
#clusterAmount = km.findOptimalClusterAmount(dpts)
kmeans = km.AssignClusters(dpts, 5, False)
km.plotClusters(kmeans)