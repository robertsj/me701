import numpy as np
import time

#%%



def dot_product(x, y):
    """ Compute the dot (inner) product of two arrays.
    """
    v = 0.0
    for i in range(len(x)):
        v += x[i]*y[i]
    return v

m = 100
n = 100000
x = np.random.rand(n)
y = np.random.rand(n)

t0 = time.time()

for i in range(m):
    #a = dot_product(x, y)
    a = np.dot(x, y)

te = time.time() - t0

print("elapsed time per iter = ", te/m)


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
x = np.linalg.solve(A, b)    
    
#%% A Basic Iterative Solution

def iterate(a, b, x0, n = 10):
    x = x0
    print('x0 = {:.5f}'.format(x))
    for i in range(n):
        x = (1 - a)*x + b
        err = x - b/a
        print('x{} = {:.5f}   err = {:.5e}'.format(i, x, err))

iterate(-0.1, 1, 0, 100)




#%% Better Solutions from SciPy
    
    
