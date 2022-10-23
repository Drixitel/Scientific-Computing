! /codes/circle3/circle_mod3.f90
! Version where pi is a module variable, and contents default to private

module circle_mod3

  implicit none
  private
  
  integer, parameter, public :: fp = selected_real_kind(15)
  real (fp), save :: pi ! this is the only thing private

  ! Public interface --All public subroutines 
  public :: initialize
  public :: area
  public :: circumference

contains

  subroutine initialize()

    ! Set the value of pi
    pi = acos(-1.0_fp)

  end subroutine initialize

  real (fp) function area(r)
    real (fp), intent(in) :: r
    area = pi * r**2
  end function area

  real (fp) function circumference(r)
    real (fp), intent(in) :: r
    circumference = 2.0_fp * pi * r
  end function circumference

end module circle_mod3
