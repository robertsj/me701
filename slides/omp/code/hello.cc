#include <omp.h>
#include <cstdio>
using std::printf;
int main()
{
#pragma omp parallel
{
 int nt = omp_get_num_threads();
 int id = omp_get_thread_num();
 printf("hello world from %i "
        "of %i\n", id, nt);
}
}
