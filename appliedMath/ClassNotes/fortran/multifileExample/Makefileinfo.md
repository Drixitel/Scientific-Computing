# /codes/multifile/Makefile

output.txt: main.ex
	./main.ex > output.txt


--- main.ex has many .o files, and we need to keep track of them -----------

main.ex: main.o sub1.o sub2.o
	gfortran main.o sub1.o sub2.o -o main.ex
	
-------------------------------------See replacement below ---------------

--the following lines are all the same, so use pattern matching and loop -- 

main.o: main.f90
	gfortran -c main.f90
sub1.o: sub1.f90
	gfortran -c sub1.f90
sub2.o: sub2.f90
	gfortran -c sub2.f90
------------replace it with the following ---------
%.o : %.f90
	gfortran -c $< 

---------------About -------------------------------
% = matchingNames 
e.g.: cat.o and cat.f90 
	Call on them with %.o : %.f90 

$< take the name given in %.f90 
e.g.: cat.o : cat.f90 
		gfortran -c cat.f90
$ = expand 
< = the variable passed 
	
%targetCreation : %prereq/Dependancefiles
%CreateObjectfiles : %Requirethe.f90Files

--------------------------------main replacement -------------
