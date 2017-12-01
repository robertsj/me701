#include <omp.h>
#include <cstdio>

using std::printf;

int main()
{
  int n = 2e7;
  double s;
#pragma omp parallel \
   private(i) shared(n, s)
{
  s = 0.0;
#pragma omp for
  for (int i = 0; i < n; ++i)
  {
    // race condition!
    s = s + i; 
    // all threads work on same
    // s and overwrite due to 
    // finite memory speed
  }
} // end parallel

printf("%16.0f\n", s);
return 0;
}
