from mpi4py import MPI
import numpy
from time import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Initialize the data
n = 100000000
data = numpy.arange(n, dtype='i')

# Passing MPI datatypes explicitly
te = time()
if rank == 0:
    comm.Send([data, MPI.INT], dest=1, tag=77)
elif rank == 1:
    comm.Recv([data, MPI.INT], source=0, tag=77)
te1 = time() - te

# Passing data via automated "pickling"
te = time()
if rank == 0:
    comm.send(data, dest=1, tag=88)
elif rank == 1:
    data = comm.recv(source=0, tag=88)
te2 = time() - te

if rank == 0:
    print("Elapsed time for Send/Recv = {:12.6f} s".format(te1))
    print("Elapsed time for send/recv = {:12.6f} s".format(te2))
    print("                     Ratio = {:12.6f}".format(te2/te1))
