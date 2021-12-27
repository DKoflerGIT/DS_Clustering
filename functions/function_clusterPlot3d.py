def plot(assignmentDict, title):
    
    from matplotlib import pyplot as plt
    import numpy as np, random

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('x')
    ax.set_xlabel('y')
    ax.set_xlabel('z')

    clusterCenters = []
    clusterColors = {}

    for a in assignmentDict: #get cluster centers from dict
        if (assignmentDict[a] not in clusterCenters):
            clusterCenters.append(assignmentDict[a])

    for c in clusterCenters: #assign random colors to clusters
        numbers = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        clusterColors[c] = '#' + ''.join('{:02X}'.format(n) for n in numbers)

    X_C = []
    Y_C = []
    Z_C = []

    for x,y,z in clusterCenters:
        X_C.append(x)
        Y_C.append(y)
        Z_C.append(z)

    for i,c in enumerate(clusterCenters):
        ax.scatter(X_C[i], Y_C[i], Z_C[i], s = 200, c = clusterColors[c], marker = "x")

    dataPoints = []
    X_D = []
    Y_D = []
    Z_D = []

    for a in assignmentDict: #get data points from dict
        if (a in dataPoints):
            dataPoints.append(a)

    for x,y,z in dataPoints:
        X_D.append(x)
        Y_D.append(y)
        Z_D.append(z)

    pts = []

    for c in clusterCenters:
        pts.clear()
        X_D.clear()
        Y_D.clear()
        Z_D.clear()

        for a in assignmentDict:
            if assignmentDict[a] == c:
                pts.append(a)

        for x,y,z in pts:
            X_D.append(x)
            Y_D.append(y)
            Z_D.append(z)

        ax.scatter(X_D, Y_D, Z_D, s = 30, c = clusterColors[c], marker = "o")

    plt.title(title)
    plt.show()
