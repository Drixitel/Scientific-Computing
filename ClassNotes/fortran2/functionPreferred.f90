! /codes/fcn1_internal_retval.f90
! COMPARE TO FILE : fcn1.f90 and fcn1_internal.f90
program fcn1
  implicit none
  ! Function is contained - no declarations needed
  integer, parameter :: fp = selected_real_kind(15)
  real (fp) :: y,z

  ! Normal Program 
  y = 2.0_fp
  z = square_number(y)
  print *, "y = ", y
  print *, "z = ", z

contains ! SUBROUTINE

  ! Function that returns the square of its input
  ! PREFERRED NOTATION: 
  ! function explicit_name(inputs) result(outputs)
  function square_number(x) result(sqx)
    implicit none
    ! Declare the inputs
    real (fp), intent(in) :: x ! Number to square
    ! intent(in): makes parameter x 'read only' 
    !             x cannot be modified! 
    !             e.g.: x = x**2 
    !                   sqx = x 
    !             used to make sure the code doesn't reach back to 
    !             where x is defined elsewhere and change it 

    ! Declare the outputs 
    real (fp) :: sqx           ! Return variable, this is not an intent(out) notice that
    ! Define the function's result 
    sqx = x**2
  end function square_number

end program fcn1


! Intent(inout)
!     out: will modify code out in other routines
!     functions: should be in only 
!     a subroutine is better used for out repsonsibilities 
