! /codes/arrayops.f90

program arrayops

  implicit none
  integer, parameter:: dp = selected_real_kind(15)
  real(dp), dimension(3,2) :: a
  real(dp), dimension(2,3) :: b
  real(dp), dimension(3,3) :: c
  real(dp), dimension(2) :: x
  real(dp), dimension(3) :: y
  integer :: i

  a = reshape((/1,2,3,4,5,6/), (/3,2/))
  ! all listed literally then reshaped into a 3x2

  print *, "a = "
  do i=1,3
    print *, a(i,:)   ! i'th row (slicing)
  end do

  b = transpose(a)

  print *, "b = "
  do i=1,2
    print *, b(i,:)   ! i'th row
  end do

  c = matmul(a,b)
  print *, "c = "
  do i=1,3
    print *, c(i,:)   ! i'th row
  end do

  x = (/5,6/) !this sets an array as a literal
  ! this wil fil the rank 1 array with the values 5,6
  y = matmul(a,x)
  print *, "x = ",x
  print *, "y = ",y

end program arrayops
