def main():
    from functions import kMeans as km

    d = km.createRandomDatapoints(500, 2) #kMeans works for 2+ dimensions, for 1 dimension not always. plot works for 2 or 3 dimensions
    n = km.findOptimalClusterAmount(d)
    k = km.AssignClusters(d, n, True, 'r')
    km.plotClusters(k, False)
    print('WCSS-score: ' + str(km.withinClusterSumSquares(k)))

if __name__ == '__main__':
    main()