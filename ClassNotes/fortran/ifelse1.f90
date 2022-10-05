! /codes/ifelse1.f90

program ifelse1

  implicit none
  integer, parameter:: dp = selected_real_kind(15)
  real (dp) :: x
  integer :: i

  if (i<=2) then
    print *, "i is less or equal to 2"
  else if (i/=5) then
    print *, "i is greater than 2 but not equal to 5"
  else 
    print *, "i is equal to 5"
  end if

  x = sqrt(2.0_dp)
  if (x<2) then
    print *, "x is less than 2"
  else
    print *, "x is not less than 2"
  end if

end program ifelse1
