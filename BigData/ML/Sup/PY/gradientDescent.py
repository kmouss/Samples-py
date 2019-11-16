import numpy as np

def gradientDescent(X, y, theta, alpha, iterations):
    # Initialize some useful values
    m = len(y); # number of training examples
    J_history = np.array([0] * iterations)
    J_history = J_history.T

    for iter in range(iterations):

        h = X @ theta
        error_vectors = h - y
        the_gradient = alpha*(1/m)*(X.T @ error_vectors)
        theta = theta - the_gradient
    
    return theta
