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
 - Zoom meeting ID: 617 763 8618 (which is also my cell number)
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
# M 08/23

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
|	1	|	M 08/23	|	Administrivia. Configuring a Linux environment.  WSL, etc.	|
|	2	|	W 08/25	|	Getting to know the open-source world.	|
|	3	|	F 08/27	|	The Linux command line and the shell; Basic commands.	|
|	4	|	M 08/30	|	More on the command line. Environment variables, profiles, etc.	|
|	5	|	W 09/01	|	Basic shell scripting (using bash).	|
|	6*	|	F 09/03	|	Version control with Git. 	|
|	 	|	M 09/06	|	HOLIDAY	|
|	7	|	W 09/08	|	GitHub for version control of collaborative projects.	|
|	8	|	F 09/10	|	More version control.	|
|	9	|	M 09/13	|	Introduction to Python. Built-in types and functions.	|
|	10	|	W 09/15	|	Python as a "graphing calculator."	|
|	11*	|	F 09/17	|	The structure of Python code: conditionals, loops, and functions.  The debugger.	|
|	12	|	M 09/20	|	Modules and code organization.	|
|	13	|	W 09/22	|	Unit testing. Test-driven development.  	|
|	14	|	F 09/24	|	Exception handling?	|
|	15	|	M 09/27	|	Sources of numerical error.  Roundoff error.  Truncation error.	|
|	16	|	W 09/29	|	Linear systems and NumPy arrays.  Least squares.	|
|	17	|	F 10/01	|	SciPy, sparse systems, and iterative solutions.	|
|	18	|	M 10/04	|	Other Python packages for technical computing (e.g., FENICs)	|
|	19	|	W 10/06	|	Advanced Matplotlib	|
|	20	|	F 10/08	|	Overview of objected-oriented programming in Python. Classes, objects, and methods.	|
|	21	|	M 10/11	|	More on OOP. Methods.	|
|	22	|	W 10/13	|	More on OOP. Inheritance.	|
|	23*	|	F 10/15	|	OO design.	|
|	24	|	M 10/18	|	Python GUIs with PyQt5	|
|	25	|	W 10/20	|	Exploring QWidgets	|
|	26	|	F 10/22	|	UI via Slots and Signals	|
|	27	|	M 10/25	|	Widget layouts	|
|	28	|	W 10/27	|	The QMainWindow class	|
|	29	|	F 10/29	|	Qt Designer for WYSIWYG layouts	|
|	30	|	M 11/01	|	Qt Rich Text	|
|	31	|	W 11/03	|	2-D graphics	|
|	32	|	F 11/05	|	2-D cont.	|
|	33	|	M 11/08	|	2-D cont.	|
|	34	|	W 11/10	|	2-D cont.	|
|	35	|	F 11/12	|	3-D graphics	|
|	36	|	M 11/15	|	3-D graphics	|
|	37	|	W 11/17	|	3-D graphics	|
|	38*	|	F 11/19	|	Reserved	|
|	   	|	M 11/22	|	HOLIDAY	|
|	   	|	W 11/24	|	HOLIDAY	|
|	  	|	F 11/26	|	HOLIDAY	|
|	39	|	M 11/29	|	Embedded Linux with Raspberry Pi	|
|	40	|	W 12/01	|	Using the GPIOs 	|
|	41	|	F 12/03	|	PyQt on the Pi	|
|	42	|	M 12/06	|	Reserved	|
|	43	|	W 12/08	|	Reserved	|
|	44	|	F 12/10	|	Reserved	|

## Academic Honesty

Kansas State University has an Honor and Integrity System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor and Integrity System. The policies and procedures of the Honor and Integrity System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. A component vital to the Honor and Integrity System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: "On my honor, as a student, I have neither given nor received unauthorized aid on this academic work." A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.

> *Please note*: Unlike an introductory course like ME 400 where canned solutions abound, I totally encourage your use of resources on the web and beyond.  Where you apply bits of code, make sure to reference the source in a comment, etc.  Posting questions to Chegg, etc., would not be okay because I might have a solver's account and will take your money and give you the wrong answer.  Actually, that would be sort of funny, but my inner compass says no.  Save time and money--see me in lecture and office hours!

## Students with Disabilities

Students with disabilities who need classroom accommodations, access to technology, or information about emergency building/campus evacuation processes should contact the Student Access Center and/or their instructor.  Services are available to students with a wide range of disabilities including, but not limited to, physical disabilities, medical conditions, learning disabilities, attention deficit disorder, depression, and anxiety. If you are a student enrolled in campus/online courses through the Manhattan or Olathe campuses, contact the Student Access Center at accesscenter@k-state.edu, 785-532-6441; for K-State Polytechnic campus, contact Julie Rowe, Diversity, Inclusion and Access Coordinator, at jarowe@ksu.edu or call 785-826-2971.

## Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article V, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.

## Wearing of Face Coverings

To protect the health and safety of the K-State community, students, faculty, staff and visitors must wear face coverings over their mouths and noses while on K-State campuses in all hallways, public spaces, classrooms and other common areas of campus buildings, and when in offices or other work spaces or outdoor settings when 6-feet social distancing cannot be maintained. In addition, all students, faculty, and staff are required to take the COVID-19 and Face Mask Safety training. Employees who need reasonable accommodations and assistance related to required face coverings may contact the ADA coordinator at charlott@k-state.edu, and students needing accommodations may contact the Student Access Center at accesscenter@k-state.edu.

In classrooms, faculty have the right to deny a student entry into the room if the student is not wearing a face covering. Students not wearing a face covering will be reminded to do so and offered a clean face covering, if one is available. If the student does not comply, the faculty member will ask the student to leave the space, and if available, join the class remotely.  As a last resort, campus police will be called. The faculty members will complete the Code of Conduct form and the Office of Student Life will look further into the issue and take the non-compliance with the request to leave into consideration of further accountability measures.

At no point should the professor or other students put themselves into an unsafe situation while attempting to enforce the face-covering policy. Manhattan campus police: 785-532-6412
