! /codes/sub1.f90

! Has NO RETURN VALUES 

!-----------------------commented code 
!!! This code will compile but with a warning 
!!!     we should always place the subroutine in the program
!!!     or in a module, the corrected code is added below

! program sub1
!   implicit none
!   real (kind=8) :: y, z

!   y = 2.
!   call fsub(y,z) ! call subroutine 
!   print *, "z = ",z
! end program sub1

! subroutine fsub(x,f)
!   implicit none
!   ! Required lines for subroutine 
!   real (kind=8), intent(in) :: x
!   real (kind=8), intent(out) :: f
!   f = x**2
! end subroutine fsub

!-----------------------commented code 

program sub1
  implicit none
  real (kind=8) :: y, z

  y = 2.
  call fsub(y,z) ! call subroutine 
  print *, "z = ",z

  contains 

subroutine fsub(x,f)
  implicit none
  ! Required lines for subroutine 
  real (kind=8), intent(in) :: x
  real (kind=8), intent(out) :: f
  f = x**2
end subroutine fsub

end program sub1