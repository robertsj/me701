// Exercise 1 
// Print "hello from thread X of Y".
#include <omp.h>
#include <cstdio>



int main(int argc, char* argv[])
{



#pragma omp parallel
{
  int thread = omp_get_thread_num();
  int num_threads = omp_get_num_threads();

  printf("Hello from %i of %i \n", thread, num_threads);
}


  return 0;
}
