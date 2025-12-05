#include <cstdio>
#include <omp.h>
int main()
{
  const long n = 100000000;
  double *v = new double[n];
  for (int i = 0; i < n; ++i)
    v[i] = (double)i;
  double s=0, et=omp_get_wtime();
  #pragma omp parallel
  {
    double s_p = 0.0;
    #pragma omp for
    for (int i = 0; i < n; ++i)
      s_p += v[i];
    #pragma omp atomic
    s += s_p;
  } // end parallel
  et = omp_get_wtime()-et;
  double s_ref = 0.5*(n*n - n);
  printf("sum is %f expected %f\n", s, s_ref);
  printf("etime %f\n", et);
  delete [] v;
}
