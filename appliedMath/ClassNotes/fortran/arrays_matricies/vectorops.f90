! /codes/vectorops.f90
!! this is a great reason for using fortran? 
program vectorops

  implicit none
  integer, parameter:: dp = selected_real_kind(15)
  ! RANK 1 Arrays with 3 elements 
  !   i.e. dimension 1 with 3 elements 
  real (dp), dimension(3) :: x, y

  ! these values are not given precision?? 
  ! does it take on the prec.of the array? 
  x = (/10.,20.,30./)
  y = (/100.,400.,900./)

  print *, "x = " ! the print
  print *, x      ! the code 

  print *, "x**2 + y = "
  print *, x**2 + y

  print *, "x*y = "
  print *, x*y

  print *, "sqrt(y) = "
  print *, sqrt(y)

  print *, "dot_product(x,y) = "
  print *, dot_product(x,y)


end program vectorops
