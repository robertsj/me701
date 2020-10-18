<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# *Object Oriented C++*: Classes and Objects                

## Summary

<!--
Short description of the lesson.
-->

In this lesson, we learn how to define *classes* that include
a public *interface* and private *attributes*.  The public interface  
include methods for *construction* and *destruction* of an
object and any methods needed to access or modify data an object
encapsulates.  Usually, this data is encapsulated, i.e., it is
not available to the user of the object.  

<!--
********* STAGE 1 - DESIRED RESULTS ********************************************
-->

## Learning Outcomes

<!--
      What course goals or outcomes will this lesson address?
-->

 - Students will be able to select the right tool for the application.



## Essential Questions

<!--
      What question(s) will your students be able to answer by the end of
      instruction?
-->

 - How to we make and use an object?  
 - What is an *initialization list*?
 - Can we have `const` member variables?

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

Allen Downey, *Think C++* is available for
free [online](http://greenteapress.com/thinkcpp/thinkCScpp.pdf) and is a nice,
basic introduction to programming using C++ as the language.


Bjarne Stroustrup, *A Tour of C++*, 2nd Ed., is a survey of C++ written by
the inventor of C++.  It's a nice and short book that discusses the
essential syntax of modern C++.

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

  - Students will define and use a class in a C++ program.
  - Students will understand how various constructors are defined
    and used.
  - Students will understand how a destructor is used.
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

  - Read Chapters 8, 9 and 14 of [Think C++]().
    Note, 8 and 9 deal with C++ `struct`, which is equivalent to a class
    with one small difference (members are by default `public`, not `private`).
  - Review how classes and objects work in Python.
  - Clone [this repository](https://github.com/me701/cpp_classes).

### Live Activities

  1. Present basic structure of a C++ class and compare, as needed, to Python.
  2. Walk through the `Point` class and supporting code.  
  3. Extend the `Point` class and application program.
  4. Define a `Vector` class similar to NumPy arrays.

### Videos

- [OO C++ Classes](tbd).



### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
