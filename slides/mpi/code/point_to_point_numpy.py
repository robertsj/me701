from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# pass explicit MPI datatypes
if rank == 0:
   data = np.linspace(0, 1, 10, dtype=np.float64)
   comm.Send([data, MPI.DOUBLE], dest=1, tag=77)
elif rank == 1:
   data = np.empty(10, dtype=np.float64)
   comm.Recv([data, MPI.DOUBLE], source=0, tag=77)
   print("rank 1 has ", data)
# automatic MPI datatype discovery
if rank == 0:
   data = np.arange(10, dtype=np.float64)
   comm.Send(data, dest=1, tag=13)
elif rank == 1:
   data = np.empty(10, dtype=np.float64)
   comm.Recv(data, source=0, tag=13)
   print("rank 1 has ", data)
