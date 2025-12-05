# set the number of threads available
export OMP_NUM_THREADS=2
# set stack size for each thread, e.g., 2 gigabytes
export OMP_STACKSIZE=2G
# if true, display various OpenMP data (version 4 only)
export OMP_DISPLAY_ENV=TRUE
# bind threads 0 and 1 to core 0 and threads 2 and 3, 
#   to core 1.  use with gnu compilers.
export GOMP_CPU_AFFINITY="0 0 1 1"
# similar but for intel compilers. options include 
#   "compact" (pack 'em in) and "scatter" (round robin)
export KMP_AFFINITY=compact

