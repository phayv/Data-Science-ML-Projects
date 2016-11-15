import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x = np.array([1,2,3,4,5,6],dtype = np.float64)
y = np.array([5,4,6,5,6,7],dtype = np.float64)

########################################## Fit a line.
def best_fit_line(x,y):
    """
        m = (x\bar * y\bar - (xy)\bar) / x\bar^2 - x^2\bar
    """
    m = (np.mean(x)*np.mean(y) - np.mean(x*y)) / (np.mean(x)**2 - np.mean(x**2))
    # b = y - m*x
    b = np.mean(y) - m*np.mean(x)
    regression_line = [(m*x_i) + b for x_i in x]
    print "y = {:5.3f}x + {:5.3f}".format(m,b)
    return m,b,np.array(regression_line)

def stackplot(x,y,regr_line):
    plt.scatter(x,y)
    plt.plot(x,regr_line)
    plt.show()

m,b,regression_line = best_fit_line(x,y)
stackplot(x,y,regression_line)

########################################## How accurate is this line?
"""
    Calculating r^2: Coefficient of Determination
    r^2 = 1 - (Sq.E.y\hat)/(Sq.E.y\bar)
    High r^2 is what we want
"""
#Check with linear_model
from sklearn.linear_model import LinearRegression

def test_with_LR(x,y):
    LR = LinearRegression()
    LR.fit(x.reshape(len(x),1),y.reshape(len(y),1))
    print "SK-Learn Accuracy: ",LR.score(x.reshape(len(x),1),y.reshape(len(y),1))
    
def squared_error(y_orig,y_fit):
    return np.sum((y_orig - y_fit)**2)

def coeff_of_det(y_orig,y_fit):
    y_mean_line = [np.mean(y_orig) for ys in y_orig]
    squared_error_fit = squared_error(y_orig,y_fit)
    squared_error_y_mean = squared_error(y_orig,y_mean_line)
    return 1 - (squared_error_fit)/(squared_error_y_mean)

r_squared = coeff_of_det(y,regression_line)
print "Our r^2 estimate : ",r_squared

test_with_LR(x,y)
########################################## Testing
import random

def create_test(n,var,step = 2,corr=False):
    val = 1
    ys = []
    for i in range(n):
        y = val + random.randrange(-var,var)
        ys.append(y)
        if corr and corr =='pos':
            val += step
        elif corr and corr =='neg':
            val -= step
    xs = [i for i in range(len(ys))]
    return np.array(xs,dtype = np.float64), np.array(ys,dtype = np.float64)

#changing var would obviously change the r^2 value (higher r^2 = low var and vise versa)
x2,y2 = create_test(40,10,2,corr='pos')

m2,b2,regression_line2 = best_fit_line(x2,y2)
stackplot(x2,y2,regression_line2)

r_squared2 = coeff_of_det(y2,regression_line2)
print "Our r^2 estimate : ",r_squared2

#Check with linear_model
test_with_LR(x2,y2)
