program segfault

  implicit none

  real, dimension(10) :: a
  integer :: i

#ifdef DEBUG_MODE
  print*,'beginning do loop'
  print*, size(a),a
#endif

  do i = 1, 5000, 199
    a(i) = i

#ifdef DEBUG_MODE
    print*,'  in do loop'
    print*, i,a(i)
#endif
  end do

#ifdef DEBUG_MODE
  print*,'end of do loop'
#endif

end program segfault
