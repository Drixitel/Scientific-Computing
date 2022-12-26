# codes/lapack/linear/makefile

FC = gfortran
FFLAGS = -O2 -g -Wall -Wextra
LFLAGS = -llapack
#LFLAGS = -L ../lapack-3.10.0 -llapack

.PHONY: clean all

all: solve1.ex randomsys1.ex randomsys2.ex randomsys3.ex

# this is correct
solve1.ex: solve1.o
	$(FC) solve1.o $(LFLAGS) -o solve1.ex

# this can be a bug depending on your gfortran version and your platform
# solve1.ex: solve1.o
# 	$(FC) $(LFLAGS) solve1.o  -o solve1.ex

randomsys1.ex: randomsys1.o init_random_seed.o
	$(FC) randomsys1.o init_random_seed.o $(LFLAGS) -o randomsys1.ex

randomsys2.ex: randomsys2.o init_random_seed.o
	$(FC) randomsys2.o init_random_seed.o $(LFLAGS) -o randomsys2.ex

randomsys3.ex: randomsys3.o  init_random_seed.o
	$(FC) randomsys3.o init_random_seed.o $(LFLAGS) -o randomsys3.ex

%.o : %.f90
	$(FC) $(FFLAGS) -c $<

clean:
	rm -f *.o *.ex
