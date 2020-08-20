<!--
This "lecture" or "lesson" template is adapted from the one provided here:
 http://www.buffalo.edu/ubcei/enhance/teaching/lesson-planning.html
Although the page produced from this is learner-facing, some of the
lesson plan structure
-->

# Getting Set Up                                                                     

## Summary

<!--
Short description of the lesson.
-->

In this lesson, the course administrivia is summarized.  A broad overview
of the course intention and content is provided.  Finally, students are
directed to the appropriate installation of a Linux or Linux-like environment
needed for learning the shell.  This environment will also be used optionally
later on for C++ development.

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

[Installing Windows Subsystem for Linux](https://wiki.ubuntu.com/WSL)

[Installing X Server for WSL](https://sourceforge.net/projects/vcxsrv/)


[Installing Ubuntu in VirtualBox](https://itsfoss.com/install-linux-in-virtualbox/)




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

  - Students will report their hardware and operating system.
  - Students will install the appropriate version of Linux.
  - Students will demonstrate their Linux installation works by performing a simple test.
  - Students will reflect on their learning by completing their daily log and
    by revisiting the use of Linux in future tasks.


<!--
********* STAGE 3 - LEARNING PLAN ****************************************
-->


## Learning Plan

(FYI: This is where I will put the things that (1) we do in recitation or
in the video, (2) that you should be doing in advance, and/or(3) that you
should be thinking about for next time.)

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

  Students should read the class Syllabus.

  Students should come to class with a suitable laptop computer or make sure
  to follow the recorded lesson to repeat the process at home.

  Students should ensure they have access to the websites listed above
  under resources.

### Live Activities

  (Note, some of these may be repeated in older videos, but I intend to
    use my live time with your to go through most of the steps.  Sometimes,
    we'll have to explore truncated versions of planned activities.)

  1. Introduction to Linux (brief; video provides more detail)
  2. Navigate to instructions for the majority.  This is likely WSL.
  3. Work through the instructions linked to above with the students.  
     Debug situations as is necessary.  Remember to *enable* WSL first,
     which requires the restart.
  4. Open the Ubuntu terminal.  Update as needed or recommended.
  5. Restart, etc., as needed.
  6. Demonstrate a few applications that preview the `bash` introduction.
  7. Install the `X` server to enable graphical windows (e.g., `gedit`).
  8. Install `gedit`.
  9. Debrief with students about remaining issues.

### Videos

 - [Lecture, Fall 2019](https://mediasite.k-state.edu/mediasite/Play/b074b6d30eba4ef0abb4e63ffdeb698e1d)
   and [slides](https://k-state.instructure.com/courses/95043/modules/items/2396248). Note, this video has lots of "empty" space since we're
   all installing Linux in a more time consuming manner than WSL.  However, you can use this as a guide for a VirtualBox installation of Ubuntu or Linux Mint on either Windows or OS X.
 - [Recitation, 08/19/2020](https://mediasite.k-state.edu/mediasite/Play/08faea2bf95d4be0848b703100bdb7651d); I think the microphone on the desk failed!
 - [Recitation, 08/21/2020](https://mediasite.k-state.edu/mediasite/Play/56612194f4a544f99ecf297a985abf631d)

## Useful Tips (To Be Updated As We Learn!)

  - Type `explorer.exe .` in the terminal to launch File Explorer and
    explore your Linux directory.  Remember, launch the terminal by finding
    the Ubuntu app and opening it.
