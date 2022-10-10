! /codes/loops1.f90

program loops1

  implicit none
  integer :: i

  do i=1,3           ! prints 1,2,3 : i = start, stop (by 1 unless stated)
    print *, i       ! unformatted print 
  end do             ! to format remove (*) replace with format
  ! a do loop is the same as a for loop
  ! set i =1 
  ! print i 
  ! incriment until 3

  do i=5,11,2        ! prints 5,7,9,11 : i= start,stop, incriment
    print *, i       ! start 5, end 11, move by 2
  end do

  do i=6,2,-1        ! prints 6,5,4,3,2
    print *, i       ! reverse stride
  end do             ! start 6, move in reverse by 1 end at 2

  i = 0
  do while (i < 5)   ! prints 0,1,2,3,4
    print *, i       ! while loop 
    i = i+1
  end do

end program loops1
