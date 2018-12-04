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

n = 1000000
x = np.ones(n)*2
y = np.ones(n)*3




# Chop up work
 

# Do the work


# Collect the results


