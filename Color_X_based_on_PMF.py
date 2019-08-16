def PDFtoPlot(X, prob):
    """
    X - numpy array [n,2] of 2D data points
    prob - numpy array [n, K] of probabilities where prob[i,j] denotes the probability
    of point i belonging to the cluster j.
    """
    colorlist = []
    for row in prob:
        colorlist.append(np.argmax(row))
    plt.scatter(X[:, 0], X[:, 1], c=colorlist, s=50, cmap='viridis')
    plt.show()
