# ME 701 - Development of Computer Applications in Mechanical Engineering

This document provides the syllabus and course policies.
Please read it carefully.

The rest of this repository contains notes, examples, and other resources
for ME 701 - Development of Computer Applications in Mechanical Engineering,
taught at Kansas State University.  All materials were developed by
Jeremy Roberts.

## Course Details

### Time and Place

11:30am--12:20pm M via Zoom (meeting ID: 617-763-8618, which is also my cell number)

11:30am--12:20pm WF in DUE 0097 for in-person recitations (half and half; optional, and will be recorded if possible)

### Instructor
 - Jeremy Roberts
 - 137D Ward Hall
 - Office Hours by appointment; see my [calendar](https://calendar.google.com/calendar/embed?src=j.alyn.roberts%40gmail.com&ctz=America/Chicago) and shoot me an email.

### Teaching Assistant
 - Rabab Elzohery
 - 133B Ward Hall
 - Office Hours TBD

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

Because of the material covered in ME 701, the lectures need to be rather hands-on, informal tutorials (although the interactive part will be during recitations). If you have a laptop, you should bring it to do examples, ask questions about homeworks, and to write any other code when necessary. If you do not have a laptop, I may have a couple old ones available for in-class use.  Either way, have a computer when going through the videos!

## Grading

Grading for the course is based on the following breakdown:

- 11 homeworks [one free drop drop] (50%)
- Two programming projects (40%)
- Participation (10%)


Although I do not subscribe to the standard 90/80/70 rule in general, that scale has been pretty
accurate the last three semesters of my teaching this course.


Each **homework** is equally weighted. Homework will be due more frequently in the early, foundational part of the course and will always be announced at least one week before its due date and time. You may drop the lowest homework score.  No homework received after grading has begun will be accepted.  Your best (and guaranteed) bet is to submit by the deadline.  Homework will be primarily an individual effort, but some assignments will require pairs of students.

The **programming projects** provide an opportunity for you to sythesize the tools learned throughout the course.  The first one emphasizes Python, while the second one will emphasize C++.  These projects are more in depth and more open-ended than a typical homework problem.  More details will be announced later on (but not too much later.)


> *Please note*: The programming required for both homework and projects might be very hard, especially if your
  programming skills coming into the class are weak.  However, the tasks will not be
  impossible if you get an early start on them!

In a small, hands-on course like this, **participation** in "lectures" is essential. That said, COVID-19 has messed things up a bit.  In our present context, active participation means doing any assigned reading (or other preparation) and coming to recitation ready to engage with the material. Regularly be present, take notes (before, during, and after lecture), ask questions, and follow up, as needed, during office hours.  This part of the assessment is going to be a [metacognitive](https://en.wikipedia.org/wiki/Metacognition) exercise for *you*, the student.  For each "lecture", you will summarize (briefly) how you prepared for lecture, what you contributed to lecture, and which topic is least clear.  These entries should not be single sentences; rather, truly spend a few minutes to reflect on what you've done to learn.  Eventually, you will "commit" these entries to an online repository where the TA and I can review them periodically for feedback on the course.  By the end of the semester, you will have a pretty clear view of your learning throughout the course (and I will, too).

Here is an example entry for a single lesson:

```
# Lesson 1

## Preparation

To prepare for this lesson, I logged into Canvas to see the first announcement
and email.  I checked the syllabus and saw the basic rules (and noted some things
still needed to be updated).

## Contribution

I showed up to the Zoom meeting and introduced myself.  I asked about the
projects because little was said in the syllabus about them.  We learned
that more information would be given out later.

## Muddy Water

It's just the beginning, so not much is particularly unclear yet.  I'm just
not sure how prepared I am for the course since my goal is to learn how to be
a better programmer, but this course seems like a lot of tough programming.

```


## Course Calendar

The following is a preliminary schedule of lectures.  Some topics are subject to change.


| Lecture   |  Date            | Topics                                                                      |
|----|-------------------------|-----------------------------------------------------------------------------|
|	1	  |	M, Aug 17 |	Administrivia. Installation/configuration of Linux Mint.	|
|	2	  |	W, Aug 19 |	Getting to know the open-source world.	|
|	3	  |	F, Aug 21	|	The Linux command line and the shell; Basic commands.	|
|	4	  |	M, Aug 24	|	More on the command line. Environment variables, profiles, etc.	|
|	5	  |	W, Aug 26	|	Basic shell scripting (using bash).	|
|	6	  |	F, Aug 28	|	Version control with Git.	|
|	7	  |	M, Aug 31	|	GitHub for version control of collaborative projects.	|
|	8	  |	W, Sep 02	|	More version control.	|
|	9	  |	F, Sep 04	|	More version control.  Brief introduction to Python.	|
|	10	|	M, Sep 07	|	Python built-in types and functions.  Python as a "graphing calculator."	|
|	11	|	W, Sep 09	|	The structure of Python code: conditionals, loops, and functions.  The debugger.	|
|	12	|	F, Sep 11	|	Modules. Unit testing.	|
|	13	|	M, Sep 14	|	Sources of numerical error.  Roundoff error.  Truncation error.	|
|	14	|	W, Sep 16	|	Linear systems and NumPy arrays.  Least squares.	|
|	xx	|	F, Sep 18	|	...catching up...	|
|	15	|	M, Sep 21	|	SciPy, sparse systems, and iterative solutions.	|
|	16	|	W, Sep 23	|	Selected SciPy applications (or continuation).	|
|	18	|	F, Sep 25	|	...catching up...and project discussions... |
|	19	|	Mon, Sep 28	|	Overview of objected-oriented programming in Python. Classes, objects, and methods.	|
|	20	|	Wed, Sep 30	|	More on OOP. Inheritance.	|
|	21	|	Fri, Oct 02	|	Applications of OOP.	|
|	22	|	Mon, Oct 05	|	Graphical-User Interfaces (GUIs) with PyQt5		|
|	23	|	Wed, Oct 07	|	More on GUIs	|
|	24	|	Fri, Oct 09	|	A survey of I/O formats (basic text, NumPy, JSON, HDF5, etc.)	|
|	25	|	Mon, Oct 12	|	Regular expressions.	|
|	26	|	Wed, Oct 14	|	Advanced Matplotlib (and other Python-based plotting)	|
|	27	|	Fri, Oct 16	|	More on Matplotlib.  Publication-quality graphics.	|
|	28	|	Mon, Oct 19	|	VisIt for visualization of large data sets. 	|
|	29	|	Wed, Oct 21	|	A rapid introduction to C++. Syntax overview (types, selection, and iteration).  The compiler.	|
|	30	|	Fri, Oct 23	|	Eclipse IDE and graphical debugging.	|
|	31	|	Mon, Oct 26	|	Functions, organizing code, and the Makefile.	|
|	32	|	Wed, Oct 28	|	Pointers, arrays, and memory management.  Valgrind.	|
|	33	|	Fri, Oct 30	|	Classes.  	|
|	34	|	Mon, Nov 02	|	More on Classes.	|
|	35	|	Wed, Nov 04	|	Templates and the standard template library (STL): vectors, maps, and more.	|
|	36	|	Fri, Nov 06	|	Using Python with C++: an overview of SWIG.	|
|	37	|	Mon, Nov 09	|	Using libraries: BLAS, LAPACK, GNU scientific library and more. 	|
|	38	|	Wed, Nov 11	|	Overview of computer architectures and parallel computing.  Navigating Beocat.	|
|	39	|	Fri, Nov 13	|	Code profiling and tuning.	|
|	40	|	Mon, Nov 16	|	Computational performance and OMILAT.	|
|	41	|	Wed, Nov 18	|	Parallel computing: OpenMP and MPI.	|
|	42	|	Fri, Nov 20	|	Parallel computing: OpenMP and MPI.	|
|	43	|	Mon, Nov 30	|	Parallel computing: OpenMP and MPI.	|
|	44	|	Wed, Dec 02	|	Parallel computing: OpenMP and MPI.	|
|	45	|	Fri, Dec 04	|	Wrap-Up / Make-Up	|


## Academic Honesty

Kansas State University has an Honor and Integrity System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor and Integrity System. The policies and procedures of the Honor and Integrity System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. A component vital to the Honor and Integrity System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: "On my honor, as a student, I have neither given nor received unauthorized aid on this academic work." A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.

> *Please note*: Unlike an introductory course like ME 400 where canned solutions abound, I totally encourage your use of resources on the web and beyond.  Where you apply bits of code, make sure to reference the source in a comment, etc.  Posting questions to Chegg, etc., would not be okay because I might have a solver's account and will take your money and give you the wrong answer.  Actually, that would be sort of funny, but my inner compass says no.  Save time and money--see me in recitation and office hours!

## Students with Disabilities

Students with disabilities who need classroom accommodations, access to technology, or information about emergency building/campus evacuation processes should contact the Student Access Center and/or their instructor.  Services are available to students with a wide range of disabilities including, but not limited to, physical disabilities, medical conditions, learning disabilities, attention deficit disorder, depression, and anxiety. If you are a student enrolled in campus/online courses through the Manhattan or Olathe campuses, contact the Student Access Center at accesscenter@k-state.edu, 785-532-6441; for K-State Polytechnic campus, contact Julie Rowe, Diversity, Inclusion and Access Coordinator, at jarowe@ksu.edu or call 785-826-2971.

## Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article V, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.

## Wearing of Face Coverings

To protect the health and safety of the K-State community, students, faculty, staff and visitors must wear face coverings over their mouths and noses while on K-State campuses in all hallways, public spaces, classrooms and other common areas of campus buildings, and when in offices or other work spaces or outdoor settings when 6-feet social distancing cannot be maintained. In addition, all students, faculty, and staff are required to take the COVID-19 and Face Mask Safety training. Employees who need reasonable accommodations and assistance related to required face coverings may contact the ADA coordinator at charlott@k-state.edu, and students needing accommodations may contact the Student Access Center at accesscenter@k-state.edu.

In classrooms, faculty have the right to deny a student entry into the room if the student is not wearing a face covering. Students not wearing a face covering will be reminded to do so and offered a clean face covering, if one is available. If the student does not comply, the faculty member will ask the student to leave the space, and if available, join the class remotely.  As a last resort, campus police will be called. The faculty members will complete the Code of Conduct form and the Office of Student Life will look further into the issue and take the non-compliance with the request to leave into consideration of further accountability measures.

At no point should the professor or other students put themselves into an unsafe situation while attempting to enforce the face-covering policy. Manhattan campus police: 785-532-6412
