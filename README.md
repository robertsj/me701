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
 - Office Hours: MW 2:30-4pm


## Course Description 

This course will provide students with the skills needed to apply computation successfully in their research and professional endeavors. This begs the question, “what is computation?” In this course, all we want to do is make the computer do what we want it to do. Our approach doesn’t always have to be the fastest or most elegant—though both are admirable qualities— but it must get the right answer.

Along the way, students will learn (or review) basic numerical methods and use them to solve problems typical in mechanical and nuclear engineering. Students will also be exposed to a variety of special topics, including graphical user interfaces, visualization tools, and parallel computing.

## Student Outcomes

Students should, at a minimum, 
   (1) do basic technical work in a Linux or Linux-like environment machines
   (2) produce graphical and non-graphical programs at level needed for solving problems typical of engineering
   (3) select the appropriate language or tool for the job

## Textbook

There is no perfect book for this course, and most reference material can easily be found online. In some cases, electronic materials (book excerpt, article, etc.) will be provided to the student.  The following are relevant sources in roughly the order in which they map onto the course content.


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

Because of the material covered in ME 701, the lectures need to be rather hands-on, informal tutorials. If you have a laptop, you should bring it to do examples, ask questions about homeworks, and to write any other code when necessary. If you do not have a laptop, I may have a couple old ones available for in-class use!

## Grading

Grading for the course is based on the following breakdown: 

- Approximately 10 homeworks (50%)
- Midterm Exam (10%)
- Final Project (40%)

By default, we'll use the 90/80/70 scale for A/B/C.  Boundaries will never be increased.

Homework will be due more frequently in the early, foundational part of the course and will always be announced at least one week before its due date. All homework is due at the beginning of class on the due date via electronic submission. You are allowed to submit one homework up to 48 hours late for full credit; no late homework accepted thereafter unless a class-wide extension is given.  Homework is an individual effort, i.e., what you submit must be your own work. 

> *Please note*: The homework might be very hard, especially if your
  programming skills coming into the class are weak.  However, the tasks will not be
  impossible if you get an early start on them!
  
The **exam** is a short (roughly 30 minute) oral examination in which you will be tested on basic items covered in class. The format will be you and us (me + at least one other examiner) at a computer (yours or mine). You’ll be given some verbal questions along with one or more (very) short tasks to demonstrate what you know. Some of the questions will likely be about your project and homework solutions.

The **project** provides an opportunity for you to explore a topic of your choosing, which can be in support of your research. The catch is that it must be computational, and it must tie in all major elements covered in the course. Examples of past work and suggestions for new work will be provided. The project will be graded based on the following rubric (a more detailed rubric for the report will be given later):

- Proposal (10%): Up to one page description of what you would like to explore with suggestions of how you will do it. I’ve set a due date, but the earlier you submit it, the earlier you can get started.
- Draft Report (10%): 4 or 5 page report using the template provided. This should include a brief one page cover letter to the editor (i.e., me). This draft will be reviewed by at least three reviewers (including me). Although both technical and grammatical aspects will be assessed, note that this draft is only worth 10%, so just do your best to get a complete draft in place.
- Report Reviews (10%): You get to assess two or more draft reports of your peers and provide them feedback anonymously. This gives you the chance to see how peer review works in the real world. You also get the benefit of having at least two sets of comments beyond the ones I provide.
- Final Report (70%): The final draft should address the reviewer comments. You should also include a revised cover letter that specifies exactly how you addressed each point from the reviews. This draft should have perfect grammar, sound technical analysis, a proper bibliography, etc.


## Course Calendar

The following is a preliminary schedule of lectures.  All topics, especially those after Lecture 22, are subject to change.
 


