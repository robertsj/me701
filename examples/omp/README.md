# OpenMP Tutorial

This directory contains files to support a short, three-day overview of
OpenMP, a standard for multi-threaded, parallel computing in C++ and Fortran.
Here, the focus is limited to C++.  The tutorial is organized by exercise.

## Exercise 1 - Hello, World

Use OpenMP to produce a program that displays several messages of the form
`Hello, from thread 1 of 4`.  This will require that students use the 
`parallel` directive, access the thread ID, and access the number of threads.
To be interesting, students should also *modify* the number of threads.

Introduces
 - concept of fork/join model 
 - `parallel` directive
 - `<omp.h>`
 - `omp_get_num_threads`
 - `omp_get_thread_num`
 - `OMP_NUM_THREADS`
 
## Exercise 2 - `c = a + b`

Given two std::vectors `a` and `b`, compute their element-wise sum `c` in 
parallel using just the `parallel` directive, the thread ID, and the number
of threads.

Introduces 
  - `omp_get_wtime`
  - concept of "work sharing"
  - concept of shared memory

## Exercise 3 - `c = a + b` (the easy way)

Repeat Exercise 2 by using the `for` directive, thereby eliminating any
need for explicit work sharing.

Introduces 
  - `for` directive
  
## Exercise 4 - The Parallel Dot Product

Use the `parallel` and `for` directives to compute the dot product of two
arrays `a` and `b`.  Assess the parallel efficiency for various thread
counts and various problem sizes.

Introduces
  - concept of private memory
  - concept of race conditions
  - `critical` directive
  - `atomic` directive
  - `reduce` directive


## Exercise 5 - The Parallel Sum of 1, 2, ..., n

Use the same basic structure from Exercise 4 to compute the sum of 1, 2, ..., n.
How does the performance differ from those of Exercise 4?


Introduces
  - concept of memory bandwidth limitations

## Exercise 6 - Heat Conduction in 2-D with Jacobi Iteration

You are given a basic program that computes the temperature in a 
two-dimensional box subject to fixed boundary temperatures.  Your job
is to parallelize this code and to extract the best performance possible.


