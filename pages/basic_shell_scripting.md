# Basic Shell Scripting                                                                

## Summary

By the end of this lecture, you will understand how to write simple programs
in `bash`, the The Bourne again shell we are using in Linux.

## Resources

[The Linux Command Line](http://linuxcommand.org/tlcl.php) is also a good resource
for `bash` in addition to general command line usage.

This [bash cheat sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
is quite extensive.


##  Evidence of Student Learning

  - Students will define and use variables in `bash`
  - Students will explain what special variables like `$1` mean in `bash`
  - Students will write short functions in `bash` that perform simple
    tasks
  - Students will execute all examples provided in the lesson notebook


## Learning Plan

### Before Lecture

  - Skim TLC 363--494
  - Create a comparison sheet of bash relative to your favorite programming
    language. Most likely, `bash` (as a language) is new to all of you, and I
    find the best way to learn a new language is to compare its
    syntax (variables, if statements, for loops, etc.) to those of a language
    I already know (e.g., Python).  You may find [this cheat sheet](https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)
    to be helpful.


### During Lecture

  1. Brief discussion of `bash` and its origins
  2. Demonstrate how to define variables in `bash`
  3. Demonstrate and reinforce some command line tricks like "piping" with `|`
  4. Demonstrate how to construct functions in `bash`
  5. Demonstrate basic `if` statements and loops.

### After Lecture

 - [Video, Lecture, 08/30/2021](https://mediasite.k-state.edu/mediasite/Play/73cd959fa3f64655acd957b3c80022421d)

 - [Video, Lecture, Fall 2019](https://mediasite.k-state.edu/mediasite/Play/71e3cbcaaadf46df8134e058a538b5821d)
   and [slides](https://github.com/robertsj/me701/blob/f2020/lectures/BashDemo.ipynb).
   If you want to execute the notebook, you will need to install the `bash` kernel for Jupyter.
   That is not necessary; all commands I use can be executed directly in the terminal or
   saved and run as scripts.

### Jeremy's Notes

 - Variable assignments should not have spaces (i.e., `a=123` is good but `a = 123` is bad).

