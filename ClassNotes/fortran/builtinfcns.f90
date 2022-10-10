! /codes/builtinfcns.f90

program builtinfcns

  implicit none
  integer, parameter:: dp = selected_real_kind(5)
  real (dp) :: pi, x, y

  ! compute pi as arc-cosine of -1:
  pi = acos(-1.0)
  print *, "pi with out any precision labeled", pi

! Precision underscore:
!   -1.0_dp applying the underscore dp gives the literal 
!    the correct precision (15 spaces)
  pi = acos(-1.0_dp)
  print *, "pi with underscore labeled", pi
  ! -1.0 : is a floating point literal (not a variable)
  !       The use of this numebr must also be controlled for 
  !       precision by the compiler

! Precision Scientific Notation e:single d: double
  pi = acos(-1.e0)
  print *, "pi with .e0", pi

  x = cos(pi)
  y = (exp(3.d0 * log(pi)))**(1.d0/3.d0)  
  ! need 3.d0 or 3.0_dp for full precision!
  ! 3.e0 i s single prec. 
  ! 3.d0 is a double prec. 

  print *, "pi = ", pi
  print *, "x  = ", x
  print *, "y  = ", y

end program builtinfcns
