# This is linear regression (least squares fit) using Gradient descent

"""
Takes a list of points, a slope and a y intercept (to make a line) and gives
the total error between the two.

Err = (1/N) * \sum_(i=1)^N ((mx_i + b - y_i))^2
"""
def line_error(m,b,points):
    totalError = 0
    for i in range(len(points.ix[:,1])):
        totalError += (points.ix[:,1][i] - (m*points.ix[:,0][i] + b))**2
    return totalError / float (len(points))

"""
Gradient Descent (where alpha is the learning rate)

-Partial derivatives of m and b
-Updated by m = m - (alpha * m_gradient)
            b = b - (alpha * b_gradient)
"""
def Gradient_Step(b_curr,m_curr,points,alpha):
    b_grad = 0
    m_grad = 0
    N = float(len(points.ix[:,1]))
    for i in range(len(points.ix[:,1])):
        b_grad += -(2/N) * (points.ix[:,1][i] - ((m_curr*points.ix[:,0][i]) + b_curr))
        m_grad += -(2/N) * points.ix[:,0][i] * ((m_curr*points.ix[:,0][i]) + b_curr - points.ix[:,1])
    b_curr = b_curr - (alpha*b_grad)
    m_curr = m_curr - (alpha*m_grad)
    return [b_curr,m_curr]