| Lec | Date         | Topic                                                                 |
|-----|--------------|-----------------------------------------------------------------------|
| 1   | Mon, Aug 25  | Administrivia. Setting up a Linux environment. WSL, Beocat, etc.      |
| 2   | Wed, Aug 27  | Getting to know the open-source world.                                |
| 3   | Fri, Aug 29  | The Linux command line and the shell. Basic commands.                 |
|     | Mon, Sep 1   | HOLIDAY (Labor Day)                                                   |
| 4   | Wed, Sep 3   | More on the command line. Environment variables, profiles, etc.       |
| 5   | Fri, Sep 5   | Basic shell scripting (using bash).                                   |
| 6   | Mon, Sep 8   | Version control with Git.                                             |
| 7   | Wed, Sep 10  | GitHub for version control of collaborative projects.                 |
| 8   | Fri, Sep 12  | Python overview and installation. Built-in types and functions.       |
| 9   | Mon, Sep 15  | Structure of Python code: conditionals, loops, functions.             |
| 10  | Wed, Sep 17  | NumPy arrays. Matplotlib for plotting.                                |
| 11  | Fri, Sep 19  | Floating-point numbers. Round-off errors and stability.               |
| 12  | Mon, Sep 22  | Data input/output: prompts, command line, and files.                  |
| 13  | Wed, Sep 24  | Regular expressions.                                                  |
| 14  | Fri, Sep 26  | Pickling and NumPy for saving data. Matrix operations with NumPy.     |
| 15  | Mon, Sep 29  | Linear least-squares regression.                                      |
| 16  | Wed, Oct 1   | SciPy for optimization and differential equations.                    |
| 17  | Fri, Oct 3   | Modules. Defensive programming. Debugging. Unit tests.                |
| 18  | Mon, Oct 6   | Overview of object-oriented programming. Classes, objects, methods.   |
| 19  | Wed, Oct 8   | More on OOP. Inheritance.                                             |
| 20  | Fri, Oct 10  | More on OOP.                                                          |
| 21  | Mon, Oct 13  | Publication-quality plots with Matplotlib.                            |
| 22  | Wed, Oct 15  | Advanced Matplotlib (and other Python-based plotting).                |
|     | Fri, Oct 17  | WILDCAT PAUSE (no class)                                              |
| 23  | Mon, Oct 20  | Visualization tools: VisIt and ParaView.                              |
| 24  | Wed, Oct 22  | Data formats: text, JSON, CSV.                                        |
| 25  | Fri, Oct 24  | Data formats: binary, HDF5, VTK.                                      |
| 26  | Mon, Oct 27  | Introduction to C++/modern Fortran. Syntax overview. Compilation.     |
|     | Wed, Oct 29  | Work Day (or make-up)                                                 |
| 27  | Fri, Oct 31  | Continued introduction to compiled languages.                         |
| 28  | Mon, Nov 3   | More on C++. Arrays and classes. Makefiles.                           |
| 29  | Wed, Nov 5   | More on Fortran. Arrays. Modules and derived types.                   |
| 30  | Fri, Nov 7   | Using Python with C++ and Fortran. Overview of SWIG and f2py.         |
| 31  | Mon, Nov 10  | Numerical linear algebra I: Vectors and matrices in C++ and Fortran.  |
| 32  | Wed, Nov 12  | Finite difference method for boundary-value problems.                 |
| 33  | Fri, Nov 14  | Numerical linear algebra II: Solving sparse systems iteratively.      |
| 34  | Mon, Nov 17  | OMILAT: Libraries vs hand-coded linear algebra.                       |
| 35  | Wed, Nov 19  | Overview of computer architectures and parallel computing.            |
|     | Nov 24–28    | HOLIDAY (Thanksgiving Break)                                          |
| 36  | Mon, Dec 1   | Introduction to multithreaded parallelism via OpenMP.                 |
| 37  | Wed, Dec 3   | OpenMP continued.                                                     |
| 38  | Fri, Dec 5   | Parallel computing on heterogeneous systems with MPI.                 |
| 39  | Mon, Dec 8   | MPI continued.                                                        |
| 40  | Wed, Dec 10  | Course wrap-up.                                                       |
|     | Fri, Dec 12  | Work Day (or make-up)                                                 |


## Mandatory Statements


### 1. Statement Regarding Academic Honesty

Kansas State University has an Honor and Integrity System based on personal integrity, which is presumed to be sufficient assurance that, in academic matters, one's work is performed honestly and without unauthorized assistance. Undergraduate and graduate students, by registration, acknowledge the jurisdiction of the Honor and Integrity System. The policies and procedures of the Honor and Integrity System apply to all full and part-time students enrolled in undergraduate and graduate courses on-campus, off-campus, and via distance learning. A component vital to the Honor and Integrity System is the inclusion of the Honor Pledge which applies to all assignments, examinations, or other course work undertaken by students. The Honor Pledge is implied, whether or not it is stated: "On my honor, as a student, I have neither given nor received unauthorized aid on this academic work." A grade of XF can result from a breach of academic honesty. The F indicates failure in the course; the X indicates the reason is an Honor Pledge violation.


