# We can define things like the compiler
CXX=g++
F90=gfortran

# Basic goal: make a target
say_hello:
	echo "Hello world"
# ^^^ 
# TAB! Not whitespace.  Won't work!

# We can use it to automate LaTeX
slides:
	pdflatex cpp_fortran.tex
	pdflatex cpp_fortran.tex

# Make a program all at once
declaring_cc:
	$(CXX) -o declaring_cc declaring.cc

# Make a program with dependencies
control.o: control.cc
	$(CXX) -c control.cc
control_cc: control.o
	$(CXX) -o control_cc control.o

# Other programs
basic_arrays.o: basic_arrays.cc
	$(CXX) -c basic_arrays.cc
basic_arrays_functions.o: basic_arrays_functions.cc
	$(CXX) -c basic_arrays_functions.cc
basic_arrays_cc: basic_arrays.o basic_arrays_functions.o
	$(CXX) -o  $@ $^

# Some special characters:
#   $@ - target name
#   $< - name of the first dependency
#   $^ - names of all dependencies
# Could use to do, e.g.,
# 
# control_cc: control.o
# 	$(CXX) -o $@ 

