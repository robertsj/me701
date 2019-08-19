// Exercise 3
// Modify the vector addition from last time to use
// an omp for directive.

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

#pragma omp parallel for
  for (long int i = 0; i < n; ++i)
      c[i] = a[i] + b[i];


  // finalize time
  et = omp_get_wtime() - et;

  printf("c[%li]=%3.1f\n", 0, c[0]);
  printf("c[%li]=%3.1f\n", n-1, c[n-1]);
  printf("time = %8.4f\n", et);

  return 0;
}
