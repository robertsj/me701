<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# Core Features of C++                                                

## Summary

<!--
Short description of the lesson.
-->

The core language features of C++ are presented and applied to develop
simple, standalone, compiled programs.  The material is presented
as "C++ for programmers."  In other words, students must come into this
with a solid background in another language (e.g., Python).

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

Allen Downey, *Think C++* is available for
free [online](http://greenteapress.com/thinkcpp/thinkCScpp.pdf) and is a nice,
basic introduction to programming using C++ as the language.

VS Code from WSL will be my default approach for working with C++ code
when an IDE is needed (sometimes, a quick use of `nano` will suffice).
With WSL and the remote extension installed already, you should need
only install the C/C++ extension.  
See more [here](https://code.visualstudio.com/docs/cpp/config-wsl)

Although any editor is fine for creating C++ programs, I've personally
used Eclipse the most for my own work.  The latest version can be
downloaded [here](https://www.eclipse.org/downloads/).  For this class,
I recommend the `Eclipse IDE for Scientific Computing`, which is one of
the options you'll see in the Eclipse Installer options.  Although
Eclipse is cross platform, I will be using it from a Linux or
Linux-like environment with open-source compilers.



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

  - Students will compile a sample program in the Linux command line.
  - Students will define and use variables to create their own C++ program.
  - Students will create a program with functions to solve tasks.
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

  - Install the GNU compiler kit.  On Linux (including WSL), you can do this
    by executing `sudo apt install build-essential gdb`.  For OS X users,
    you can get equivalent tools from XCode (ask if needed).
  - Pick an editor you want to use.  For VS Code users, check out these
    [instructions](https://code.visualstudio.com/docs/cpp/config-wsl) for
    getting your WSL-enabled, VS Code installation ready for C++.
  - Read Chapters 1--7 of Allen Downey, *Think C++*; it's
    available for free [online](http://greenteapress.com/thinkcpp/thinkCScpp.pdf).  
  - Clone [this repository](https://github.com/me701/organizing_cpp_code)

### Live Activities

  1. Brief discussion of `c++` and its types and operators
  2. Demonstrate basic `if` statements and loops.
  3. Demonstrate basic functions.
  4. Use the compiler directly and use a Makefile to compile a program.

### Videos

 - [C++, VS Code, and WSL](https://youtu.be/lxDB8PAegZU)
   A.bout 10 min. Install GNU compilers; install VS Code C++ extension for WSL; hello world.]
 - [C++ Core Features](https://mediasite.k-state.edu/mediasite/Play/d0e9a90978af49229bf7c0fd327ca4a51d)
   and [slides](https://github.com/robertsj/me701/blob/f2019/lectures/CppBasics.ipynb).
   If you want to execute the notebook, you will need to install the `c++` kernel for Jupyter.
   That is not necessary; all commands I use can be executed directly in the terminal or
   saved and run as scripts.  Eclipse is also used.
 - [C++ Functions](https://mediasite.k-state.edu/mediasite/Play/94d5dfd001864587b967f26187f15fea1d)
   and [slides](https://github.com/robertsj/me701/blob/f2019/lectures/BasicsOfCppCodeOrganization.ipynb).
   Eclipse is used.

### Useful Tips (To Be Updated As We Learn!)


<!--  

NOTES  




-->
