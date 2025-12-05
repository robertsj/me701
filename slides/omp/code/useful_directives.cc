// defines a parallel region
#pragma omp parallel num_threads(int) \
 default(shared|none) \
 shared(list) private(list) 
// defines a parallel loop
#pragma omp for private(list) \
 reduction(identifier: list) \
 schedule(kind,[chunk_size]) \
 collapse(int)
// defines a block to be done in serial
#pragma omp single private(list) nowait
// similar, but thread 0 must do it
#pragma omp master private(list) nowait
// make all thread stop until the rest catch up
#pragma omp barrier
// indicate a block must be done one thread at a time
#pragma omp critical
// indicate a statement (e.g., v[i]+=a) must be 
//   done one at a time
#pragma omp atomic

