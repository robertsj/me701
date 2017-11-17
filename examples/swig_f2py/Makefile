SWIG_INCLUDES=-I/home/robertsj/opt/anaconda3/include/python3.6m -I/home/robertsj/opt/miniconda3/lib/python3.6/site-packages/numpy/core/include

all: f2py_demo f2py_demo2 swig_demo swig_demo2

# F2PY demonstration
f2py_demo:
	f2py -c -m simple_f90_demo simple_f90_demo.f90
f2py_demo2:
	f2py -c -m module_f90_demo module_f90_demo.f90

swig_demo:
	swig -python -c++ simple_cpp_demo.i
	g++ -fPIC -c simple_cpp_demo.cc simple_cpp_demo_wrap.cxx ${SWIG_INCLUDES}
	g++ -shared simple_cpp_demo.o simple_cpp_demo_wrap.o ${SWIG_INCLUDES} -o _simple_cpp_demo.so 

swig_demo2:
	swig -python -c++ class_cpp_demo.i
	g++ -fPIC -c class_cpp_demo.cc class_cpp_demo_wrap.cxx ${SWIG_INCLUDES}
	g++ -shared class_cpp_demo.o class_cpp_demo_wrap.o ${SWIG_INCLUDES} -o _class_cpp_demo.so 


# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x *wrap.cxx *.so *.pyc

# Same, but leave the shared objects
neat:
	@rm -f *.o *.mod *-x *wrap.cxx *.pyc

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .f90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<
