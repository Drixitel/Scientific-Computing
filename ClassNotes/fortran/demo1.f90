! /codes/demo1.f90
! Fortran 90 program illustrating data types.
! Note that you should pick one convention, rather
! than mixing matching like this file does. This is
! just for illustration

! .f90 files always start with program {filename}
!   and end with end program (filename)
!   Can only have one pair of (program,end program)

! Start Code -----------------------------------------------
program demo1

  implicit none 
  ! implicit none :
  !   Removes an unwanted feature where the code determines 
  !   The type of variable you want just by the name of the variable 
  !   E.g. if the variable is i,j,k the compilier will think you want
  !         it to be an integer. 
! Define Variables --------------------------------------------
  integer, parameter :: fp = selected_real_kind(7) ! Use this format
  ! integer: is a type 
  ! parameter: takes the role of constant
  !   There for the integer {fp} will never change its value
  ! selected_real_kind() and kind= : PRECISION/MEMORY
  !    kind = 4 : single precision 4 bytes
  !    kind = 8 : double 
  !    selected_real_kind(#): I want at least # places 
  !         past the decimal
  integer, parameter :: dp = selected_real_kind(15) 
  real :: x   
  ! floating point rep. of variable x
  real (kind=dp) :: y,z ! do this format 
  ! kind: related to memory space/precision of variable 
  integer :: m    
  ! Variable {m} is not assigned keyword parameter so it can be changed later in code
  real (dp) :: i,a    ! do not do this format
  ! keyword kind is omitted, however it is still specified 
  ! anything not declared will throw an error 

! Test Code -------------------------------------------------------------------------
  ! Comment out implicit none and the declaration for i, then observe
  ! what the following lines do:
  i = 10
  print*, i
  print*, "i = 10 but implicit assignment will change it"

  i = 10.2394872938479287
  print *,i
  print*, "now, i = 10.2394872938479287 but implicit assignment will change it"

  a = 1.3234 
  !  NOTE:  a is not formally defined, but we have no issue
  !         implicit will assign it by force if we do not have {implicit none}
  print*,a
  print*, "a = 1.3234 but implicit assignment will change it"

! Bunch of print statements ---------------------------------------------------------
  m = 3
  print *, " "
  print *, "M = ", M   
! NOTE: that M is the same as m  (It is case IN-sensitive)


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