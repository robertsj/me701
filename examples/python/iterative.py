import numpy as np
import scipy as sp
import scipy.sparse
import scipy.sparse.linalg
import matplotlib.pyplot as plt

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
    
    
# how to solve?    @
x = np.linalg.solve(A, b)   

def richardson(A, P, b, x0, tol=1e-6, maxit=1000):
    x = 1*x0
    inv_P = np.linalg.inv(P)
    
    r = np.linalg.norm(inv_P@A@x - inv_P@b)
    it = 0
    I = np.eye(A.shape[0])
    while r > tol and it < maxit:
        x = (I - inv_P@A) @ x + inv_P@b
        r = np.linalg.norm(inv_P@A@x - inv_P@b)
        print("it = ", it, "r = ", r)
        it = it + 1
    return x

