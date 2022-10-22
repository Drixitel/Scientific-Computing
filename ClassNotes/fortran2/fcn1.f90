! /codes/fcn1.f90
! Functions 

program fcn1
  implicit none
  real (kind=8) :: y, z
  real (kind=8), external :: f
  ! f is defined elsewhere i.e external 
  ! external, is not a nice sytax there are better ones

  y = 2.d0
  z = f(y)
  print *, "y = ", y
  print *, "z = ", z
end program fcn1

! outside of the program we have the definined function
!     normally found in an external module/file 

! Body of the funtion: 
!   With default nameing for f
real (kind=8) function f(x) ! default assign the the f bc they share the same name 
  implicit none                     ! best practice 
  real (kind=8), intent(in) :: x    ! declare type of input variables
  f = x**2                          ! returns f 
end function f
