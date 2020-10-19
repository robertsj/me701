<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# Binary Data

## Summary

<!--
Short description of the lesson.
-->

In this lesson, we review basic techniques for dealing with raw binary
data in Python.  Data stored in binary format require less memory and fewer
operations to read, write, and process.  Here, we explore how to write
data directly to a binary format.  We also explore a couple of built-in
techniques for storing data arbitrary data to file.


<!--
********* STAGE 1 - DESIRED RESULTS ********************************************
-->

## Learning Outcomes

<!--
      What course goals or outcomes will this lesson address?
-->

 - Students will be able to choose the proper tool.
 - Students will be able to find, load, manipulate, and save
   data to file.


## Essential Questions

<!--
      What question(s) will your students be able to answer by the end of
      instruction?
-->

 - How is data actually stored on file?  Is it machine dependent?

## Resources

<!--
      What resources can be made available to your student to support their
      active learning?
      What formats are best suited to complement your course material?
-->

Binary formats are ubiquitous.  One aspect of a binary format is the order in
which the individual [bytes](https://en.wikipedia.org/wiki/Byte) are stored, i.e., the file's
[endianness](https://en.wikipedia.org/wiki/Endianness).  For most applications,
we use higher-level interfaces that hide such details.  However, when working
with embedded systems, legacy code, and proprietary formats, an understanding
of these low-level details goes a long way.

The primary tools to use low-level `byte`-wise data in Python are
the `byte` and `bytearray` types, the `struct` module and its
`pack` function.



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

  - Students will explain what is meant by "binary data".
  - Students will read and write numerical and other data from and to
    file in binary format.
  - Students will convert a number in base-10 to a number in base-16.
  - Students will use `pickle` to save arbitrary Python objects to
    file in binary format.


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

  - Review how to convert 123 to binary.
  - Review the Python [bytes](https://docs.python.org/3.1/library/functions.html#bytes)
    type
  - Review rules for using [literal values](https://docs.python.org/3.1/reference/lexical_analysis.html#literals).


### Live Activities

  1. Review binary representation and extend to base-16.
  2. Encoding data into byte strings.
  3. Saving byte-wise data to file.
  4. Compare text and binary formats for the same data (including
     `np.save/np.load` and `pickle.dump/pickle.load`).
  5. Brief illustration of how to handle binary data in C++.

### Videos

- [Binary Data](tbd)
   and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/Binary_Data.ipynb)


### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
