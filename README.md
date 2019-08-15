# ME 701 - Development of Computer Applications in Mechanical Engineering

This document provides the syllabus and course policies.
Please read it carefully.

The rest of this repository contains notes, examples, and other resources
for ME 701 - Development of Computer Applications in Mechanical Engineering, 
taught at Kansas State University.  All materials were developed by 
Jeremy Roberts.

## 

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

which provides a nice overview of Python at the level (and with the pace) of this class. It also surveys other topics important to effective computing in the sciences, including the Linux command line, version control, and (some) visualization.

A thorough overview of the command line in Linux is given by

- W. Shotts, Jr. *The Linux Command Line: A Complete Introduction*, No Starch Press (2012).
  ISBN: 978-1-59327-389-7. Available free from [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php) 
  
for which a free PDF version is available.

Other books that present Python in a way useful to students of scientific computing include

- H. Langtangen. *Python Scripting for Computational Science*, 3rd ed. Springer, (2009). ISBN: 978-3540739159
- J. Stewert. *Python for Scientists*. Cambridge University Press, (2014). ISBN:978-1107686427
- B. Shapiro. *Scientific Computation: Python Hacking for Math Junkies*. Sherwood Forest
  Books, (2015). ISBN: 978-0692366936

and, although not a full-fledged book, you might find my online Python materials for ME 400 useful:

