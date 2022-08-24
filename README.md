# ME 701 - Development of Computer Applications in Mechanical Engineering

This document provides the syllabus and course policies.
Please read it carefully.

The rest of this repository contains notes, examples, and other resources
for ME 701 - Development of Computer Applications in Mechanical Engineering,
taught at Kansas State University.  All materials were developed by
Jeremy Roberts.

## Course Details

### Time and Place

11:30am--12:20pm MWF DUE 0097
 
### Instructor
 - Jeremy Roberts
 - 137D Ward Hall
 - Office Hours by appointment; see my [calendar](https://calendar.google.com/calendar/embed?src=j.alyn.roberts%40gmail.com&ctz=America/Chicago) and shoot me an email.  


## Course Description 

From the catalog: Nature of design, graphical user interface development to support computer-aided design, algorithms and computer graphics in computer applications, feature-based design, applications to design problems.

## Student Outcomes

Students should, at a minimum, 
   (1) do basic technical work in a Linux or Linux-like environment machines
   (2) produce graphical and non-graphical programs at level needed for solving problems typical of engineering
   (3) select the appropriate language or tool for the job

## Textbook

There is no perfect book for this course, and most reference material can easily be found online. In some cases, electronic materials (book excerpt, article, etc.) will be provided to the student.  The following are relevant sources in roughly the order in which they map onto the course content.


- A. Scopatz and K. Huff. Effective Computation in Physics. O’Reilly Media, (2015). ISBN: 978-1491901533

- W. Shotts, Jr. *The Linux Command Line: A Complete Introduction*, No Starch Press (2012).
  ISBN: 978-1-59327-389-7. Available free from [http://linuxcommand.org/tlcl.php](http://linuxcommand.org/tlcl.php)

- J. Roberts. *Python for Engineers* (2016).
  [http://robertsj.github.io/me400_notes/index.html](http://robertsj.github.io/me400_notes/index.html)

- A. Moore, *Mastering GUI Programming with Python*,Packt Publishing, (2019).   ASIN: B07S9WFD92. 
  Online resources available at [https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python](https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python)

- D. Mallow, *Exploring Raspberry Pi: Interfacing to the Real World with Embedded Linux*, (2016). ISBN-10: 1119188687 


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


Each **homework** is equally weighted. Homework will be due more frequently in the early, foundational part of the course and will always be announced at least one week before its due date and time. You may drop the lowest homework score.  Homework received after grading has begun may not be accepted.  Your best (and guaranteed) bet is to submit by the deadline.  Homework will be primarily an individual effort, but some assignments will require pairs of students.

The **programming projects** provide an opportunity for you to sythesize the tools learned throughout the course.  The first project emphasizes use of version control and Python for solving a technical problem. The second project emphasizes the development of a graphical program based on PyQt to aid in the analysis of an engineering (or other technical) problem.  These projects are more in depth and more open-ended than a typical homework problem.   


In a small, hands-on course like this, **participation** in "lectures" is essential.  In our present context, active participation means doing any assigned reading (or other preparation) and coming to lecture ready to engage with the material. Regularly be present, take notes (before, during, and after lecture), ask questions, and follow up, as needed, during office hours.  This part of the assessment is going to be a [metacognitive](https://en.wikipedia.org/wiki/Metacognition) exercise for *you*, the student.  For each "lecture", you will summarize (briefly) how you prepared for lecture, what you contributed to lecture, and which topic is least clear.  These entries should not be single sentences; rather, truly spend a few minutes to reflect on what you've done to learn.  Eventually, you will "commit" these entries to an online repository where I can review them periodically for feedback on the course.  By the end of the semester, you will have a pretty clear view of your learning throughout the course (and I will, too).

Here is an example entry for a single lesson:

```
# M 08/22

## Preparation

To prepare for this lesson, I logged into Canvas to see the first announcement
and email.  I checked the syllabus and saw the basic rules (and noted some things
still needed to be updated).

## Contribution

I showed up to lecture and introduced myself.  I asked about the
projects because little was said in the syllabus about them.  We learned
that more information would be given out later.

## Muddy Water

It's just the beginning, so not much is particularly unclear yet.  I'm just
not sure how prepared I am for the course since my goal is to learn how to be
a better programmer, but this course seems like a lot of tough programming.

```


## Course Calendar

The following is a preliminary schedule of lectures.  Some topics, especially those after Lecture 24, are subject to change.
Dates with asterisks are likely dates where a virtual lecture (or asynchronous instruction) will be required.


| Lecture   |  Date            | Topics                                                                      |
|----|-------------------------|-----------------------------------------------------------------------------|
|	1	|	M 08/22	|	Administrivia. Configuring a Linux environment.  WSL, etc.	|
|	2	|	W 08/24	|	Getting to know the open-source world.	|
|	3	|	F 08/26	|	The Linux command line and the shell; Basic commands.	|
|	4	|	M 08/29	|	More on the command line. Environment variables, profiles, etc.	|
|	5	|	W 08/31	|	Basic shell scripting (using bash).	|
|	6	|	F 09/02	|	Version control with Git. 	|
|		|	M 09/05	|	HOLIDAY	|
|	7	|	W 09/07	|	GitHub for version control of collaborative projects.	|
|	8	|	F 09/09	|	More version control.	|
|	9	|	M 09/12	|	Introduction to Python. Built-in types and functions.	|
|	10	|	W 09/14	|	Python as a "graphing calculator."	|
|	11	|	F 09/16	|	The structure of Python code: conditionals, loops, and functions.  The debugger.	|
|	12	|	M 09/19	|	Modules and code organization.	|
|	13	|	W 09/21	|	Unit testing. Test-driven development.  	|
|	14	|	F 09/23	|	Exception handling?	|
|	15	|	M 09/26	|	Sources of numerical error.  Roundoff error.  Truncation error.	|
|	16	|	W 09/28	|	Linear systems and NumPy arrays.  Least squares.	|
|	17	|	F 09/30	|	SciPy, sparse systems, and iterative solutions.	|
|	18	|	M 10/03	|	Other Python packages for technical computing (e.g., FENICs)	|
|	19	|	W 10/05	|	Advanced Matplotlib	|
|	20	|	F 10/07	|	Overview of objected-oriented programming in Python. Classes, objects, and methods.	|
|	21	|	M 10/10	|	More on OOP. Inheritance.	|
|	22	|	W 10/12	|	More on OOP.	|
|	23	|	F 10/14	|	OO Design	|
|	24	|	M 10/17	|	Python GUIs with PyQt5	|
|	25	|	W 10/19	|	UI via Slots and Signals 	|
|	26	|	F 10/21	|	Exploring QWidgets	|
|	27	|	M 10/24	|	Widget layouts	|
|	28	|	W 10/26	|	The QMainWindow class	|
|	29	|	F 10/28	|	Qt Designer for WYSIWYG layouts	|
|		|	M 10/31	|	Rest Day / Roberts Travel	|
|	30	|	W 11/02	|	Styles and Formatting	|
|		|	F 11/04	|	Project 1 Development Session	|
|	31	|	M 11/07	|	Embedded Plots	|
|	32	|	W 11/09	|	Basic Bitmaps	|
|	33	|	F 11/11	|	Custom Widgets (Plot Digitizer)	|
|	34	|	M 11/14	|	3-D graphics	|
|	35	|	W 11/16	|	3-D graphics	|
|	36	|	F 11/18	|	3-D graphics	|
|		|	M 11/21	|	HOLIDAY	|
|		|	W 11/23	|	HOLIDAY	|
|		|	F 11/25	|	HOLIDAY	|
|	37	|	M 11/28	|	Embedded Linux with Raspberry Pi	|
|	38	|	W 11/30	|	Using the GPIOs 	|
|	39	|	F 12/02	|	PyQt on the Pi	|
|	40	|	M 12/05	|	Reserved	|
|	41	|	W 12/07	|	Reserved	|
|		|	F 12/09	|	Wrap-up and Project 2 Development Session	|

## Academic Honesty

Kansas State University has an Honor and Integrity System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor and Integrity System. The policies and procedures of the Honor and Integrity System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. A component vital to the Honor and Integrity System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: "On my honor, as a student, I have neither given nor received unauthorized aid on this academic work." A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.

> *Please note*: Unlike an introductory course like ME 400 where canned solutions abound, I totally encourage your use of resources on the web and beyond.  Where you apply bits of code, make sure to reference the source in a comment, etc.  Posting questions to Chegg, etc., would not be okay because I might have a solver's account and will take your money and give you the wrong answer.  Actually, that would be sort of funny, but my inner compass says no.  Save time and money--see me in lecture and office hours!

## Students with Disabilities

Students with disabilities who need classroom accommodations, access to technology, or information about emergency building/campus evacuation processes should contact the Student Access Center and/or their instructor.  Services are available to students with a wide range of disabilities including, but not limited to, physical disabilities, medical conditions, learning disabilities, attention deficit disorder, depression, and anxiety. If you are a student enrolled in campus/online courses through the Manhattan or Olathe campuses, contact the Student Access Center at accesscenter@k-state.edu, 785-532-6441; for K-State Polytechnic campus, contact Julie Rowe, Diversity, Inclusion and Access Coordinator, at jarowe@ksu.edu or call 785-826-2971.

## Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article V, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.
 