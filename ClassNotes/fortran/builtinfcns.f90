! /codes/builtinfcns.f90

program builtinfcns

  implicit none
  integer, parameter:: dp = selected_real_kind(15)
  real (dp) :: pi, x, y

  ! compute pi as arc-cosine of -1:
  pi = acos(-1.0_dp)
  !! try running: just acos(-1.0)
  !! removing the underscore reduced the precision 
  !! to promote this literal back up we can do 
  !! gfortran -fdefault-real-8 filename (not.ex) && ./file
  !! can do the underscore or use the previous code to 
  !!!  get the precision you want 

  x = cos(pi)
  y = (exp(3.d0 * log(pi)))**(1.d0/3.d0)  ! need 3.d0 or 3.0_dp for full precision!

  print *, "pi = ", pi
  print *, "x  = ", x
  print *, "y  = ", y

end program builtinfcns
