def plot(assignmentDict, title):
    
    from matplotlib import pyplot as plt
    import numpy as np, random

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
            case 1:
                plt.scatter(c[0], s = 200, c = clusterColors[c], marker = "x")
                plt.scatter(dataPointsPlot[0], s = 30, c = dataPointsPlot[c], marker = "o")
            case 2:
                plt.scatter(c[0], c[1], s = 200, c = clusterColors[c], marker = "x")
                plt.scatter(dataPointsPlot[0], dataPointsPlot[1], s = 30, c = clusterColors[c], marker = "o")
            case 3:
                ax.scatter(c[0], c[1], c[2], s = 200, c = clusterColors[c], marker = "x", alpha = 1, depthshade = False)
                ax.scatter(dataPointsPlot[0], dataPointsPlot[1], dataPointsPlot[2], s = 30, c = clusterColors[c], marker = "o", alpha = 1, depthshade = False)

    plt.title(title)
    plt.show()