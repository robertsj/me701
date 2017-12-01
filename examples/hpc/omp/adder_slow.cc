#include <omp.h>
#include <cstdio>

using std::printf;

int main()
{
  int i, n;
  double s;
#pragma omp parallel \
   private(i) shared(s)
{
  s = 0.0;
  s_tmp = 0.0;
  n = 2e7;
#pragma omp for
  for (int i = 0; i < n; ++i)
  {
#pragma omp atomic
    s = s + i;
    // safe addition, but 
    // serializes execution!
  }
} // end parallel

printf("%16.0f\n", s);
return 0;
}
