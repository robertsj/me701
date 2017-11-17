#include <cmath>
#include <cstdio>

// return the bigger of a and b
double bigger(double a, double b)
{
  if (a > b)
      return a;
  return b;
}

// return the L_p norm of a, an array of length n
double norm(double *a, int n, int p)
{
    double s = 0;
    for (int i = 0; i < n; ++i)
    {
        s += std::pow(std::abs(a[i]), p);
    }
    return std::pow(s, 1.0/p);
}

// create and fill an array with [start, start+1, ..., start+n]
void range(int *a, int n, int start)
{
    for (int i = 0; i < n; ++i)
    {
        a[i] = start + i;
    }
}


double add_ab(double *a, int m, double *b, int n)
{
   double s = 0;
   for (int i = 0; i < m; ++i)
      s += a[i];
   for (int i = 0; i < n; ++i)
      s += b[i];
   return s;
}

