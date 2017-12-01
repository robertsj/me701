from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

print "Hello from rank ", rank, " of ", size

s = 0.0
n = 10000
m = n / size
for i in range(rank*m, (rank+1)*m) :
    s += (i+1) 

# send to process zero
if rank > 0 :
    comm.send(s, dest=0, tag=123)
else :
    for p in range(1, size) :
        s += comm.recv(source=p, tag=123)

if rank == 0 :
    print s, n*(n+1)/2
