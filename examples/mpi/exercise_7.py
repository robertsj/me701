"""
Exercise 7 - Perform a dot product with MPI.

Calculate the parallel efficiency.  How does this compare to OpenMP?
"""


import numpy as np
import matplotlib.pyplot as plt
import time

from mpi4py import MPI
comm = MPI.COMM_WORLD

# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()



n = 100000000
x = np.ones(n)*2
y = np.ones(n)*3

te = time.time()

# Chop up work
chunk = n // size
start = rank*chunk
stop = (rank+1)*chunk
if rank == size - 1:
   stop = n

# Do the work
#dp = 0.0
#for i in range(start, stop):
#    dp += x[i]*y[i]
dp = np.sum(x[start:stop]*y[start:stop])

# Collect the results
dp_global = comm.gather(dp, root=0)

te = time.time() - te

if rank == 0:
    dp_global = sum(dp_global)
    print(dp_global)
    print("time = ", te)

