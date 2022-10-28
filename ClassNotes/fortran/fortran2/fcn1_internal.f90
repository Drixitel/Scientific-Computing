! /codes/fcn1_internal.f90
! COMPARE TO FILE : fcn1.f90

! Program defined but this time it  CONTIANS
!     the function we previously created 
program fcn1
  ! Best practice: impicit
  implicit none
  ! Best practice : set the kind
  integer, parameter :: fp = selected_real_kind(15)
  real (fp) :: y,z ! was in prev. 
  ! Missing: external real variable f 
  !   No longer needed as it is contained in
  !   the same file 

  !Program is the same 
  y = 2.0_fp
  z = f(y) ! can use it directly, did not need declare
  print *, "y = ", y
  print *, "z = ", z

  ! No longer ends the program, but announces CONTAINS
contains
  ! SUBROUTINE -- All the same as well 
  real (fp) function f(x) ! fp can be used here as well 
    implicit none
    real (fp), intent(in) :: x
    f = x**2
  end function f

end program fcn1
