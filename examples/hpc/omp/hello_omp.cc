#include <omp.h>
#include <cstdio>

using std::printf;

int main()
{
 #pragma omp parallel
 {
  printf("hey from thread %i of %i\n", 
         omp_get_thread_num(), 
         omp_get_num_threads());
 }
 return 0;
}
