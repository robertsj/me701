#include <cstdio>
int main()
{
  double a[3][3];
  double k = 0;
  for (int i = 0; i < 3; ++i)
  {
      for (int j = 0; j < 3; ++j)
      {
          a[i][j] = k;
          k = k + 1.0;
      }
  }
  double *b = &a[0][0];
  for (int i = 0; i < 9; ++i)
  {
      std:printf("%6.2f\n", b[i]);
  }
  return 0;
}
