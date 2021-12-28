# Verson 1.4
# D. Kofler 2021
# Now works for n-dimensional datapoints

def AssignClusters(E, k = 1):
    import random
    import math

    C = []
    L = {}

    dim = len(E[0]) #dimensionality of the data points

    def euclidean_distance(dataPoint1, dataPoint2): #calculates euclidean distance
        pts = []
        
        for d in range(dim):
            pts.append((dataPoint1[d],dataPoint2[d]))

        sumSquares = 0
        for i,p in enumerate(pts):
            sumSquares += (p[1] - p[0]) ** 2

        return round(math.sqrt(sumSquares),2)

    def selectRandomCenters(k): # returns k random data points from all data points E
        return random.sample(E, k)

    # Choose random datapoints as starting cluster centers
    C = selectRandomCenters(k)

    def argminDistance(dataPoint): # returns index of closest cluster for a given datapoint
        minDistCenter = C[0]
        minDist = euclidean_distance(dataPoint,minDistCenter)

        for c in C:
            dist = euclidean_distance(dataPoint,c)
            if dist < minDist:
                minDist = dist
                minDistCenter = c
                
        return C.index(minDistCenter)

    # Find closest cluster for each datapoint
    for e in E:
        L[e] = C[argminDistance(e)]

    def UpdateCluster(c): # moves given cluster to mean position of its current corresponding datapoints
        pts = []

        for l in L:
            if L[l] == c:
                pts.append(l)

        sums = []
        newPosList = []

        for d in range(dim):
            sums.append(0)
            
            for p in pts:
                sums[d] += p[d]
            newPosList.append(round(sums[d] / len(pts),2))

        return tuple(newPosList)

    # optimize cluster-positions
    iter = 0
    maxIters = 100

    while True:
        changed = False

        # Update clusters
        for i,c in enumerate(C):
            C[i] = UpdateCluster(c)

        # Update minDist
        for e in E:
            minDist = euclidean_distance(e,C[argminDistance(e)])

            if minDist != euclidean_distance(e,L[e]):
                L[e] = C[argminDistance(e)]
                changed = True

        iter += 1

        if not changed or iter > maxIters:
            break
    
    return L