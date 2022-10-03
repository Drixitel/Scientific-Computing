! /codes/loops2.f90

program loops2

  implicit none
  integer :: i,j,jmax

  i = 0
  jmax = 100
  do j=1,jmax        ! prints 0,1,2,3,4
    if (i>=5) exit
    print *, i
    i = i+1
  end do

  if (j==jmax+1) then
    print *, "Warning: jmax iterations reached."
  end if

end program loops2
