<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# Working with Python                                                                 

## Summary

<!--
Short description of the lesson.
-->

In this lesson, we get up to speed with Python and how to use it on
our machines from both the terminal (WSL or otherwise) and graphical
options.  We'll also look at some of the variable types in Python.

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

The recommended Python framework is [Anaconda](https://www.anaconda.com/products/individual),
which comes with everything we will need by default for this part of the
course.

A fairly representative set of topics is provided by my old
ME 400 notes [Python for Engineers](https://robertsj.github.io/me400_notes/index.html).

Other resources for Python include

- Downey, Think Python; [free to download](https://greenteapress.com/wp/think-python/);
  This is an introductory text that has been used in ME 400 previously.  Use it as
  a reference for basic programming logic and Python syntax.

- H. Langtangen. *Python Scripting for Computational Science*, 3rd ed. Springer, (2009). ISBN: 978-3540739159
  This is an older, somewhat outdated text.  However, I like it because it shows how versatile Python can be
  and where it entered into the technical computing domain.

- B. Shapiro. *Scientific Computation: Python Hacking for Math Junkies*. Sherwood Forest
  Books, (2015). ISBN: 978-0692366936.  This book is just fun.  Each chapter is
  pretty focused on some math, computational, or similar, technical problem.  


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

  - Students will be able to select and install an appropriate version of
    Python and related packages.
  - Students will write and execute a simple program in Python.
  - Students will use Python as a "graphing calculator"
    to compute and visualize results for simple problems.
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

  - Bring a laptop with [Anaconda](https://www.anaconda.com/products/individual)
    installed on your machine.  It is fine to install it on Windows.  We will
    learn how to access that from the terminal if needed.
  - Review lectures 1 through 11 of [Python for Engineers](https://robertsj.github.io/me400_notes/index.html).
    Most of this should be *review* given the prerequisites for this class, but
    I may include some content there that less familiar.
  - Put together a list of the programming topics that is least familiar,
    most anxiety-inducing, etc.  I want to focus on the weakest links in
    the time we have with Python.


### Live Activities

  1. Check that Python is available from Windows and the terminal.
  2. Interactive Python exercises (using, e.g., IDLE in CMD.exe)
  3. Scripted Python exercises (using, e.g., Spyder)

### Videos

 - [Slides from F2019](https://github.com/robertsj/me701/blob/f2020/lectures/OverviewOfPython.ipynb).

 - [Video - Part 1](https://ksu.zoom.us/rec/share/w3Eq2XM7ig0bXXMARbRJdjg_VedUMDasaRF8MzHQaTqy2s0svxNZIfZOQw52febp.GQW52qNzi_W5qMVx?startTime=1599760003000) - discusses Anaconda on Windows and on WSL; VS Code with
   Anaconda; and using VS Code from WSL.  Watch at 2x speed for sanity and comedy.

    * 00:00-07:00 getting Anaconda on WSL
    * 07:00-12:00 getting VS Code and Python/WSL extensions
    * 12:00 or so is a brief comment about Anaconda for Windows 10 (not WSL)
    * 12:00-20:00 basic Python types (`int`, `float`, `str`, `bool`)
    * 20:00-26:00 Python containers (`list`, `tuple`, and `dict`)
    * 26:00-32:00 Python in WSL using `code .` to open VS Code from the terminal.
    * 32:00-..... Me flailing until I remember that I need X11.  See next video for the fix.

 - [Video - Part 2](https://ksu.zoom.us/rec/share/w3Eq2XM7ig0bXXMARbRJdjg_VedUMDasaRF8MzHQaTqy2s0svxNZIfZOQw52febp.GQW52qNzi_W5qMVx?startTime=1599762592000) - quick fix-up that shows how to get Python plots to
   load from WSL.



### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
