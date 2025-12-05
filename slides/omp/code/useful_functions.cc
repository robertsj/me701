// get the number of threads in the pool
int omp_get_num_threads(void);
// get the number a thread is in the pool of threads
int omp_get_thread_num(void);
// set the number of threads available 
void omp_set_num_threads(int num_threads);
// get wall clock time in seconds (unique per thread)
double omp_get_wtime(void);



