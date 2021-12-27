import os, random, numpy as np
import functions.function_kMeans3d as km, functions.function_clusterPlot3d as plt

E = []

#Create random 3D-Datapoints
n = 100 # number of data_points
for i in range(n):
    random_x = random.randint(0,100)
    random_y = random.randint(0,100)
    random_z = random.randint(0,100)
    point = (random_x, random_y, random_z)
    E.append(point)

plt.plot(km.AssignClusters(E, 4), "k-Means clustering")