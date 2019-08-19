"""
Exercise 6 -  2-D Heat Transfer
"""

import numpy as np
import matplotlib.pyplot as plt
import time

from mpi4py import MPI
comm = MPI.COMM_WORLD

# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()

def solve(q, k, n):

    Delta = 1.0/(n-1)

    # Divide the [X, Y] domain along the X axis.
    chunk = n // size
    if rank == size-1:
        chunk = chunk + (n - chunk*size)

    # Initialize temperature (with BC's)
    if size == 1:
       T = np.zeros((n, n))
    elif rank == 0 or rank == size-1:
        T = np.zeros((chunk+1, n))
    else:
        T = np.zeros((chunk+2, n))
    T[:, n-1] = 1.0
    T_old = T.copy()

    # Perform the Jacobi iterations
    r = 1.0
    it = 0
    max_it = 100
    while r > 1e-4 and it < max_it:

        # Swap
        T_old, T = T, T_old

        # Update temperatures
        r = 0.0
        for i in range(1, T.shape[0]-1): 
            for j in range(1, n-1):
                tmp = 0.25*(T_old[i+1,j]+T_old[i-1,j]+T_old[i,j+1]+T_old[i,j-1])
                T[i, j] = tmp + Delta*Delta/k/4.0*q;
                r += (T[i, j]-T_old[i, j])**2

        # Compute residual and update counter
        r = np.sqrt(r)
        r = comm.allgather(r)
        r = np.linalg.norm(r)

        # Update ghost cells
        if rank < size-1:
            # send to right
            comm.Send([T[-2, :], MPI.DOUBLE], dest=rank+1, tag=77)
        if rank > 0:
            # receive from left
            comm.Recv([T[0, :], MPI.DOUBLE], source=rank-1, tag=77)
        if rank > 0:
            # send to my left
            comm.Send([T[1, :], MPI.DOUBLE], dest=rank-1, tag=88)
        if rank < size-1:
            # receive from my right
            comm.Recv([T[-1, :], MPI.DOUBLE], source=rank+1, tag=88)
        
        it += 1

        if rank == 0 and it % 100 == 0:
            print(" it={}, res={}".format(it, r))

    # Return now if one process
    if size == 1:
        return T

    # Initialize the final T
    T_final = None

    # Get final temperatures onto rank 0.  First, tell have each process tell
    # rank 0 how many elements (chunk*n) will be sent.
    counts = comm.gather(chunk*n, root=0)
    
    # Have rank 0 initialize T_final and determine where each rank's 
    # contributions will go.
    if rank == 0:
        T_final = np.zeros((n, n), dtype='float')
        displacements = [0]
        for i in range(len(counts)-1):
            displacements.append(sum(counts[:(i+1)]))
    else:
        displacements = None


    # Gather all temperatures and return
    if rank == 0:
        start, stop = 0, chunk
    else:
        start, stop = 1, chunk+1
    comm.Gatherv(sendbuf=[T[start:stop], MPI.DOUBLE], 
                 recvbuf=[T_final, counts, displacements, MPI.DOUBLE], root=0)
    return T_final

def plot_temperature(n, T):
    x = np.linspace(0, 1, n)
    y = x.copy()
    xx, yy = np.meshgrid(x, y)
    plt.contourf(xx, yy, T.T, cmap='inferno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == "__main__":


    q = 10  # heat generation rate
    k = 1   # conductivity
    n = 100 # number of points per dimension

    te = time.time()
    T = solve(q, k, n)
    te = time.time() - te 
    if rank == 0:
        print(np.mean(T))
        print("te = ", te)
        plot_temperature(n, T)

