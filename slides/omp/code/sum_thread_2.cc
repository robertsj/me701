#include <cstdio>
using std::printf;
int main()
{
  const long n = 100000000;
  double *v = new double[n];
  for (int i = 0; i < n; ++i)
    v[i] = (double)i;
  double s = 0.0;
  #pragma omp parallel for
  for (int i = 0; i < n; ++i)
  {
    #pragma omp atomic
    s += v[i];
  }
  double s_ref = 0.5*(n*n-n);
  printf("sum is %f, "
      "expected %f\n", s, s_ref);
  delete [] v;
}
