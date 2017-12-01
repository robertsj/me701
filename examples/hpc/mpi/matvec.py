import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
p = comm.Get_size()

"""
Goal: given a matrix A and a vector x, compute 
the matrix-vector product y <-- A*x in parallel.
"""

def matvec(A, x) :
    n = len(A)
    start = (n/p)*r 
    end = (n/p)*(r+1)
    y = np.zeros(n/p)
    for i in range(start, end) :
        y[i-start] = np.dot(A[i][:], x)
    # awkward, but necessary if lowercase versions used
    y = np.array(comm.allgather(y)).reshape(n)
    return y

A = np.ones((4,4))
x = np.ones(4)

if r == 0 :
    y_ref = np.dot(A,x)
    
y = matvec(A, x)

if r == 0 :
    print y_ref
    print y
