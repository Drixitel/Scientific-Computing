# /codes/multifile/Makefile

# FOR some more INFO READ: Makefileinfo.pdf

# Set Flags and complilers 
FC = gfortran   # Complier 
FFLAGS = -O3	# optimization flags
DFLAGS = -g3	# debugging 
LFLAGS =		# linking leave blank - is valid

# Set Variables, so we no longer need them in the targets
OBJECTS = 	main.o sub1.o sub2.o
# PHONY: all targets that do not correspond to a file 
.PHONY: clean
# TARGET: this one makes a file
output.txt: main.ex
	./main.ex > output.txt

#----------Replaced with $(OBJECTS)----------
# ORIGINAL
# main.ex: main.o sub1.o sub2.o
# 	gfortran main.o sub1.o sub2.o -o main.ex
# 		$ : tells shell to expand ()

# ---------Replaced with flags ----------
# main.ex: $(OBJECTS)
# 	gfortran -o main.ex $(OBJECTS)

main.ex: $(OBJECTS)
	$(FC) $(LFLAGS) -o main.ex $(OBJECTS)

# --------Replaced with $.o line--------------------
# ORIGINAL
# main.o: main.f90
# 	gfortran -c main.f90
# sub1.o: sub1.f90
# 	gfortran -c sub1.f90
# sub2.o: sub2.f90
# 	gfortran -c sub2.f90

# ---------Replaced with flags ----------
# %.o : %.f90
# 	gfortran -c $< 

%.o : %.f90
	$(FC) -c $(DFLAGS) $<

# CLEAN TARGET-----------------------------------------
# Resets whole directory as though you compiled nothing 
# Is a debugging tool 
# requires: a .PHONY  object must be created 
# 		Why: bc we are not creating a target file it just needs to b called

clean:
	rm -f main.ex $(OBJECTS)


# MORE SYMBOLS: ----------------------------------------
# about: $@ $^
#		$< : matches the first first item 
#		$^ : matches the whole list
#			useful here in the linker target so they all show up in the link
#		$@ : corresponds to the target (output.txt) that we are building 