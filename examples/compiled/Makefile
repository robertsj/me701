# We can define things like the compiler
CXX=g++
F90=gfortran

# Basic goal: make a target
say_hello:
	echo "Hello world"
# ^^^ 
# TAB! Not whitespace.  Won't work!

# Make a program all at once
declaring_cc:
	$(CXX) -o declaring_cc declaring.cc

# Make a program with dependencies
control.o: control.cc
	$(CXX) -c control.cc
control_cc: control.o
	$(CXX) -o control_cc control.o

# Some special characters:
#   $@ - target name
#   $< - name of the first dependency
#   $^ - names of all dependencies
# Could use to do, e.g.,
# 
# control_cc: control.o
# 	$(CXX) -o $@ 

