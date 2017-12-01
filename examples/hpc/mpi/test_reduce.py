import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# lets add up the number n size times.
# assume it is read in by the master process.
if rank == 0 :
    n = 100
else :
    n = None
n = comm.bcast(n, root=0)

# reduce
m = -1
data = np.zeros(1)
data[0] = rank
sum_data = 0.0*data
comm.Reduce([data, MPI.DOUBLE], [sum_data, MPI.DOUBLE], op=MPI.SUM, root=0)

res = comm.allreduce(sendobj=rank, op=MPI.MAX)
print res
if rank == 0 :
  print "result = ", sum_data[0], res
  
