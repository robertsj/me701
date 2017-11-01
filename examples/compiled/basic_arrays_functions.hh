// include guard
#ifndef basic_arrays_functions_hh
#define basic_arrays_functions_hh

// system-level includes
#include <vector>

// declare helpful typedef (a "shortcut")
typedef std::vector<double> vec_dbl;

// declare functions, etc.
void passing_dumb_arrays(double *a, const int n);
void pass_vector_by_value(vec_dbl a);
void pass_vector_by_reference(vec_dbl &a);
void pass_vector_by_pointer(vec_dbl *a);

#endif // basic_arrays_functions_hh 
