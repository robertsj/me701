TARGET     = ex2
OBJFILES   = example2.o example2_f_and_J.o
CLEANFILES = $(TARGET)

include ${PETSC_DIR}/lib/petsc/conf/variables
include ${PETSC_DIR}/lib/petsc/conf/rules

all: $(TARGET)

$(TARGET) : $(OBJFILES)
	${CXXLINKER} -o $(TARGET) $(OBJFILES) ${PETSC_LIB}

