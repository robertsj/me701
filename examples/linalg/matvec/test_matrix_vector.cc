// Driver program to test matrix-vector multiplication from c
#include <cstdio>
#include <omp.h>
//void DGEMV(char *trans, const int *m, const int *n, const double *alpha,
//           const double *a, const int *lda, const double *x, const int *incx,
//           const double *beta, double *y, const int *incy);
typedef int MKL_INT;
extern "C" {
void dgemv(const char *trans, const MKL_INT *m, const MKL_INT *n, const double *alpha,
           const double *A, const MKL_INT *lda, const double *x, const MKL_INT *incx,
           const double *beta, double *y, const MKL_INT *incy);
}
int main()
{
  double *A, *x, *y;
  double alpha = 1.0, beta = 0.0, t, t2, flops;
  int n, m, lda, incx = 1, incy = 1;
  char trans = 'n';
  int maxi = 200;
  int maxj = 50;

  for (int j = 0; j < maxj; ++j)
  {
    // Matrix size
    m   = 10 * 2 * (j+1);
    n   = m;
    lda = m;
    // Create the matrix and vector. NOTE, the "logically" 2-D 
    // array A must be 1-D in practice.  Remember, indexing [i][j]
    // is the same as doing [j + i*n] for *row* major, or 
    // [i + j*n] for *col* major.  Here, we can actually choose the
    // interpretation by how we index as we fill A.
    A = new double[n*n];
    x = new double[n];
    y = new double[n];
    // Initialize A and x
    for (int i = 0; i < n; ++i)
    {
        for (int k = 0; k < n; ++k)
        {
            A[i + k*n] = 1;
        }
        x[i] = 1;
        y[i] = 0;
    }
    // Start the timer.
    t = omp_get_wtime();
    // Loop over and apply A several times for consistent timing
    for (int i = 0; i < maxi; ++i)
    {
      // Reset
      for (int k = 0; k < n; ++k)
      {
          y[k] = 0.0;
      }
      // careful on use of referencing!  Remember that BLAS and LAPAC
      dgemv(&trans, &m, &n, &alpha, A, &lda, x, &incx, &beta, y, &incy);
      if (y[0] != (double)n)
      {
          printf("bad result. stop.\n");
          return -1;
      }
    }
    t2 = omp_get_wtime()-t;
    // we should subtract m for our own implementation, since
    // we don't do y = Ax-y, just y = Ax
    flops = (2*m*m)*maxi;
    printf("%4i  %12.4f\n", m,  flops / 1e6 / t2);
    // deallocate memory
    delete [] A;
    delete [] x;
    delete [] y;
  }
}
