# Sources of Numerical Error                                                       

## Summary

Computers most often work with data encoded in a binary (1's and 0's) format.
We humans tend to think in decimal.  To go between the two formats on a
machine with finite memory requires we make approximations all the time,
even if we don't notice.  We'll cover binary and decimal representation with
a focus on numerical applications.  However, the core ideas are
important to any low-level signal processing and data handling
that we do later on.

## Resources

- Context for errors from [finite differences](https://robertsj.github.io/me400_notes/lectures/Numerical_Differentiation.html).

- [Wikipedia article](https://en.wikipedia.org/wiki/IEEE_754) on
  the IEEE_754 floating-point standard and tinker with

- [IEEE754 converter tool](https://www.h-schmidt.net/FloatConverter/IEEE754.html).

##  Evidence of Student Learning


  - Students will convert fractional numbers from binary to decimal.
  - Students will convert fractional numbers from decimal to binary.
  - Students will apply a finite-difference approximation to a function
    and describe the relationship between the error of the approximation
    and the size of the finite step used.
  - Students will reflect on their learning by completing their daily log.


## Learning Plan

### Before Lecture

  - Skim [finite differences](https://robertsj.github.io/me400_notes/lectures/Numerical_Differentiation.html) for context.
  - Skim the [Wikipedia article](https://en.wikipedia.org/wiki/IEEE_754) on
    the IEEE_754 floating-point standard and tinker with
    [this neat tool](https://www.h-schmidt.net/FloatConverter/IEEE754.html).

### During Lecture

  1. Review finite difference approximations for derivatives and 
     explore the resulting error.
  2. Define fixed-point and floating-point numbers.
  3. Convert between binary and decimal values.
  4. Explore the basic limits of the IEEE 754 floating-point system.
  4. Use Numpy's various float types to characterize the numerical round-off
     error of an algorithm.

### After Lecture

 - [Lecture, F2019](https://mediasite.k-state.edu/mediasite/Play/b88e55a077fb4690be57da00965999751d)
   and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/SourcesOfNumericalError.ipynb)

### Jeremy's Notes

Finite differences will drive the linear systems we construct and solve in the next two lessons.
