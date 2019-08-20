# ME 701 - Development of Computer Applications in Mechanical Engineering

This document provides the syllabus and course policies.
Please read it carefully.

The rest of this repository contains notes, examples, and other resources
for ME 701 - Development of Computer Applications in Mechanical Engineering, 
taught at Kansas State University.  All materials were developed by 
Jeremy Roberts.

## Course Details

### Time and Place

11:30--12:20pm MWF in DU 1032


### Instructor
 - Jeremy Roberts
 - 137D Ward Hall
 - Office Hours by appointment; see my [calendar](https://calendar.google.com/calendar/embed?src=j.alyn.roberts%40gmail.com&ctz=America/Chicago).

### Teaching Assistant
 - Richard Reed
 - 133B Ward Hall
 - Office Hours TBD.

## Course Description and Objectives

This course will provide students with the skills needed to apply computation successfully in their research and professional endeavors. This begs the question, “what is computation?” In this course, all we want to do is make the computer do what we want it to do. Our approach doesn’t always have to be the fastest or most elegant—though both are admirable qualities—but it must get the right answer.

Along the way, students will learn (or review) basic numerical methods and use them to solve problems typical in mechanical and nuclear engineering. Students will also be exposed to a variety of special topics, including graphical user interfaces, visualization tools, and parallel computing.

**Students should at a minimum leave the course with (1) a basic understanding of how to do scientific work on Linux machines, (2) programming skills at a level needed for solving problems typical of engineering, and (3) the ability to select the appropriate language or tool for the job.**

## Textbook

There is no perfect book for this course, and most reference material can easily be found online. In some cases, electronic materials (book excerpt, article, etc.) will be provided to the student. 

However, there are good books for parts of the material we’ll cover. I have several, and you’re more than welcome to borrow them to determine whether they belong on your shelf, too. When appropriate, I’ll assign excerpts as reading.

A book that aligns well with much of the early content (and much of the spirit) of this course is

- A. Scopatz and K. Huff. Effective Computation in Physics. O’Reilly Media, (2015). ISBN:
  978-1491901533

which provides a nice overview of Python at the level (and with the pace) of this class. It also surveys other topics important to effective computing in the sciences, including the Linux command line, version control, data storage, and (some) visualization.  This book is **recommended** for students who like a print reference.

A thorough overview of the command line in Linux is given by

- W. Shotts, Jr. *The Linux Command Line: A Complete Introduction*, No Starch Press (2012).
  ISBN: 978-1-59327-389-7. Available free from [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php) 
  
for which a free PDF version is available.  Readings will be assigned from this book.

Other books that present Python in a way useful to students of scientific computing include

- H. Langtangen. *Python Scripting for Computational Science*, 3rd ed. Springer, (2009). ISBN: 978-3540739159
- J. Stewert. *Python for Scientists*. Cambridge University Press, (2014). ISBN:978-1107686427
- B. Shapiro. *Scientific Computation: Python Hacking for Math Junkies*. Sherwood Forest
  Books, (2015). ISBN: 978-0692366936

and, although not a full-fledged book, you might find my online Python materials for ME 400 useful:

- J. Roberts. *Python for Engineers* (2016). 
  [http://robertsj.github.io/me400_notes/index.html](http://robertsj.github.io/me400_notes/index.html)

Despite the utility of Python for scientific computing, there remains a need to understand a bit about compiled languages, particularly for development of high-performance code and maintenance of legacy code.  In this course, C++ will be introduced and used, and some appropriate resources include:

- Allen Downey, *Think C++* [It's available for free [online](http://greenteapress.com/thinkcpp/thinkCScpp.pdf) and is a nice, basic introduction to programming using C++ as the language.]
- Francis and Whiteley, *Guide to Scientific Computing in C++*, Springer (2012).  [Presents a short overview of basic C++ syntax with various applications of interest in scientific computing.]
- Stroustrup. A Tour of C++. Addison-Wesley Professional (2018). [An excellent survey, especially for those who already know a bit of C++ or are very experienced in another language.]


For development of Qt-based graphical user interfaces (GUI’s) in Python, the essential reference is

- Summerfield, *Rapid GUI Programming with Python and Qt*, Prentice Hall (2007).   [However, this is swiftly becoming dated since Qt has moved on to version 5, and many things are not backwards compatible.  We'll leverage existing tutorials like those [here](http://zetcode.com/gui/pyqt5/)]

Finally, the scope of parallel programming is large. For topics related to high-performance computing, OpenMP, and MPI we’ll
cover in the last quarter of the course, the standard references are

- G. Jost and R. van der Pas. Using OpenMP: Portable Shared Memory Parallel Programming, MIT Press, (2007). ISBN: 978-0262533027
- W. Gropp, E. Lusk, and A. Skjellum. Using MPI: Portable Parallel Programming with the Message Passing Interface, 2nd ed. MIT Press, (1999). ISBN: 978-0262571326
- G. Hager and G. Wellein. Introduction to high performance computing for scientists and engineers. CRC Press (2010). [Excerpts of this book will be provided.]



## Prerequisites

ME 400 (Computer Applications in Mechanical Engineering) or equivalent.  In other words, you should already know how to program at a basic level.

## Lectures and Laptops

Because of the material covered in ME 701, the lectures need to be rather hands-on, informal tutorials. If you have a laptop, you should bring it to class to do in-class examples, ask questions about homeworks, and to write any other code when necessary. If you do not have a laptop, I may have a couple old ones available for in-class use.

## Grading

Grading for the course is based on the following breakdown: 

- 11 homeworks [one free drop drop] (50%)
- Two programming projects (40%)
- Participation (10%)


Although I do not subscribe to the standard 90/80/70 rule in general, that scale has been pretty
accurate the last three semesters of my teaching this course. 


Each **homework** is equally weighted. Homework will be due more frequently in the early, foundational part of the course and will always be announced at least one week before its due date and time. You may drop the lowest homework score.  No homework received after grading has begun will be accepted.  Your best (and guaranteed) bet is to submit by the deadline.  Homework will be primarily an individual effort, but some assignments will require pairs of students.

The **programming projects** provide an opportunity for you to sythesize the tools learned throughout the course.  The first one emphasizes Python, while the second one will emphasize C++.  These projects are more in depth and more open-ended than a typical homework problem.  More details will be announced later on.

In a small, hands-on course like this, **participation** in lectures is essential.  Active participation, in my view, means doing any assigned reading (or other preparation) and coming to class ready to engage with the material.  Regularly be present, take notes (before, during, and after lecture), ask questions, and follow up, as needed, during office hours.  This part of the assessment is going to be a [metacognitive](https://en.wikipedia.org/wiki/Metacognition) exercise for *you*, the student.  For each lecture, you are going to summarize (briefly) how you prepared for lecture, what you contributed to lecture, and which topic is least clear.  Eventually, you will "commit" these entries to an online repository where the TA and I can review them periodically for feedback on the course.  By the end of the semester, you will have a pretty clear view of your learning throughout the course (and I will, too).

> *Please note*: The programming required for both homework and projects might be very hard, especially if your
  programming skills coming into the class are weak.  However, the tasks will not be
  impossible if you get an early start on them!

## Course Calendar

The following is a preliminary schedule of lectures.  Some topics are subject to change.


| Lecture   |  Date            | Topics                                                                      |
|----|-------------------------|-----------------------------------------------------------------------------|
|	1	|	Mon, Aug 26	|	Administrivia. Installation/configuration of Linux Mint.	|
|	2	|	Wed, Aug 28	|	Getting to know the open-source world.	|
|	3	|	Fri, Aug 30	|	The Linux command line and the shell; Basic commands.	|
|		|	Mon, Sep 02	|	HOLIDAY	|
|	4	|	Wed, Sep 04	|	More on the command line. Environment variables, profiles, etc.	|
|	5	|	Fri, Sep 06	|	Basic shell scripting (using bash).	|
|	6	|	Mon, Sep 09	|	Version control with Git.	|
|	7	|	Wed, Sep 11	|	GitHub for version control of collaborative projects.	|
|	8	|	Fri, Sep 13	|	Python overview and installation. Built-in types and functions.  Python as a "graphing calculator."	|
|	9	|	Mon, Sep 16	|	The structure of Python code: conditionals, loops, and functions.  The debugger.	|
|	10	|	Wed, Sep 18	|	Modules. Unit testing.	|
|	11	|	Fri, Sep 20	|	Sources of numerical error.  Roundoff error.  Truncation error.	|
|	12	|	Mon, Sep 23	|	Linear systems and NumPy arrays.  Least squares.	|
|	13	|	Wed, Sep 25	|	SciPy, sparse systems, and iterative solutions.	|
|	14	|	Fri, Sep 27	|	Selected SciPy applications (or continuation).	|
|	15	|	Mon, Sep 30	|	Overview of objected-oriented programming in Python. Classes, objects, and methods.	|
|	16	|	Wed, Oct 02	|	More on OOP. Inheritance.	|
|	17	|	Fri, Oct 04	|	More on OOP.	|
|	18	|	Mon, Oct 07	|	Applications of OOP.	|
|	19	|	Wed, Oct 09	|	Graphical-User Interfaces (GUIs) with PyQt5	|
|	20	|	Fri, Oct 11	|	More on GUIs	|
|	21	|	Mon, Oct 14	|	More on GUIs	|
|	22	|	Wed, Oct 16	|	A survey of I/O formats (basic text, NumPy, JSON, HDF5, etc.)	|
|	23	|	Fri, Oct 18	|	Regular expressions.	|
|	24	|	Mon, Oct 21	|	Advanced Matplotlib (and other Python-based plotting)	|
|	25	|	Wed, Oct 23	|	More on Matplotlib.  Publication-quality graphics.	|
|	26	|	Fri, Oct 25	|	VisIt for visualization of large data sets. 	|
|	27	|	Mon, Oct 28	|	A rapid introduction to C++. Syntax overview (types, selection, and iteration).  The compiler.	|
|	28	|	Wed, Oct 30	|	Eclipse IDE and graphical debugging.	|
|	29	|	Fri, Nov 01	|	Functions, organizing code, and the Makefile.	|
|	30	|	Mon, Nov 04	|	Pointers, arrays, and memory management.  Valgrind.	|
|	31	|	Wed, Nov 06	| Classes, objects, and methods: Part Deux.	|
|	32	|	Fri, Nov 08	|	Exception-handling and defensive programming. 	|
|	33	|	Mon, Nov 11	|	Templates and the standard template library (STL): vectors, maps, and more.	|
|	34	|	Wed, Nov 13	|	Using Python with C++: an overview of SWIG.	|
|	35	|	Fri, Nov 15	|	Using libraries: BLAS, LAPACK, GNU scientific library and more. 	|
|	36	|	Mon, Nov 18	|	Code profiling and tuning.	|
|	37	|	Wed, Nov 20	|	Computational performance and OMILAT.	|
|	38	|	Fri, Nov 22	|	Overview of computer architectures and parallel computing.  Navigating Beocat.	|
|		|	Mon, Nov 25	|	HOLIDAY	|
|		|	Wed, Nov 27	|	HOLIDAY	|
|		|	Fri, Nov 29	|	HOLIDAY	|
|	39	|	Mon, Dec 02	|	Introduction to multithreaded parallelism via OpenMP.	|
|	40	|	Wed, Dec 04	|	OpenMP continued.	|
|	41	|	Fri, Dec 06	|	OpenMP continued.	|
|	42	|	Mon, Dec 09	|	Introduction to parallel compution on heterogeneous systems with MPI.	|
|	43	|	Wed, Dec 11	|	MPI continued.	|
|	44	|	Fri, Dec 13	|	MPI continued.  Course wrapup.	|
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      


## Academic Honesty

Kansas State University has an Honor System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one’s work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor System. The policies and procedures of the Honor System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. The honor system website can be reached via the following URL: www.ksu.edu/honor. A component vital to the Honor System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: “On my honor, as a student, I have neither given nor received unauthorized aid on this academic work.” A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.

## Students with Disabilities

Students with disabilities who need classroom accommodations, access to technology, or in- formation about emergency building/campus evacuation processes should contact the Student Access Center and/or their instructor. Services are available to students with a wide range of disabilities including, but not limited to, physical disabilities, medical conditions, learning disabilities, attention deficit disorder, depression, and anxiety. If you are a student enrolled in campus/online courses through the Manhattan or Olathe campuses, contact the Student Ac- cess Center at accesscenter@k-state.edu, 785-532-6441; for Salina campus, contact the Academic and Career Advising Center at acac@k-state.edu, 785-826-2649.

## Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article VI, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.
