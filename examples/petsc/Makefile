export PETSC_DIR=/home/robertsj/opt/petsc/petsc-3.10.2
export PETSC_ARCH=gcc-shared-release
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PETSC_DIR/$PETSC_ARCH/lib

include ${PETSC_DIR}/lib/petsc/conf/variables
include ${PETSC_DIR}/lib/petsc/conf/rules

info:
	echo "PETSC Libraries are:\n  ${PETSC_LIB}"
	echo "CXXLINKER is:\n  ${CXXLINKER}"
	echo "FLINKER is:\n  ${FLINKER}"

hello: hello.o  chkopts
	-${CXXLINKER} -o hello hello.o  ${PETSC_LIB}
	${RM} hello.o

example1cc: example1.o  chkopts
	-${CXXLINKER} -o example1cc example1.o  ${PETSC_LIB}
	${RM} example1.o


example2_f_J.o: example2_f_J.cc
	$(PETSC_CXXCOMPILE) -o $@ $< 

example2cc: example2.o example2_f_J.o chkopts
	-${CXXLINKER} -o example2cc example2.o example2_f_J.o ${PETSC_LIB}
	${RM} example2.o


# Rule to compile all objects
%.o: %.cc 
	$(PETSC_CXXCOMPILE) -o $@ $< $(CXXFLAGS)

