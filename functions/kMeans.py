# Verson 1.5
# D. Kofler 2021

from matplotlib import pyplot as plt
import numpy, random, math

def createRandomDatapoints(amount, dimentionality): # creates random datapoints
    E = []
    pt = []

    for a in range(amount):
        pt.clear()
        for d in range(dimentionality):
            pt.append(random.randint(0,100))
        E.append(tuple(pt))
    
    return E


def euclideanDistance(dataPoint1, dataPoint2): # calculates euclidean distance
    pts = []
    
    dim = len(dataPoint1) #dimensionality of the data points

    for d in range(dim):
        pts.append((dataPoint1[d],dataPoint2[d]))

    sumSquares = 0
    for i,p in enumerate(pts):
        sumSquares += (p[1] - p[0]) ** 2

    return round(math.sqrt(sumSquares),2)


def AssignClusters(dataPoints, clusterAmount, optimize): # assigns datapoints to clusters using a k-Means algorithm
    C = []
    L = {}
    E = dataPoints
    k = clusterAmount

    dim = len(E[0]) #dimensionality of the data points

    def selectRandomCenters(k): # returns k random data points from all data points E
        return random.sample(E, k)

    def selectInitialCenters(k): # returns k data points as initial cluster centers based on kMeans++ 
        initialClusters = []
        weights = []
        weightsp = []
        initialClusters.append(random.choice(E)) # add random datapoint as first inital cluster center

        # print('initial cluster ' +
        #     str(E.index(initialClusters[0])) +
        #     ' at (' +
        #     str(initialClusters[0][0]) +
        #     ',' +
        #     str(initialClusters[0][1]) +
        #     ')'
        # )

        iter = 1
        
        while iter < k:
            iter = iter + 1
            weights.clear()
            weightsp.clear()
            
            # Sum of all D(X)^2
            sumDx2 = 0
            for e in E: 
                e_minDist = euclideanDistance(e, initialClusters[0])

                # find distance to closest cluster center
                for c in initialClusters:
                    e_dist = euclideanDistance(e, c)

                    if e_dist < e_minDist:
                        e_minDist = e_dist
                
                # add minDist^2 to sum of all minDist^2
                sumDx2 += e_minDist ** 2

            # D(X)^2 for current point
            for e in E:    
                Dx2 = 0
                e_minDist = euclideanDistance(e, initialClusters[0])

                # find distance to closest cluster center
                for c in initialClusters: 
                    e_dist = euclideanDistance(e, c)

                    if e_dist < e_minDist:
                        e_minDist = e_dist
                
                Dx2 = e_minDist ** 2
                w = round(Dx2 / sumDx2, 4)
                weights.append(w)
                weightsp.append((round(w * 100, 2), int(Dx2)))
            
            # for i, w in enumerate(weightsp):
            #     print(str(i) + ' - ' + str(w[0]) + ' - d: ' + str(w[1]))
            ic = random.choices(E, weights = weights, k = 1)[0]
            # print('chose cluster ' +
            #     str(E.index(ic)) +
            #     ' at (' +
            #     str(ic[0]) +
            #     ',' +
            #     str(ic[1]) +
            #     ') with probabiltiy ' +
            #     str(weightsp[E.index(ic)][0]) +
            #     ' %'
            # )
            initialClusters.append(ic)

        return initialClusters

    # Choose datapoints as starting cluster centers
    C = selectInitialCenters(k)

    def argminDistance(dataPoint): # returns index of closest cluster for a given datapoint
        minDistCenter = C[0]
        minDist = euclideanDistance(dataPoint,minDistCenter)

        for c in C:
            dist = euclideanDistance(dataPoint,c)
            if dist < minDist:
                minDist = dist
                minDistCenter = c
                
        return C.index(minDistCenter)

    # Find closest cluster for each datapoint
    for e in E:
        L[e] = argminDistance(e)

    def UpdateCluster(c): # moves given cluster to mean position of its current corresponding datapoints
        pts = []

        for l in L:
            if C[L[l]] == c:
                pts.append(l)

        sums = []
        newPosList = []

        for d in range(dim):
            sums.append(0)
            
            for p in pts:
                sums[d] += p[d]

            if sums[d] == 0:
                newPosList.append(50)
            else:
                newPosList.append(round(sums[d] / len(pts), 2))

        return tuple(newPosList)

    # optimize cluster-positions
    iter = 0
    maxIters = 100

    while optimize:
        changed = False

        # Update clusters
        for i,c in enumerate(C):
            C[i] = UpdateCluster(c)

        # Update minDist
        for e in E:
            minDist = euclideanDistance(e,C[argminDistance(e)])

            if minDist != euclideanDistance(e,C[L[e]]):
                L[e] = argminDistance(e)
                changed = True

        iter += 1

        if not changed or iter > maxIters:
            break
    
    ResDict = {}
    for l in L:
        ResDict[l] = C[L[l]]

    return ResDict


