! /codes/fcn1.f90

program fcn1
  implicit none
  real (kind=8) :: y, z
  ! NOTE: the better select_real_kind() cannot be used 
  !   Since f(x) is external they cannot see the constants
  !   they do not have access, kind is difined explicitly everywhere
  real (kind=8), external :: f
  ! external means it is not in this file 
  ! compiler needs to go searching for this symbol

  y = 2.d0
  z = f(y)
  print *, "y = ", y
  print *, "z = ", z
end program fcn1
! END PROGRAM PASSED, THE PROGRAM HAS ENDED



! New code for definition of symbol/function {f}
real (kind=8) function f(x)
! declare the type to return is real
! keyword: function 
! name and parameters {f(x)}
  implicit none
! implicit is always added
  real (kind=8), intent(in) :: x
! declaration of input variable 
  f = x**2
! default is to assine by the same name {f}
end function f
