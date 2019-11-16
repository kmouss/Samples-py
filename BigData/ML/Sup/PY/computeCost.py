import numpy as np

def computeCost(X, y, theta):

    # Initialize some useful values
    m = len(y); # number of training examples

    # return the following variables correctly 
    J = 0

    predictions = np.matmul(X, theta)
    sqrErrors = np.power(predictions-y, 2)
    J = (1/(2*m)) * sqrErrors.sum()

    return J