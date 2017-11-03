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
    passing_dumb_arrays(&c[0], n); // dumb pointer under the hood!

    // How about vectors?
    std::printf("           original value of c[1]: %6.2f\n", c[1]);
    pass_vector_by_value(c);
    std::printf("value of c[1] after pass by value: %6.2f\n", c[1]);
    pass_vector_by_reference(c);
    std::printf("  value of c[1] after pass by ref: %6.2f\n", c[1]);
    pass_vector_by_pointer(&c);
    std::printf("  value of c[1] after pass by ptr: %6.2f\n", c[1]);

    // what about 2-D arrays?
    double a2[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}}; 
    std::printf("  a2[1][1] is %6.2f\n", a2[1][1]);
    double **b2;
    b2 = new double*[3]; // an array of pointers;
    int k = 1;
    for (int i = 0; i < 3; ++i)
    {
      b2[i] = new double[3];
      for (int j = 0; j < 3; ++j)
      {
        b2[i][j] = ++k; // 6? what if k++?
      }
    }
    std::printf("  b2[1][1] is %6.2f\n", b2[1][1]); 
    
    // are we forgetting something?
    return 0;   
}



