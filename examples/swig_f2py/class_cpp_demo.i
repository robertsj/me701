// The syntax is %module module_name, i.e., the name
// you want to import.  All of the C++ includes you need
// should be included here.
%module class_cpp_demo
%{
#include "class_cpp_demo.hh"
%}

// OPTION 2 (inspired by http://wiki.scipy.org/Cookbook/SWIG_NumPy_examples)
// this stuff is boiler plate:
%{
#define SWIG_FILE_WITH_INIT
%}
%include "numpy.i"
%init %{
  import_array();
%}
// The following is an example of a SWIG "typemap".  This is an advanced
// feature that I've only ever tinkered with seriously for one project, but 
// I've **used** the labor of others liberally.

// This is what we want for input arrays that should not get changed
%apply (double* INPLACE_ARRAY1, int DIM1) {(double* a, int n)}

// INCLUDE THE HEADER FILE WITH THE ACTUAL DECLARATIONS
%include "class_cpp_demo.hh"
