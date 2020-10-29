<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# HPC Architectures

## Summary

<!--
Short description of the lesson.
-->

The basic timing we did last time is a good tool to have, but sometimes
it's better to profile your code a bit more comprehensively.  Here, we'll
look at how to use tools like `gprof` to figure out where execution
bottlenecks may be hurting your program's performance.

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

 - How fast can I actually go, and which things are stopping me?

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

The [gprof](https://en.wikipedia.org/wiki/Gprof) tool is readily
accessible and gives substantial information about run-time performance
of programs.

There are numerous other [performance tools](https://en.wikipedia.org/wiki/List_of_performance_analysis_tools)
available.   [Valgrind]() includes `cachegrind` and `callgrind` that are
useful tools for understanding execution in more detail.

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

  - Students will use `gprof` to profile a C++ program.
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

  - Read [Ch. 1]() of Hager and Wellein
  - Review [this overview](https://web.eecs.umich.edu/~sugih/pointers/gprof_quick.html) of `gprof`

### Live Activities

  1. Download example code and discuss.
  2. Use `gprof` to understand performance.

### Videos

- [Video](tbd)
  and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/HPC_notes.ipynb)



### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
