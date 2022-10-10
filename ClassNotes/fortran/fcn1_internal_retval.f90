! /codes/fcn1_internal_retval.f90

! TRY AND USE THIS STYLE AS OFTEN AS POSSIBLE
program fcn1
  implicit none
  integer, parameter :: fp = selected_real_kind(15)
  real (fp) :: y,z

  y = 2.0_fp
  z = square_number(y)
  print *, "y = ", y
  print *, "z = ", z

contains

  ! Function that returns the square of its input
  ! Allows a descriptive name
  function square_number(x) result(sqx)
    implicit none
    real (fp), intent(in) :: x ! Number to square
    ! intent: 
    !   specific to arguments coming in 
    !   for subroutines & is in read only 
    !   it cannot be modified by the program
    !   Good by convention to have intent(in) ONLY
    real (fp) :: sqx           ! Return variable
    sqx = x**2
    ! saved to sqx but we need not use it 
    ! we can used the descriptive name 
  end function square_number

end program fcn1
