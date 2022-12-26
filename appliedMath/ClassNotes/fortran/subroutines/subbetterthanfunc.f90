! /codes/sub1.f90

program sub1
  implicit none
  real (kind=8) :: y, z

  y = 2.
  call fsub(y,z) ! calling a function not in the progarm 
  ! call: replaces the need to use external :: fsub 
  ! See fcn1.f90 for an example of it 
  ! Compiler finds sunroutine 
  print *, "z = ",z
!==========Comment out and uncomment external subroute to use it externally ==========
  contains

subroutine fsub(x,f) ! subroute: has no return value 
  ! nameOfSubrout(input,output)
  ! every input and output must be defined
  implicit none
  real (kind=8), intent(in) :: x
  real (kind=8), intent(out) :: f
  f = x**2
  ! you can output any # of items in a subroutine 
  ! if you need multiple things, it's best to use a subroute vs. a function 
end subroutine fsub
! ===========================================================

end program sub1
! ============= uncomment to use it as an external subroutine ===============
!``````  HAVEING SUBROUTE OUTSIDE WILL THROW AN IMPLICIT INTERFACE FLAG`````````
! -Wimplicit-inerface
!     This flag is due to the compliler having to guess what it is
 
! TO FIX ERROR AND KEEP IT OUTSIDE: 
!   - just put the subroutine in a module
!   - see file sub3module.f90

!subroutine fsub(x,f) ! subroute: has no return value 
!   ! nameOfSubrout(input,output)
!   ! every input and output must be defined
!   implicit none
!   real (kind=8), intent(in) :: x
!   real (kind=8), intent(out) :: f
!   f = x**2
!   ! you can output any # of items in a subroutine 
!   ! if you need multiple things, it's best to use a subroute vs. a function 
! end subroutine fsub
! ====================================================================================