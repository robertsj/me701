from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

te = MPI.Wtime()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
root = 0        # root process
last = size - 1 # last process

L = 10.0        # length
Q = 1.0         # heat generation rate
k = 0.1         # thermal conductivity
n = 1000        # number of divisions
Delta = L / n   # cell size

# determine work bounds 
chunk = (n+1) / size
# give last bit of work to the last process
if rank == size - 1 :
  chunk += n + 1 - chunk*size
# allocate local temperature arrays and loop bounds
if rank == 0 :
    T = np.zeros(chunk + 1) # one "ghost" point
    i_s, i_e = 0, chunk
elif rank == size - 1 :
    T = np.zeros(chunk + 1) # one "ghost" point
    i_s, i_e = 1, chunk + 1
else :
    T = np.zeros(chunk + 2) # two "ghost" points
    i_s, i_e = 1, chunk + 1

print("rank=%i i_s=%i i_e=%i chunk=%i" % (rank, i_s, i_e, chunk))

for iteration in range(10) : 
    
    # save the old temperature
    T_old = 1.0*T 
            
    # the middle
    for i in range(i_s+1, i_e-1) :
        T[i] = 0.5*Delta**2*Q/k + 0.5*(T_old[i+1]+T_old[i-1])

    # boundaries
    i = i_s
    if rank == root :
        T[i] = 0.0
    else :
        T[i] =  0.5*Delta**2*Q/k + 0.5*(T_old[i+1]+T_old[i-1])
    i = i_e-1
    if rank == last :
        T[i] = 0.0   
    else :
        T[i] =  0.5*Delta**2*Q/k + 0.5*(T_old[i+1]+T_old[i-1])
    
    # check for point-wise convergence
    error = max(abs(T-T_old))
    error = comm.reduce(error, error, op=MPI.MAX, root=root)
    error = comm.bcast(error, root=root)
    if rank == 0 and iteration % 500 == 0 :
        print " iteration %i, error %f" % (iteration, error)
    if error < 1e-6 :
        break
    
    # otherwise, get boundaries from neighbor
    # send left
    if rank == 0 : print "****",rank, T
    if rank > root :
        comm.send(T[i_s], dest=rank-1, tag=111)               
    if rank < last :        
        T[i_e] = comm.recv(source=rank+1, tag=111)
    # send right
    if rank < last :
        comm.send(T[i_e-1], dest=rank+1, tag=222)
    if rank > root :
        T[i_s-1] = comm.recv(source=rank-1, tag=222) 
        if rank == 1 : 
            "<<<<<", T[i_s-1]
    if rank == 0 : print "****",rank, T

    
# get all temps on rank 0
T = comm.gather(T[i_s:i_e], root=root)

if rank == 0 :
    # compute the elapsed time
    te = MPI.Wtime() - te
    # construct a complete array of temperatures
    T_total = np.zeros(n+1)
    j = 0
    for i in range(size) :
        T_total[j:j+len(T[i])] = T[i][:]
        j += len(T[i])
    print T_total
    print sum(T_total)
    print "Elapsed time: %f seconds" % te
    print "Number of iterations: %i" % iteration
    print "Final error: %f" % error
    x = np.linspace(0, L, n+1)
    T_ref = -0.5*Q/k*x**2 + 0.5*Q/k*L*x
    plt.figure(0)
    plt.plot(x, T_total, 'k', x, T_ref, 'b--')
    plt.xlabel('x') 
    plt.ylabel('T')
    plt.figure(1)
    plt.plot(x, (T_total-T_ref)/T_ref, 'r--')    
    #plt.show()
