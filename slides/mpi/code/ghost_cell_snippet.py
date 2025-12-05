    # send left
    if rank > root :
        comm.send(T[i_s], dest=rank-1, tag=111)
    if rank < last :
        T[i_e] = comm.recv(source=rank+1, tag=111)
    # send right
    if rank < last :
        comm.send(T[i_e-1], dest=rank+1, tag=222)
    if rank > root :
        T[i_s-1] = comm.recv(source=rank-1, tag=222)  
