import numpy as np

#%%

def dot_product(x, y):
    """ Compute the dot (inner) product of two arrays.
    """
    v = 0.0
    for i in range(len(x)):
        v += x[i]*y[i]
    return v




#%% 
n = 100
A = np.zeros((n, n), dtype='float64')
b = np.zeros(n)
for i in range(0, n):
    A[i, i] = -2
    if i > 0 :
        A[i, i-1] = 1.0
    if i < n-1: 
        A[i, i+1] = 1.0
    b[i] = 1
    
    
# how to solve?
    
    
#%% A Basic Iterative Solution





#%% Better Solutions from SciPy
    
    
