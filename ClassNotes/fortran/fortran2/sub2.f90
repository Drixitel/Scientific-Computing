! /codes/sub2.f90

program sub2
  implicit none
  real (kind=8), dimension(3) :: y, z ! Rank 1 array of length 3
  integer :: n

  y = (/2., 3., 4./)
  n = size(y)
  call fsub(n,y,z)
  print *, "z = ",z
end program sub2

subroutine fsub(n,x,f)
  ! compute f(x) = x**2 for all elements of the array x 
  ! of length n.
  ! THIS IS AN OLD METHOD TO PASS AN ARRAY TO A SUBROUTE
  implicit none
  integer, intent(in) :: n
  real (kind=8), dimension(n), intent(in) :: x
  real (kind=8), dimension(n), intent(out) :: f
  f = x**2
end subroutine fsub
