#ifndef POLYNOMIAL_HH
#define POLYNOMIAL_HH

class Polynomial
{
  public:

    Polynomial(double *a, int n);
    double eval(double x);

  private:

    double *_a;
    int _n;
};

#endif // POLYNOMIAL_HH
