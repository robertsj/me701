// Driver program to test matrix-vector multiplication from c
#include <cstdio>
int main()
{
  double **a;
  double *x, *y;
  double alpha = 1.0, beta = 0.0, t, t2, omp_get_wtime, flops;
  int n, m, lda, incx = 1, incy = 1, i, j, maxi;
  char trans = 't';

  for (j = 0; j < 50; ++j)
  {
    // Matrix size
    m   = 10 * 2 * j
    n   = m
    lda = m
    // Create the matrix and vector
    allocate(A(m, n), x(n), y(n))
    // Initialize A and x
    A = 1.0
    x = 1.0
    // Start the timer.
    t = omp_get_wtime()
    // Loop over and apply A several times for consistent timing
    maxi = 200
    for (i = 0; i < maxi; ++i)
    {
      // Reset
      y = 0.0
      call dgemv(trans, m, n, alpha, A, lda, x, incx, beta, y, incy)
    }
    t2 = omp_get_wtime()-t
    // we should subtract m for our own implementation, since
    // we don't do y = Ax-y, just y = Ax
    flops = (2*m*m)*maxi
    print *, m,  flops / dble(1e6) / t2
    deallocate(A, x, y)
  }
}
