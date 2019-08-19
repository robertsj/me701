from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print("Hello, from {} of {}!".format(rank, size))

if rank == 0:
   input('blahblah')

