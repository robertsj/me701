"""
Exercise 5 -  A Collective Study
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD

# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()


def bcast_demo():
    if rank == 0:
      data = {'a': 123, 'b': 'hello, world'}
    else:
      data = None
    data = comm.bcast(data, root=0)
    print(data)

def gather_demo():
  data = rank**2
  gathered_data = comm.gather(data, root=0)
  print(rank, gathered_data)
 
def allgather_demo():
  data = rank**2
  gathered_data = comm.allgather(data)
  print(rank, gathered_data)

def scatter_demo():
  if size != 4:
      print("you need 4 processes for this one!")
      return
  if rank == 0:
      data = [100, 101, 102, 103]
  else:
      data = None
  data = comm.scatter(data, root=0)
  print(rank, data)

if __name__ == '__main__':

    #bcast_demo()
    #gather_demo()
    #allgather_demo()
    scatter_demo()
   
