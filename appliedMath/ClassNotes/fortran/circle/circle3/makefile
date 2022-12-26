# Fortran Complier 
FC = gfortran

# Debugging: Keep on each run 
FLAGS = -Wall -Wextra -Wimplicit-interface -fPIC -g
# 	-fbacktrace is now on by default 
# 	-Wall -Wextra: warnings and extra warnings 
# 	-Wimplicit-interface:
# 	-fPIC: 
# 	-g: debugging (ALWAYS ADD does not affect speed) 
#		tells memory location and file name in the backtrace

# Debugging: Remove when complete 
FFLAGS = -fmax-errors=5  -fcheck=all -fbacktrace
# 	-fmax-errors=5: 
# 	-fcheck=all : balance checking (can slow the program)
#		 =bounds: gives runtime error and array pulled from
#		 -bounds check will slow the processor
# 		 - Include this in debugging, remove once working properly

# Not sure what LFLAGS are
LFLAGS = 

# Optimization Flags: Slow it in debugging 
OFLAGS = -O3 -march=native -ffast-math -funroll-loops -ffree-line-length-none -Wuninitialized
# 	-ffree-line-length-none: no caps on the lines
# 	Other flags taken from IanMay website 


# OBJ: set of object files expected to loop through 
OBJ = circle_mod3Private.o circle_main3.o 

# Create the executable and apply flags 
# 	-o FILENAME: Specifies the name of the output file
# 				 default: a.out
circle.ex: $(OBJ)
# for debugging 
	$(FC) -o $@ $^ $(LFLAGS) $(FLAGS) $(FFLAGS)
# for optimization 
#	$(FC) -o $@ $^ $(LFLAGS) $(FLAGS) $(OFLAGS)
# Don't add these just yet 
#	clear
#	./$@

# about: $@ $^
#		$@ : corresponds to the target (orbits.ex) that we are building 
#		$^ : matches the whole list
#			useful here in the linker target so they all show up in the link
#		$< : matches the first first item 

# Create directories & Process/link Object Files 
# % % double percent, calls the same name 
%.o: %.f90
	$(FC) -c -o $@ $< $(FFLAGS)


# Clean up 
.PHONY: clean move data

clean:
	rm -f bvp.ex *.o *~ *.mod
move: 
	mv *.o obj
data: 
	mv *.dat data
