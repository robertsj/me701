// Exercise 5
// Parallelize the solver given below for  
//    -k(T_xx + T_yy) = q
// subject to
//    T(0, y) = T(1, y) = T(x, 0) = 0
//    T(x, 1) = 1
// with k = 1 and q = 0.
//
// Jacobi iteration is used based on the finite
// difference relation
//   -k (T(i+1,j)+T(i-1,j)+T(i, j+1)+T(i, j-1)-4*T(i,j)) / Delta^2 = q
// Isolate T(i, j) so that
//    T(i, j)^{new} = (1/4)*(T(i+1,j)+T(i-1,j)+T(i, j+1)+T(i, j-1))^{old} + (Delta^2/k/4)*q
// Note that dividing by (k/Delta^2) is just like multiplying by inv(D) from
// earlier in the class, i.e.,  x^{new} = (I - inv(D)*A)x^{old} + inv(D)b.
#include <cmath>
#include <cstdio>
#include <omp.h>

int main(int argc, char* argv[])
{
  // Initialize timer
  double total_et = omp_get_wtime();

  // Problem parameters
  double q = 0;
  double k = 1;
  int n = 1000; 
  double Delta = 1.0/(n-1);

  // Initialize T arrays
  double *T = new double[n*n];
  double *T_old = new double[n*n];
  double *swap;
  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
    {
      T_old[i*n + j] = 0.0;
      T[i*n+j] = 0.0;
    }
  }
  // BC's
  for (int i = 0; i < n; ++i)
  {
    T[i*n + n-1] = 1.0;
    T_old[i*n + n-1] = 1.0;
  }

  // Jacobi iterations until r = ||T-T_old|| is small enough
  double jacobi_et = omp_get_wtime();
  double r;
  int it = 0;
  do
  {
    it += 1;

    double coef = Delta*Delta/k/4.0;
    for (int i = 1; i < n-1; ++i)
    {
      for (int j = 1; j < n-1; ++j)
      {
         T[i*n+j] =  0.25*(T_old[(i+1)*n+j] + T_old[(i-1)*n+j] + T_old[i*n+j+1] + T_old[i*n+j-1]) + coef*q;
      }
    }

    // Compute r = ||T-T_old||
    r = 0.0;
    for (int i = 0; i < n*n; ++i)
        r += pow(T[i]-T_old[i], 2);
    r = sqrt(r);

    // Save T to T_old.  Note, this is *not* a copy!
    swap = T_old;
    T_old = T;
    T = swap;

    if (it % 10 == 0)
    {
      std::printf("iter %i,  error %8.3e\n", it, r);
    }
  }
  while (r > 1e-4 and it < 100000);
  printf("FINAL: iter %i,  error %8.3e\n", it, r);
  jacobi_et = omp_get_wtime() - jacobi_et;

  // Write to file as x, y, T using C-style writing
  double write_et = omp_get_wtime();
  FILE *fh; 
  fh = std::fopen("temperatures.txt", "w");
  for (int i = 0; i < n; ++i)
  {
    double x = i*Delta;
    for (int j = 0; j < n; ++j)
    {
      double y = j*Delta;
      std::fprintf(fh, "%12.6e  %12.6e  %12.6e\n", x, y, T_old[i*n+j]);
    }
  }
  std::fclose(fh);
  write_et = omp_get_wtime() - write_et;

  // Free the memory
  delete [] T;
  delete [] T_old;

  // Finalize timer
  total_et = omp_get_wtime() - total_et;
  printf("JACOBI ELAPSED TIME: %8.3e seconds\n", jacobi_et);
  printf(" WRITE ELAPSED TIME: %8.3e seconds\n", write_et);
  printf(" TOTAL ELAPSED TIME: %8.3e seconds\n", total_et);


}
