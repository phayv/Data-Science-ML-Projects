from __future__ import division
import re, math, random
from collections import defaultdict, Counter
from functools import partial

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scipy.linalg

#-----------------Vectors

def vector_add(v, w):
    """adds two vectors by elements: numpy.add()"""
    return np.array([v_i + w_i for v_i, w_i in zip(v,w)])

def vector_subtract(v, w):
    """subtracts two vectors by elements: numpy.subtract()"""
    return np.array([v_i - w_i for v_i, w_i in zip(v,w)])

def vector_sum(vectors):
    """adds multiple vectors at once"""
    return reduce(vector_add, vectors)

def scalar_multiply(const, v):
    """multiply a vector by a scalar: np.multiply()"""
    return np.array([const * v_i for v_i in v])

def vector_mean(vectors):
    """computes the vector who has element being the mean for each row"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
    """numpy.dot()"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_squares(v):
    """return a dot of square elements"""
    return dot(v, v)

def magnitude(v):
    """returns magnitude of vector"""
    return math.sqrt(sum_squares(v))

def squared_distance(v, w):
    """returns sum of the squares of two vectors"""
    return sum_squares(vector_subtract(v, w))

def distance(v, w):
    """returns distance of two vectors"""
    return math.sqrt(squared_distance(v, w))

#-----------------Matrices
def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]
    
def get_column(A, j):
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix 
    whose (i,j)-th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]  

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

def identity_matrix(i,j):
    return make_matrix(5, 5, is_diagonal)





