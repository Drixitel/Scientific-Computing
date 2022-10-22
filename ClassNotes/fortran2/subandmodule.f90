! /codes/sub3.f90

module sub3module 
! having the subrout in a module fixes the warnings of 
! Implicit interface. The progarm and subroute can stay seperate

contains 

  subroutine fsub(x,f)
    ! compute f(x) = x**2 for all elements of the array x. 
    implicit none
    real (kind=8), intent(in) :: x(:) ! Rank 1 Array length : any 
    real (kind=8), intent(out) :: f(size(x)) ! Rank 1 length : of input x
    f = x**2
  end subroutine fsub

end module sub3module

!----------------------------------------------

program sub3
  use sub3module ! use: call the modules 
  implicit none
  real (kind=8) :: y(3), z(3)

  y = (/2., 3., 4./)
  call fsub(y,z)
  print *, "z = ",z
end program sub3
