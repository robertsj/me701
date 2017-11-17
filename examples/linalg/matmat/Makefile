# Makefile for linear algebra tests 

#===============================================================================
# User Options
#===============================================================================

F90=gfortran
CXX=g++
OPT=-O3 -march=core-avx2 -v
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

all: driver-mm-x driver-mm-blas-x driver-mm-mkl-x 

#===============================================================================
# Matrix-Vector Tests
#===============================================================================

# Row-major MV test
driver-mm-x: matrix_matrix.o test_matrix_matrix.o
	$(F90) $(OPT) $(OMPFLAG) matrix_matrix.f90 test_matrix_matrix.f90 -o $@ 

# Use the repository's BLAS implementation
driver-mm-blas-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_matrix.f90 -o $@ $(LIBBLAS)

# Use MKL
driver-mm-mkl-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_matrix.f90 -o $@ $(LIBMKL)

# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x driver-mm-x driver-mm-mkl-x

# Same, but leave the executable
neat:
	@rm -f *.o *.mod

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .F90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(OPT) $(OMPFLAG) $(INCLUDE) -c $<
