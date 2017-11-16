# Makefile for linear algebra tests 

#===============================================================================
# User Options
#===============================================================================

F90=gfortran
CXX=g++
OPT=-O3
OMPFLAG=-fopenmp
ANACONDA=/home/robertsj/opt/miniconda3


#===============================================================================
# Vendor BLAS implementations
#===============================================================================

# For linking MKL, see:
#   http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor/
LIBMKL = -L$(ANACONDA)/lib -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -lpthread -lm -ldl   
  
# BLAS defines a generic set of functions with vendor-specific
# implementations; here, we use the blas implementation from the 
# software repository.  You may need to do "sudo apt install libblas"
LIBBLAS = -L /usr/lib -lblas

#===============================================================================
# Targets
#===============================================================================

all: driver-mv-row-x driver-mv-col-x driver-mv-blas-x driver-mv-mkl-x \
     driver-mv-col-cxx-x driver-mv-mkl-cxx-x

#===============================================================================
# Matrix-Vector Tests
#===============================================================================

# Row-major MV test
driver-mv-row-x:
	$(F90) $(OPT) $(OMPFLAG) matrix_vector_rm.f90 test_matrix_vector.f90 -o $@ 

# Column-major MV test
driver-mv-col-x:
	$(F90) $(OPT) $(OMPFLAG) matrix_vector_cm.f90 test_matrix_vector.f90 -o $@ 

# Use the repository's BLAS implementation
driver-mv-blas-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_vector.f90 -o $@ $(LIBBLAS)

# Use MKL
driver-mv-mkl-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_vector.f90 -o $@ $(LIBMKL)

# Use column-major Fortran code with C++
driver-mv-col-cxx-x:
	$(F90) $(OPT) $(OMPFLAG) -c -fno-underscoring matrix_vector_cm.f90 
	$(CXX) $(OPT) $(OMPFLAG) -c test_matrix_vector.cc
	$(CXX) $(OPT) $(OMPFLAG) matrix_vector_cm.o test_matrix_vector.o -o $@

# Use MKL with C++
driver-mv-mkl-cxx-x:
	$(CXX) $(OPT) $(OMPFLAG) test_matrix_vector.cc -o $@ $(LIBMKL)


# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x

# Same, but leave the executable
neat:
	@rm -f *.o *.mod

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .F90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<
