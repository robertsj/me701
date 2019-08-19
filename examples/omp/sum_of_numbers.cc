// Exercise 5
#include <omp.h>
#include <cstdio>
#include <vector>

int main(int argc, char* argv[])
{
  
  long int n = 200000000;

  double dp = 0.0;

  // initialize timer
  double et = omp_get_wtime();

#pragma omp parallel 
{
  double dp_private = 0.0; // private for a single thread

#pragma omp for
  for (long int i = 1; i <= n; ++i)
      dp_private += (double)i;

#pragma omp critical
  dp += dp_private;

} // end parallel

  // finalize time
  et = omp_get_wtime() - et;

  printf("       sum is =%20.1e\n", dp);
  printf("sum should be =%20.1e\n", n*(n+1)/2.0);
  printf(" elapsed time =%8.4f\n", et);

  return 0;
}
