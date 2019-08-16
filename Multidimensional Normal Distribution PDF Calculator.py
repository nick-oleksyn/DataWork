def nd(x, mu, var):
    """
    x - array or list [1,d]
    d - dimensionality (features)
    mu - mean of the normal distribution
    var - variance (sigma^2) of the normal distribution
    returns probability PDF
    #commented below : included an alternative version of the calculation
    that involves linear algebra and matrix inverse
    """
    var= float(var)
    d = x.shape[0]
    #r = math.pow((var* 2*math.pi), -d/2)* np.exp(((-1/2) * (((np.transpose((x - mu))@ (1/var*np.eye(d))) @ (x - mu)))))
    lindist = 0
    for i in range(d):
        lindist += (x[i]-mu[i])**2
    r = math.pow((var* 2*math.pi), -d/2)* np.exp( (-1/2) * (1/var) * (lindist))

    return r
