// Exercise 2
// Add to arrays (here, std::vectors) in parallel using
// only the parallel directive and the thread id and count.
#include <omp.h>
#include <cstdio>
#include <vector>

int main(int argc, char* argv[])
{
  
  long int n = 10000000;
  std::vector<double> a(n, 1.0);
  std::vector<double> b(n, 2.0);
  std::vector<double> c(n, 0.0);

  // initialize timer
  double et = omp_get_wtime();

#pragma omp parallel
{
  int thread = omp_get_thread_num();
  int num_threads = omp_get_num_threads();
  int chunk = n / num_threads;
  int start = thread*chunk;
  int stop = (thread+1)*chunk;
  if (thread == num_threads - 1)
  {
    stop = n;
  }   

  for (int i = start; i < stop; ++i)
      c[i] = a[i] + b[i];
} // end parallel


  // finalize time
  et = omp_get_wtime() - et;

  printf("c[%li]=%3.1f\n", 0, c[0]);
  printf("c[%li]=%3.1f\n", n-1, c[n-1]);
  printf("time = %8.4f\n", et);

  return 0;
}
