#include <omp.h>
#include <cstdio>

using std::printf;

int main()
{
  int i, n;
  double s, s_tmp;
#pragma omp parallel \
   private(i, s_tmp) shared(s)
{
  s = 0.0;
  s_tmp = 0.0;
  n = 2e7;
#pragma omp for
  for (int i = 0; i < n; ++i)
  {
    s_tmp = s_tmp + i;
  }
#pragma omp atomic
  s = s + s_tmp;
} // end parallel

printf("%16.0f\n", s);

return 0;
}
