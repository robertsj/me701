from mpi4py import MPI
comm = MPI.COMM_WORLD
import numpy as np
# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()

n = 10

assert(size==3)

A_final = 0
if rank == 0:
    A_final = np.zeros((n, n), dtype='float')
    A = np.ones((2, n))*2.0

if rank == 1:
    A = np.ones((3, n))*3.0

if rank == 2:
    A = np.ones((5, n))*4.0

counts = [2*n, 3*n, 5*n]
comm.Gatherv(sendbuf=[A, MPI.DOUBLE], recvbuf=[A_final, counts, [0, 20, 50], MPI.DOUBLE], root=0)
print(A_final)

