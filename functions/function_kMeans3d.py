def AssignClusters(E, k):
    import random
    import math

    C = []
    L = {}

    def euclidean_distance(data_point_a, data_point_b): #calculates euclidean distance
        x_a = data_point_a[0]
        y_a = data_point_a[1]
        z_a = data_point_a[2]
        x_b = data_point_b[0]
        y_b = data_point_b[1]
        z_b = data_point_b[2]
        
        eucl_dist = round(math.sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2 + (z_a - z_b) ** 2),2)
        
        return eucl_dist

    def selectRandomCenters(k): # returns k random data points from all data points E
        return random.sample(E, k)

    # Choose random datapoints as starting cluster centers
    C = selectRandomCenters(k)

    def argminDistance(e): # returns index of closest cluster for a given datapoint
        minDist = 100

        for c in C:
            dist = euclidean_distance(e,c)
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

        sumX = 0
        sumY = 0
        sumZ = 0

        for x,y,z in pts:
            sumX += x
            sumY += y
            sumZ += z
        
        newPos = (round(sumX/len(pts),0),round(sumY/len(pts),0),round(sumZ/len(pts),0))
        return newPos

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