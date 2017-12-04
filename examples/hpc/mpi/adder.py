from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

t0 = MPI.Wtime()

# Sum up i = 1....n
n = int(1e7)

# Choose my bounds
chunk = n//size
b, e = rank*chunk+1, (rank+1)*chunk+1
if rank == size - 1:
    e = n+1

# Do my sum
s = 0
for i in range(b, e):
    s += i

# Get them all to master
for i in range(1, size):
    if rank == i:
        comm.send(s, dest=0, tag=i)    
    elif rank == 0:
        s += comm.recv(source=i, tag=i)
    
if rank == 0:
    print("sum = {}, expected = {}, time = {}".format(s, (n+1)*n/2, MPI.Wtime()-t0))
      
  
  

