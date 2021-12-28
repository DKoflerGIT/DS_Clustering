def plot(assignmentDict, title, xLabel, yLabel, zLabel):
    
    from matplotlib import pyplot as plt
    import numpy as np, random

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)

    dataPoints = []
    clusterCenters = []
    
    for a in assignmentDict: 
        if (a in dataPoints): #get data points from dict
            dataPoints.append(a)

        if (assignmentDict[a] not in clusterCenters): #get cluster centers from dict
            clusterCenters.append(assignmentDict[a])     

    clusterColors = {}

    for c in clusterCenters: #assign random colors to each cluster
        numbers = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        clusterColors[c] = '#' + ''.join('{:02X}'.format(n) for n in numbers)

    X_D = []
    Y_D = []
    Z_D = []
    X_C = []
    Y_C = []
    Z_C = []

    for x,y,z in dataPoints:
        X_D.append(x)
        Y_D.append(y)
        Z_D.append(z)

    for x,y,z in clusterCenters:
        X_C.append(x)
        Y_C.append(y)
        Z_C.append(z)

    pts = []

    for i,c in enumerate(clusterCenters):
        #plot clusters
        ax.scatter(X_C[i], Y_C[i], Z_C[i], s = 200, c = clusterColors[c], marker = "x", alpha = 1, depthshade = False)

        # plot data points
        pts.clear()
        X_D.clear()
        Y_D.clear()
        Z_D.clear()
    
        for a in assignmentDict: # get datapoints assigned to current cluster
            if assignmentDict[a] == c:
                pts.append(a)
        
        for x,y,z in pts:
            X_D.append(x)
            Y_D.append(y)
            Z_D.append(z)

        ax.scatter(X_D, Y_D, Z_D, s = 30, c = clusterColors[c], marker = "o", alpha = 1, depthshade = False)

    plt.title(title)
    plt.show()
