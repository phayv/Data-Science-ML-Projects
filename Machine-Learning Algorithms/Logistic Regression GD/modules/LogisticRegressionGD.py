"""
The hypothesis of this is the Logistic Function, and we want to minimize the Logistic cost function of 2 parameters
"""

import numpy as np
from scipy import stats
from sklearn.datasets.samples_generator import make _regression


def Gradient_Descent(alpha, x, y, eps = 1*(10**(-6)), maxcount = 1000):
"""This will take 2 features and return the least square fit parameter value for those 2 features.
"""
    converged = False
    count = 0
    
    #initialization
    n_samples = x.shape[0]
    theta = np.zeros(2)
    x_transpose = x.transpose()
    
    while !converged:
        # Cost function
        J = np.sum( (np.dot(x,theta) - y)**2 )/(2*n_samples)
        # Derivitive of cost function
        gradient = np.dot( x_tranpose, np.dot(x,theta) - y )/n_samples
        
        # Updating
        theta = temp_theta - alpha*gradient
        temp_theta = theta
        
        count += 1
        if count == 1000:
            print "max iterations reached"
            break
        if theta - temp_theta < eps:
            converged = True
    return theta


if __name__ == '__main__':
    x,y = make_regression(n_samples = 100, n_features = 1, n_informative = 1, random_state = 0, noise = 35)
    m,n = np.shape(x)
    alpha = .01
    theta = Gradient_Descent(alpha,x,y)
    
    