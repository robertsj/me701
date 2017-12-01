#include <omp.h>
#include <cstdio>
using std::printf;
int main()
{
  int n = 2e7;
  double s = 0.0, s_tmp;
  double t0 = omp_get_wtime(), te;
#pragma omp parallel \
   private(s_tmp) shared(n, s)
{
  s_tmp = 0.0;
#pragma omp for
  for (int i = 0; i < n; ++i)
  {
    s_tmp = s_tmp + i;
  }
#pragma omp atomic
  s = s + s_tmp;
} // end parallel
te = omp_get_wtime() - t0;
printf("%16.0f, et=%10.2e\n", s, te);
return 0;
}
