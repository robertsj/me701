// Exercise 4 
// Parallelize the program below that computes the
// dot product.
// 
// Compile using 
// $$ g++ -fopenmp dot_product.cc -o dot_product
//
// Compare (the final result) to one that simply sums
// the numbers i = 0..n.  Which scales better?  Why?

#include <omp.h>
#include <cstdio>
#include <vector>

int main(int argc, char* argv[])
{
  
  long int n = 200000000;
  double *a = new double[n];
  double *b = new double[n];

  // initialize arrays (not in the timed zone)
  for (long int i = 0; i < n; ++i)
  {
    a[i] = 2.0;
    b[i] = 3.0;
  }

  double dp = 0.0;

  // initialize timer
  double et = omp_get_wtime();

#pragma omp parallel 
{
  double dp_private = 0.0; // private for a single thread

#pragma omp for
  for (long int i = 0; i < n; ++i)
      dp_private += a[i]*b[i];

#pragma omp critical
  dp += dp_private;

} // end parallel

  // finalize time
  et = omp_get_wtime() - et;

  printf("       dot product is =%20.1e\n", dp);
  printf("dot product should be =%20.1e\n", n*6.0);
  printf("         elapsed time =%8.4f\n", et);

  // free the memory
  delete [] a;
  delete [] b;

  return 0;
}
