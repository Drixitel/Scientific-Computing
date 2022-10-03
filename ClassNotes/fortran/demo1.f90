! /codes/demo1.f90
! Fortran 90 program illustrating data types.
! Note that you should pick one convention, rather
! than mixing matching like this file does. This is
! just for illustration

program demo1

  implicit none !! turns off assumed typing 
  !! also if a variable is added without first declaring it will thow an error (needs implicit none) 
  integer, parameter :: fp = selected_real_kind(7) !! parameter is like constant 
  integer, parameter :: dp = selected_real_kind(15) !!selected real kind (places past dec)
  real :: x   !! floating point rep. of x 
  real (kind=dp) :: y,z   !! memory speace (kind), 
  integer :: m    !! not a parameter so it can be changed
  real (dp) :: i    !! don't need to write kind, but does the same (just here to show)

  ! Comment out implicit none and the declaration for i, then observe
  ! what the following lines do:
  ! i = 10
  ! print*, i
  ! i = 10.2394872938479287
  ! print *,i
  ! a = 1.3234 !! notice a is not defined, but it can appear, but it will become a type real 
  !! variables become certain types depending on the nameing (not bc of anything else)
  !! e.g: i,j,k are integrers etc. 
  !! this occurs bc implicit none is not included 
  ! print*,a

  !! bunch of print statements 
  m = 3
  print *, " "
  print *, "M = ", M   ! note that M is the same as m  (case insensitive)


  print *, " "
  print *, "x is real (kind=4)"
  x = 1.0_fp + 1.23456789e-6_fp
  print *, "x = ", x


  print *, " "
  print *, "y is real (kind=8)"
  print *, "  but 1.e0 is real (kind=4):"
  y = 1.0_fp + 1.23456789e-6_fp
  print *, "y = ", y


  print *, " "
  print *, "z is real (kind=8)"
  print *, "  and 1.d0 is real (kind=8):"
  ! The following line is equivalent to z = 1.d0 + 1.23456789d-6
  z = 1.0_dp + 1.23456789e-6_dp
  print *, "z = ", z

end program demo1

!! to run: 
!! gfortran filename (this compules the files)
!! ls 
!! ./a.out (this notation will change)
!! a.out = assembler output 

!! to better label files: 
!! gfortran -o filenewname.ex filename (make an executable)
!! do not use .exe 
!! What is ./ notation 
!! This is due to .bash and how it executes 
!! consider creating a bin for .ex files 
!! in same location ./ 
!! in not the same location pass location 

!! a make file can remove the need to compile and more 
!! files 

!! about Kind parameter: 
!!  without kind we get single precision 
!!  with kind we get more precision (double)
!!  kind = 4 (takes up 4 bytes with 8 decimals)
!!  kind = 8 (takes up 8 bytes with double dec.)
!!  To fix the kind based on precision we use 
!!    seleced real kind (number past the dec.)

!! Intrinsic Functions
!! fortran has them bultiin 