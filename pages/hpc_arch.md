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

Here, we try to answer "what is a computer?" a bit more carefully than
we might have understood it to be.  The modern cache-based computer
is a complicated beast, with a variety of special-purpose registers
that can greatly accelerate how much "work" we can do.  We'll start
with the basic unit of work, the floating-point operation, and then
try to understand what our machines should, in theory, be capable of
doing.  We'll then show that may not be the case...ever.

<!--
********* STAGE 1 - DESIRED RESULTS ********************************************
-->

## Learning Outcomes

<!--
      What course goals or outcomes will this lesson address?
-->

 - Students will be able to choose the proper tool.
 - Students will be able to list the basic components of a modern
   computer.
 - Students will know how to perform basic timing of their
   programs.

## Essential Questions

<!--
      What question(s) will your students be able to answer by the end of
      instruction?
-->

 - How fast can I actually go?

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

Hager and Wellein, Introduction to High Performance Computing for
Scientists and Engineers (Chapman & Hall/CRC Computational Science)
is a great resource for performance-oriented, scientific programmers.


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

  - Students will describe their CPUs and memory.
  - Students will using basic timing functions to estimate FLOPS
    for a simple program.

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

  - Read [Ch. 1](https://k-state.instructure.com/files/14392374/download?download_frd=1) of Hager and Wellein.
  - Review how to get information about your CPU and memory and find out
    the clock speed (Ghz), total memory (GB), caches (MB?), etc.

### Live Activities

  1. Review the basic structure of a computer.
  2. Consider the various enhancements that let us go beyond
     one FLOP/cycle.
  3. Perform simple test cases with optimization flags, etc.
  4. Implement/use a basic timer to estimate compute FLOP/S.

### Videos

- [Video](tbd)
  and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/HPC_notes.ipynb)



### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
