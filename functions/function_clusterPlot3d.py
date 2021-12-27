def plot(dataPoints, clusterCenters, labels, plotClusters, colorDataPoints, title):
    
    from matplotlib import pyplot as plt
    import numpy as np, random

    X_D = []
    Y_D = []
    Z_D = []

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('x')
    ax.set_xlabel('y')
    ax.set_xlabel('z')

    if plotClusters:
        clusterCenterPoints = {}   
        for c in clusterCenters:
            clusterCenterPoints[c] = '#' + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:]

        X_C = []
        Y_C = []
        Z_C = []

        for x,y,z in clusterCenters:
            X_C.append(x)
            Y_C.append(y)
            Z_C.append(z)

        for i,c in enumerate(clusterCenterPoints):
            ax.scatter(X_C[i], Y_C[i], Z_C[i], s = 200, c = clusterCenterPoints[c], marker = "x")

    if not colorDataPoints:
        for x,y,z in dataPoints:
            X_D.append(x)
            Y_D.append(y)
            Z_D.append(z)

        ax.scatter(X_D, Y_D, Z_D, s = 30, c = 'k', marker = "o")
    else:
        pts = []

        for i,c in enumerate(clusterCenters):
            pts.clear()
            X_D.clear()
            Y_D.clear()
            Z_D.clear()

            for l in labels:
                if labels[l] == i:
                    pts.append(l)

            for x,y,z in pts:
                X_D.append(x)
                Y_D.append(y)
                Z_D.append(z)

            ax.scatter(X_D, Y_D, Z_D, s = 30, c = clusterCenterPoints[c], marker = "o")

    plt.title(title)
    plt.show()

#####################

import os, random, numpy as np
import function_kMeans3d as km

E = []
k = 7 # number of clusters

#Create random 3D-Datapoints
n = 500 # number of data_points
for i in range(n):
    random_x = random.randint(0,100)
    random_y = random.randint(0,100)
    random_z = random.randint(0,100)
    point = (random_x, random_y, random_z)
    E.append(point)

L = {} #Assignment
C = [] #Clusters
L, C = km.AssignClusters(E, k)

plot(E, C, L, True, False, "Test")