def findOptimalClusterAmount(E): # finds the optimal amount of clusters using the WCSS-method
    
    assinments = {}
    wcssDict = {}
    for i in range(2, 11): #try with up to 10 clusters
        assinments.clear()
        assinments = AssignClusters(E, i, True)

        wcss = 0
        for e in E:
            wcss += int(euclideanDistance(e, assinments[e]) ** 2)

        wcssDict[i] = wcss

        if i == 2:
            optimalClusterAmount = 10
        else:
            if optimalClusterAmount == 10 and wcssDict[i - 1] - wcss < wcssDict[2] / 10:
                optimalClusterAmount = i - 1

    print('Optimal number of clusters (change in WCSS < 10%): ' + str(optimalClusterAmount))

    X = []
    Y = []

    for w in wcssDict:
            X.append(w)
            Y.append(wcssDict[w])   

    plt.plot(X, Y, c = 'k')
    plt.title('Within Cluster Sum of Squares')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

    return optimalClusterAmount


def plotClusters(assignmentDict, annotations): # creates 2D or 3D plots of clusters and their assigned datapoints
    dataPoints = []
    clusterCenters = []

    for a in assignmentDict: 
        if (a not in dataPoints): #get data points from dict
            dataPoints.append(a)

        if (assignmentDict[a] not in clusterCenters): #get cluster centers from dict
            clusterCenters.append(assignmentDict[a])     

    dim = len(dataPoints[0]) #dimensionality of the data points
    if dim > 3:
        return

    clusterColors = {}

    for c in clusterCenters: #assign random colors to each cluster
        numbers = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        clusterColors[c] = '#' + ''.join('{:02X}'.format(n) for n in numbers)

    pts = []
    dataPointsPlot = []

    fig = plt.figure(figsize=(10,10))
    if (dim == 3):
        ax = fig.add_subplot(projection='3d')

    for i,c in enumerate(clusterCenters):
        pts.clear()
        dataPointsPlot.clear()

        for a in assignmentDict: # get datapoints assigned to current cluster
            if assignmentDict[a] == c:
                pts.append(a)

        for d in range(dim):
            dataPointsPlot.append([])
            for p in pts:   
                dataPointsPlot[d].append(p[d])

        #plot
        match dim:
            case 1: ##not working yet
                plt.scatter(c[0], s = 200, c = clusterColors[c], marker = 'x')
                plt.scatter(dataPointsPlot[0], s = 30, c = dataPointsPlot[c], marker = 'o')

            case 2:
                if annotations:
                    s1 = 500
                    s2 = 200
                else:
                    s1 = 200
                    s2 = 50

                #cluster-centers
                plt.scatter(c[0], c[1], s = s1, c = clusterColors[c], marker = 'o') #s = 200 when using annotations

                #data-points
                plt.scatter(dataPointsPlot[0], dataPointsPlot[1], s = s2, c = 'w', edgecolors = clusterColors[c], marker = 'o') #s = 200 when using annotations

                plt.xlabel('x')
                plt.ylabel('y')
                plt.title('2D k-Means-clustering')

            case 3:
                ax.scatter(c[0], c[1], c[2], s = 200, c = clusterColors[c], marker = 'x', alpha = 1, depthshade = False)
                ax.scatter(dataPointsPlot[0], dataPointsPlot[1], dataPointsPlot[2], s = 30, c = clusterColors[c], marker = 'o', alpha = 1, depthshade = False)

                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')

                plt.title('3D k-Means-clustering')
    
    if annotations:
        for i, d in enumerate(dataPoints):
            plt.annotate(i, d, (d[0] - 0.8, d[1] - 0.6))

        for i, c in enumerate(clusterCenters):
            plt.annotate(i, c, (c[0] - 0.5, c[1] - 0.5))

    plt.show()