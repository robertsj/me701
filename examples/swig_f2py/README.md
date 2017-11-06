# README

Simple examples of SWIG and f2py are presented.  This can be 
a tricky process, and I didn't start from scratch.  For SWIG,
I borrowed the updated numpy.i (usually comes with NumPy) from

    https://github.com/numpy/numpy/pull/2923/files

This let's it work with Python 3.

I also borrowed the typemap usage for SWIG from 
 
    http://wiki.scipy.org/Cookbook/SWIG_NumPy_examples

As you'll see, SWIG is the more complicated beast, but so, too, is
C++ a more complicated beast than Fortran.
