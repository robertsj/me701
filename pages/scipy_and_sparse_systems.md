# SciPy and Sparse Systems                                                              

## Summary


Last time, we used NumPy to construct and solve linear systems.  Sometimes,
however, such constructions are just too expensive, with respect to both
computational effort and memory requirements.  Here, we look at SciPy and
its interface for defining sparse systems, i.e., systems whose matrix
$\mathbf{A}$ has a whole bunch of zeros.


## Resources

SciPy Lecture on [Sparse Matrices](https://scipy-lectures.org/advanced/scipy_sparse/index.html)

##  Evidence of Student Learning

  - Students will install (if needed) and import SciPy modules.
  - Students will construct SciPy sparse matrices to represent
    sparse linear systems.
  - Students will use SciPy's sparse solvers to solve sparse
    systems of the form $\mathbf{Ax}=\mathbf{b}$.
  - Students will reflect on their learning by completing their daily log.

## Learning Plan

### Before Lecture

  - Review [linear systems](http://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_2/module_2.html).
  - Review [least squares](http://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_3/least_squares.html)


### During Lecture

  1. Revisit linear system using sparse matrices.
  2. Solve sparse system with SciPy.

### After Lecture

 - [Rohan's Guest Lecture](https://mediasite.k-state.edu/mediasite/Play/f7d9276f75fb4e2b91e45892b273a6771d)
 - [Lecture, F2019](https://mediasite.k-state.edu/mediasite/Play/0f4ca4afbdb54c29a8104dc05711fb431d),
   [slides](https://github.com/robertsj/me701/blob/f2020/lectures/SparseSystemsAndIterativeMethods.ipynb),
   and [supplementary notes](https://k-state.instructure.com/courses/95043/files/14392369/download?download_frd=1).


### Jeremy's Notes

Rohan Amare provided a guest lecture on sparse systems based on his own work.