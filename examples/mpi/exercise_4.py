"""
Exercise 4 - From One to All.

Use the input function to get a number from the user on just one process.  
Then, use send and recv to get that number to every other process.
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD

# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()

# Get the input


# Send to every other process


# Print out who has what
print("Rank {} has {}".format(rank, number))


