#include "class_cpp_demo.hh"

Polynomial::Polynomial(double *a, int n)
  : _a(a), _n(n)
{
      // nothing
}

double Polynomial::eval(double x)
{
    double v = 0.0;
    double x_i = 1.0;
    for (int i = 0; i < _n; ++i)
    {
        v += _a[i] * x_i;
        x_i *= x;
    }
    return v;
}

