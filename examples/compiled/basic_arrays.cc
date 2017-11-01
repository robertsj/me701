// demonstration of basic arrays in C++

// system-level includes
#include <vector>
#include <cstdio>

// local includes
#include "basic_arrays_functions.hh"

int main(int argc, char* argv[])
{
    // A fixed-sized array of floating-point values
    int n = 100;
    double a[n];
    for (int i = 0; i < n; ++i)
        a[i] = 1.0;
    
    // A dynamically-sized array of the same
    double *b = new double[n];
    for (int i = 0; i < n; ++i)
        b[i] = 2.0;
    
    // A dynamically-sized "array" using std::vector
    std::vector<double> c(n, 3.0);

    // How to pass arrays?
    passing_dumb_arrays(a, n);
    passing_dumb_arrays(b, n);
    passing_dumb_arrays(&c[0], n); // depends on a dumb pointer under the hood!

    // How about vectors?
    std::printf("           original value of c[1]: %6.2f\n", c[1]);
    pass_vector_by_value(c);
    std::printf("value of c[1] after pass by value: %6.2f\n", c[1]);
    pass_vector_by_reference(c);
    std::printf("  value of c[1] after pass by ref: %6.2f\n", c[1]);
    pass_vector_by_pointer(&c);
    std::printf("  value of c[1] after pass by ptr: %6.2f\n", c[1]);
    return 0;
}