### 2. Statement Regarding Students with Disabilities

At K-State it is important that every student has access to course content and the means to demonstrate course mastery. Students with disabilities may benefit from services including accommodations provided by the Student Access Center. Disabilities can include physical, learning, executive functions, and mental health. You may register at the Student Access Center or to learn more contact:  

```
Manhattan/Olathe/Global Campus – Student Access Center  
accesscenter@k-state.edu
785-532-6441    

K-State Salina Campus – Julie Rowe; Student Success Coordinator
jarowe@k-state.edu
785-820-7908    
```

Students already registered with the Student Access Center please request your Letters of Accommodation early in the semester to provide adequate time to arrange your approved academic accommodations. Once SAC approves your Letter of Accommodation it will be e-mailed to you, and your instructor(s) for this course.  Please follow up with your instructor to discuss how best to implement the approved accommodations. 

### 3. Statement Defining Expectations for Classroom Conduct

All student activities in the University, including this course, are governed by the Student Judicial Conduct Code as outlined in the Student Governing Association By Laws, Article V, Section 3, number 2. Students who engage in behavior that disrupts the learning environment may be asked to leave the class.

### 4. Statement on Mutual Respect and Inclusion in K-State Teaching and Learning Spaces

At K-State, faculty and staff are committed to creating and maintaining an inclusive and supportive learning environment for students from diverse backgrounds and perspectives. K-State courses, labs, and other virtual and physical learning spaces promote equitable opportunity to learn, participate, contribute, and succeed, regardless of age, race, color, ethnicity, nationality, genetic information, ancestry, disability, socioeconomic status, military or veteran status, immigration status, Indigenous identity, gender identity, gender expression, sexuality, religion, culture, as well as other social identities.

Faculty and staff are committed to promoting equity and believe the success of an inclusive learning environment relies on the participation, support, and understanding of all students. Students are encouraged to share their views and lived experiences as they relate to the course or their course experience, while recognizing they are doing so in a learning environment in which all are expected to engage with respect to honor the rights, safety, and dignity of others in keeping with the K-State Principles of Community. 

If you feel uncomfortable because of comments or behavior encountered in this class, you may bring it to the attention of your instructor, advisors, and/or mentors. If you have questions about how to proceed with a confidential process to resolve concerns, please contact the Student Ombudsperson Office. Violations of the student code of conduct can be reported using the Code of Conduct Reporting Form. You can also report discrimination, harassment or sexual harassment, if needed.

### 5. Statement Regarding Discrimination, Harassment, and Sexual Harassment

Kansas State University is committed to maintaining academic, housing, and work environments that are free of discrimination, harassment, and sexual harassment. Instructors support the University’s commitment by creating a safe learning environment during this course, free of conduct that would interfere with your academic opportunities. Instructors also have a duty to report any behavior they become aware of that potentially violates the University’s policy prohibiting discrimination, harassment, and sexual harassment, as outlined by PPM 3010.  

If a student is subjected to discrimination, harassment, or sexual harassment, they are encouraged to make a non-confidential report to the University’s Office for Institutional Equity (OIE) using the online reporting form. Incident disclosure is not required to receive resources at K-State. Reports that include domestic and dating violence, sexual assault, or stalking, should be considered for reporting by the complainant to the Kansas State University Police Department or the Riley County Police Department. Reports made to law enforcement are separate from reports made to OIE. A complainant can choose to report to one or both entities. Confidential support and advocacy can be found with the K-State Center for Advocacy, Response, and Education (CARE). Confidential mental health services can be found with Lafene Counseling and Psychological Services (CAPS). Academic support can be found with the Office of Student Life (OSL). OSL is a non-confidential resource. OIE also provides a comprehensive list of resources on their website. If you have questions about non-confidential and confidential resources, please contact OIE at equity@ksu.edu or (785) 532-6220. 

 
