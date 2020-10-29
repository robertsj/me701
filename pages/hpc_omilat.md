<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# HPC Case Study: OMILAT

## Summary

<!--
Short description of the lesson.
-->

Only masochists implement linear algebra themselves.  We'll see
why that is by comparing the best code we can write in C++ to the
off-the-shelf tools from the professionals.  

<!--
********* STAGE 1 - DESIRED RESULTS ********************************************
-->

## Learning Outcomes

<!--
      What course goals or outcomes will this lesson address?
-->

 - Students will be able to choose the proper tool.


## Essential Questions

<!--
      What question(s) will your students be able to answer by the end of
      instruction?
-->

 - How fast can I actually go?
 - Is a library a better option?

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

The [BLAS](https://en.wikipedia.org/wiki/BLAS) specification defines
a variety of low-level, vector-vector, matrix-vector, and matrix-matrix
subroutines essential to many numerical computing applications.

The [LAPACK](https://en.wikipedia.org/wiki/LAPACK) specification
builds on BLAS to define solvers for linear and eigen systems,
various decompositions, etc.

Intel's [Math Kernel Library (MKL)](https://en.wikipedia.org/wiki/Math_Kernel_Library) is among the best performing
implementations of BLAS/LAPACK, especially on Intel systems.

The [ATLAS](https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software) library is a BLAS/LAPACK implementation that uses
parameterized code and numerical experiments to "tune"
the final compiled code to one's machine.  A similar approach
was used to produce the [FFTW](https://en.wikipedia.org/wiki/FFTW) library that implements fast Fourier
transforms.

The [Eigen](https://en.wikipedia.org/wiki/Eigen_(C%2B%2B_library)) is a
template (head-only) C++ library that implements BLAS and some of
LAPACK.  Because it uses only headers, it is very easy to incorporate into
existing code.

The [LINPACK](https://en.wikipedia.org/wiki/LINPACK_benchmarks)
benchmark is a widely used for testing the performance of
large-scale compute clusters.  However, it's good for single-cove
studies, too.  We'll use the [Intel implementation](https://software.intel.com/content/www/us/en/develop/documentation/mkl-windows-developer-guide/top/intel-math-kernel-library-benchmarks/intel-distribution-for-linpack-benchmark/overview-of-the-intel-distribution-for-linpack-benchmark.html).

<!--
********* STAGE 2 - ASSESSMENT EVIDENCE ****************************************
-->

##  Evidence of Student Learning

<!--
      How will you assess students’ prior knowledge?
      What criteria will be used to assess student performance?
      What evidence will be collected to demonstrate achievement?
      How will students reflect and self-assess their learning?
-->

  - Students will run several versions of a BLAS-driven program.
  - Students will run the LINPACK and/or similar performance
    benchmarks.
  - Students will reflect on their learning by completing their daily log.

<!--
********* STAGE 3 - LEARNING PLAN ****************************************
-->


## Learning Plan

<!--
List the steps in chronological order to create a timeline of what
will occur in your lesson.

Consider how each of the components below will be included in your
lesson if applicable:

   - Anticipatory Sets/Hooks
       * How will you introduce the material and capture their attention?
   - Teacher Modeling
       * What instructional content and techniques will be incorporated
         into this lesson?
   - Guided Practice
       * How will you scaffold information for your students?
       * How will collaborative learning be used?
   - Learning Activities
       * How will students actively engage with the material?
       * How will students work towards achievement of the learning outcomes?
   - Independent Practice
       * How will students show evidence of learning?
   - Reflection
       * What have you learned about your teaching and content covered in this unit?
       * What changes or adjustments could you make?
       * What were the strongest features of your unit?
       * What are your overall reflections in the course to this point?
   - Conclusion and Preview
       * What should students take away from this lesson?
       * What will happen next? Why?
-->

### Required Preparation

  - Remember how to compute $\mathbf{Ax}$.

### Live Activities

  1. Review the matrix-vector product and implement in C++ using both
     row- and column-wise access.
  2. Compute FLOP/S and compare to estimated peak performance.
  3. Do same but link to MKL instead and compare.
  4. Run HPL to see true peak performance.

### Videos

- [Video](tbd)
  and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/HPC_notes.ipynb)



### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
