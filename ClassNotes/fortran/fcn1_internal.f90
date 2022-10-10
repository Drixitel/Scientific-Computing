! /codes/fcn1_internal.f90

program fcn1
  implicit none
  integer, parameter :: fp = selected_real_kind(15)
  real (fp) :: y,w

  y = 2.0_fp
  w = f(y)
  ! function is used and not defined previously bc the program is aware
  !   due to keyword : contians
  print *, "y = ", y
  print *, "w = ", w

contains
! keyword: contains 
!   everything after this key word is a subroutine
!   in this version everything has access to one another
!   f(x) has acces to the constants and they to it because they are 
!   "contained in one another" 

  real (fp) function f(x)
    implicit none
    real (fp), intent(in) :: x
    f = x**2
  end function f

end program fcn1
