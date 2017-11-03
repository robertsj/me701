#include "basic_arrays_functions.hh"

#include <cstdio>

// Demonstrate how to pass dumb arrays.  Note, prefer to "const" all 
// incoming scalars (ints, floats, etc.) that are not to change inside 
// the function.  Pedantic, but "defensive"
void passing_dumb_arrays(double *a, const int n)
{
    // do something with the array
    std::printf("a[1] = %6.2f\n", a[1]);
}

void pass_vector_by_value(vec_dbl a)
{
    // do something with the array
    std::printf("a[1] = %6.2f\n", a[1]);
    // change an element
    a[1] = 99;
}

void pass_vector_by_reference(vec_dbl &a)
{
    // do something with the array
    std::printf("a[1] = %6.2f\n", a[1]);
    // change an element
    a[1] = 99;
}

void pass_vector_by_pointer(vec_dbl *a)
{
    // do something with the array
    std::printf("a[1] = %6.2f\n", (*a)[1]);
    // change an element
    (*a)[1] = 101;
}