- J. Roberts. *Python for Engineers* (2016). 
  [http://robertsj.github.io/me400_notes/index.html](http://robertsj.github.io/me400_notes/index.html)

Despite the utility of Python for scientific computing, there remains a need to understand a bit about compiled languages, particularly for development of high-performance code and maintenance of legacy code.  In this course, C++ will be introduced and used, and some appropriate resources include:

- Francis and Whiteley, *Guide to Scientific Computing in C++*, Springer (2012)
- Stroustrup. A Tour of C++. Addison-Wesley Professional (2018)


For development of Qt-based graphical user interfaces (GUI’s) in Python, the essential reference is

- Summerfield, *Rapid GUI Programming with Python and Qt*, Prentice Hall (2007) 

Finally, the scope of parallel programming is large. For topics related to high-performance computing, OpenMP, and MPI we’ll
cover in the last quarter of the course, the standard references are

- G. Jost and R. van der Pas. Using OpenMP: Portable Shared Memory Parallel Programming, MIT Press, (2007). ISBN: 978-0262533027
- W. Gropp, E. Lusk, and A. Skjellum. Using MPI: Portable Parallel Programming with the Message Passing Interface, 2nd ed. MIT Press, (1999). ISBN: 978-0262571326
- G. Hager and G. Wellein. Introduction to high performance computing for scientists and engineers. CRC Press (2010)



## Prerequisites

ME 400 (Computer Applications in Mechanical Engineering) with at least a B grade or permission of the instructor.

# Lectures and Laptops

Because of the material covered in ME 701, the lectures need to be rather hands-on, informal tutorials. If you have a laptop, you should bring it to class to do in-class examples, ask questions about homeworks, and to write any other code when necessary. If you do not have a laptop, I may have a couple old ones available for in-class use.

## Grading

Grading for the course is based on the following breakdown: 

- 10 homeworks (50%)
- Midterm Exam (10%)
- Final Project (40%)

Although I do not subscribe to the standard 90/80/70 rule in general, that scale has been pretty
accurate the last three semesters of my teaching this course.


Each **homework** is worth 6 points. Homework will be due more frequently in the early, foundational part of the course and will always be announced at least one week before its due date. All homework is due at the beginning of class on the due date via electronic submission. You are allowed to submit one homework up to 48 hours late for full credit; no late homework accepted thereafter unless a class-wide extension is given.  Homework is an individual effort, i.e., what you submit must be your own work. 

> *Please note*: The homework might be very hard, especially if your
  programming skills coming into the class are weak.  However, the tasks will not be
  impossible if you get an early start on them!
  
The **exam** is a short (roughly 30 minute) oral examination in which you will be tested on basic items covered in class. The format will be you and us (me + at least one other examiner) at a computer (yours or mine). You’ll be given some verbal questions along with one or more (very) short tasks to demonstrate what you know. Some of the questions will likely be about your project and homework solutions.

The **project** provides an opportunity for you to explore a topic of your choosing, which can be in support of your research. The catch is that it must be computational, and it must tie in all major elements covered in the course. Examples of past work and suggestions for new work will be provided. The project will be graded based on the following rubric (a more detailed rubric for the report will be given later):

- Proposal (10%): Up to one page description of what you would like to explore with suggestions of how you will do it. I’ve set a due date, but the earlier you submit it, the earlier you can get started.
- Draft Report (10%): 4 or 5 page report using the template provided. This should include a brief one page cover letter to the editor (i.e., me). This draft will be reviewed by at least three reviewers (including me). Although both technical and grammatical aspects will be assessed, note that this draft is only worth 10%, so just do your best to get a complete draft in place.
- Report Reviews (10%): You get to assess two or more draft reports of your peers and provide them feedback anonymously. This gives you the chance to see how peer review works in the real world. You also get the benefit of having at least two sets of comments beyond the ones I provide.
- Final Report (70%): The final draft should address the reviewer comments. You should also include a revised cover letter that specifies exactly how you addressed each point from the reviews. This draft should have perfect grammar, sound technical analysis, a proper bibliography, etc.

# Course Calendar

The following is a preliminary schedule of lectures.


| Lecture   |  Date            | Topics                                                                      |
|----|-------------------------|-----------------------------------------------------------------------------|
| 1  | Mon, Aug 26 | Administrivia. Installation/configuration of Linux Mint. |
| 2  | Wed, Aug 28 | Getting to know the open-source world. |
| 3  | Fri, Aug 30 | The Linux command line and the shell; Basic commands. |
|    | Mon, Sep 02 | HOLIDAY |
| 4  | Wed, Sep 04 | More on the command line. Environment variables, profiles, etc. |
| 5  | Fri, Sep 06 | Basic shell scripting (using bash). |
| 6  | Mon, Sep 09 | Version control with Git. |
| 7  | Wed, Sep 11 | GitHub for version control of collaborative projects. |
| 8  | Fri, Sep 13 | Python overview and installation. Built-in types and functions.  Python as a "graphing calculator." |
| 9  | Mon, Sep 16 | The structure of Python code: conditionals, loops, and functions.  The debugger. |
| 10 | Wed, Sep 18 | Modules, unit tests, and defensive programming. |
| 11 | Fri, Sep 20 | Floating-point numbers. Round-off errors and stability. |
| 12 | Mon, Sep 23 | Linear systems and NumPy arrays. |
| 13 | Wed, Sep 25 | Linear least-squares regression. |
| 14 | Fri, Sep 27 | SciPy applications: curve fitting, optimization, and IVPs. |
| 15 | Mon, Sep 30 | A survey of I/O formats (basic text, NumPy, JSON, HDF5, etc.) |
| 16 | Wed, Oct 02 | Regular expressions. |
| 17 | Fri, Oct 04 | Advanced Matplotlib (and other Python-based plotting) |
| 18 | Mon, Oct 07 | More on Matplotlib.  Publication-quality graphics. |
| 19 | Wed, Oct 09 | VisIt for visualization of large data sets. |
| 20 | Fri, Oct 11 | Overview of objected-oriented programming in Python. Classes, objects, and methods. |
| 21 | Mon, Oct 14 | More on OOP. Inheritance. |
| 22 | Wed, Oct 16 | More on OOP. |
| 23 | Fri, Oct 18 | Applications of OOP. |
| 24 | Mon, Oct 21 | Graphical-User Interfaces (GUIs) with PyQt5 |
| 25 | Wed, Oct 23 | More on GUIs |
| 26 | Fri, Oct 25 | More on GUIs |
| 27 | Mon, Oct 28 | A rapid introduction to C++ and modern Fortran. Syntax overview. Compilation. |
| 28 | Wed, Oct 30 | Introduction continued. |
| 29 | Fri, Nov 01 | More on C++. Pointers, arrays, etc. |
| 30 | Mon, Nov 04 | More on C++. Classes. |
| 31 | Wed, Nov 06 | More on Fortran. Arrays and modules. |
| 32 | Fri, Nov 08 | Using Python with Fortran: an overview of f2py. |
| 33 | Mon, Nov 11 | Using Python with C++: an overview of SWIG. |
| 34 | Wed, Nov 13 | Numerical linear algebra I: Vectors and matrices in C++ and Fortran. |
| 35 | Fri, Nov 15 | Finite difference method for boundary-value problems. |
| 36 | Mon, Nov 18 | Numerical linear algebra II: Solving sparse systems iteratively. |
| 37 | Wed, Nov 20 | OMILAT: Only masochists implement linear algebra themselves. Libraries. |
| 38 | Fri, Nov 22 | Overview of computer architectures and parallel computing. |
|    | Mon, Nov 25 | HOLIDAY |
|    | Wed, Nov 27 | HOLIDAY |
|    | Fri, Nov 29 | HOLIDAY |
| 39 | Mon, Dec 02 | Introduction to multithreaded parallelism via OpenMP. |
| 40 | Wed, Dec 04 | OpenMP continued. |
| 41 | Fri, Dec 06 | OpenMP continued. |
| 42 | Mon, Dec 09 | Introduction to parallel compution on heterogeneous systems with MPI. |
| 43 | Wed, Dec 11 | MPI continued. |
| 44 | Fri, Dec 13 | MPI continued.  Course wrapup. |
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      


## Academic Honesty

Kansas State University has an Honor System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one’s work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor System. The policies and procedures of the Honor System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. The honor system website can be reached via the following URL: www.ksu.edu/honor. A component vital to the Honor System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: “On my honor, as a student, I have neither given nor received unauthorized aid on this academic work.” A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.

## Students with Disabilities

Students with disabilities who need classroom accommodations, access to technology, or in- formation about emergency building/campus evacuation processes should contact the Student Access Center and/or their instructor. Services are available to students with a wide range of disabilities including, but not limited to, physical disabilities, medical conditions, learning disabilities, attention deficit disorder, depression, and anxiety. If you are a student enrolled in campus/online courses through the Manhattan or Olathe campuses, contact the Student Ac- cess Center at accesscenter@k-state.edu, 785-532-6441; for Salina campus, contact the Academic and Career Advising Center at acac@k-state.edu, 785-826-2649.

## Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article VI, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.
