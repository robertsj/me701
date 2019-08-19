"""
Exercise 2 - Roger, that.
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()



if rank == 0:
    message = [1,2,3, 'a', {'1': 123}]
    comm.send(message, dest=1, tag=77)

if rank == 1:
    message = comm.recv(source=0, tag=77)

print(rank, message)
