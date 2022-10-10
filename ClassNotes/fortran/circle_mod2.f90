! /codes/circle2/circle_mod2.f90
! Version where pi is a module variable.

module circle_mod2

  implicit none
  integer, parameter :: fp = selected_real_kind(15)
  real (fp), save :: pi 
  ! save: makes pi sharabel across all modules 

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

end module circle_mod2
