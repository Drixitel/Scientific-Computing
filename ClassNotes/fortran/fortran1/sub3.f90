! /codes/sub3.f90

module sub3module
! typicaly modules are in thier own files but this is fine for e.g.
contains 

  subroutine fsub(x,f)
    ! compute f(x) = x**2 for all elements of the array x. 
    implicit none
    real (kind=8), intent(in) :: x(:)
    ! the {:} says: a Rank 1 array but I don't care how long it is
    real (kind=8), intent(out) :: f(size(x))
    ! {f} is also a Rank 1 array with no care of length
    f = x**2
  end subroutine fsub

end module sub3module
! having the subr. be inside the module removes warnings and compiles normally

!----------------------------------------------

program sub3
  use sub3module
  ! use-statement can be amended to only call one function 
  ! Uncomment below it will call only the one function
  ! use sub3module, only:fsub


  implicit none
  real (kind=8) :: y(3), z(3)

  y = (/2., 3., 4./)
  call fsub(y,z)
  print *, "z = ",z
end program sub3
