<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# SciPy and Sparse Systems                                                              

## Summary

<!--
Short description of the lesson.
-->

Last time, we used NumPy to construct and solve linear systems.  Sometimes,
however, such constructions are just too expensive, with respect to both
computational effort and memory requirements.  Here, we look at SciPy and
its interface for defining sparse systems, i.e., systems whose matrix
$\mathbf{A}$ has a whole bunch of zeros.

<!--
********* STAGE 1 - DESIRED RESULTS ********************************************
-->

## Learning Outcomes

<!--
      What course goals or outcomes will this lesson address?
-->



## Essential Questions

<!--
      What question(s) will your students be able to answer by the end of
      instruction?
-->

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

The [NumPy](https://numpy.org/) project provides a lot of documentation and
support, including [this introductory tutorial](https://numpy.org/devdocs/user/quickstart.html).

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

  - Students will install (if needed) and import SciPy modules.
  - Students will construct SciPy sparse matrices to represent
    sparse linear systems.
  - Students will use SciPy's sparse solvers to solve sparse
    systems of the form $\mathbf{Ax}=\mathbf{b}$.
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

  - Review [linear systems](http://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_2/module_2.html).
  - Review [least squares](http://robertsj.github.io/python_for_engineers/courses/pythonic_apps_2/modules/module_3/least_squares.html)


### Live Activities

  1. Revisit linear system using sparse matrices.
  2. Solve sparse system with SciPy.
  3. Discuss project.

### Videos

 - [Lecture, F2019](https://mediasite.k-state.edu/mediasite/Play/0f4ca4afbdb54c29a8104dc05711fb431d),
   [slides](https://github.com/robertsj/me701/blob/f2020/lectures/SparseSystemsAndIterativeMethods.ipynb),
   and [supplementary notes](https://k-state.instructure.com/courses/95043/files/14392369/download?download_frd=1).


### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
