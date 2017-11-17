F90=gfortran
OPT=-O3

triad:
	gcc $(OPT) -c timing.c dummy.c
	$(F90) -O3 -c triad.f90
	gfortran -O3 -o triadx triad.o dummy.o timing.o

triad_tuned:
	gcc $(OPT) -c timing.c dummy.c
	$(F90) -O3 -mtune=native -c triad.f90
	gfortran -O3 -mtune=native -o triadx_tuned triad.o dummy.o timing.o

