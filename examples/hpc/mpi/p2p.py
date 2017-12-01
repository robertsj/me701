import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
assert size == 2

Jack, Jill = 0, 1
if rank == Jack:
   a, b, c = 123, 3.14, "hello!"
   comm.send((a, b, c), dest=Jill, tag=1)
   a, b, c = 999, 1.0, "goodbye."
else:
   a, b, c = comm.recv(source=Jack, tag=1)

if rank == Jack:
    print("Jack has {}, {}, {}".format(a, b, c))
if rank == Jill:
    print("Jill has {}, {}, {}".format(a, b, c))

