export PETSC_DIR=/home/robertsj/tmp/petsc_stuff/petsc
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
