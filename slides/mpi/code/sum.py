from mpi4py import MPI
comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()
# compute the sum s of the numbers 0...n-1
n, s = 1000, 0.0
# compute starting and ending indices
i_s = rank*(n/size)
i_e = i_s+(n/size)
if rank == size - 1 :
    i_e = n
# perform the sum and have process 0 get the sum
for i in range(i_s, i_e) :
    s += i
comm.reduce(s, s, op=MPI.SUM, root=0)
# print the result on process 0
if rank == 0 :
    print("sum is ", s, " expected ", n*(n-1)/2)
    