from mpi4py import MPI
comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()
# BROADCASTING VALUES FROM ONE TO ALL
a = None
if rank == 0:
    a = 123
a = comm.bcast(a, root=0)
if rank == 1:
    print("after bcast, a = {}".format(a))
# SCATTERING AN ARRAY ON ONE TO ALL
a = None
if rank == 0:
    a = ['1',234,[2,3],{'A': 1}]
a = comm.scatter(a, root=0)
if rank == 1:
    print("after scatter, a = {}".format(a))
# GATHERING FROM ALL TO AN ARRAY ON ONE
a = rank**2
b = comm.gather(a, root=0)
print("rank={}, after gather, b = {}".format(rank, b))
# GATHERING FROM ALL TO AN ARRAY ON ALL
c = comm.allgather(a)
print("rank={}, after allgather, c = {}".format(rank, c))
