from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
import numpy as np

# rank 0 defines a to be an array of ones, while 
# rank 1 defined b to be an array of twos.  Then
# we let them share these.
n=100000
if rank == 0:
   a = np.ones(n)
   comm.send(a, dest=1, tag=1)
   b = comm.recv(source=1, tag=2)
elif rank == 1:
   b = np.ones(n)*2
   comm.send(b, dest=0, tag=2)
   a = comm.recv(source=0, tag=1);
   
print("rank = ", rank, a[0], b[0])

