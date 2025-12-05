from mpi4py import MPI
comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()
# initialize data to be communicated
if rank == 0:
   dataB = 123, [(i+1)**2 for i in range(size)]
else:
   dataB, dataS = None, None
dataG = (rank+1)**3
# collectively move the data
dataB = comm.bcast(dataB, root=0)
dataS = comm.scatter(dataS, root=0)
dataG = comm.gather(dataG, root=0)
# print the results on a single process
if rank == 0 :
    print(dataB, dataS, dataG)

