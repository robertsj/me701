from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank() 
import numpy as np

n=100000

# Option 1
a = np.zeros(n)
t = MPI.Wtime()
if rank == 0:
   a = np.ones(n, dtype='f')
   comm.send(a, dest=1, tag=1)
elif rank == 1:
   a = comm.recv(source=0, tag=1);
if rank == 1:
    print("a[0]={}, time={}".format(a[0], MPI.Wtime()-t))

# Option 2
a = np.zeros(n)
t = MPI.Wtime()
if rank == 0:
   a = np.ones(n)
   comm.Send(a, dest=1, tag=1)
elif rank == 1:
   comm.Recv(a, source=0, tag=1);
if rank == 1:
    print("a[0]={}, time={}".format(a[0], MPI.Wtime()-t))
