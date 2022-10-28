! /codes/circle1/circle_mod.f90

module circle_mod

  implicit none
  integer, parameter :: fp = selected_real_kind(15)
  real (fp), parameter :: pi = 3.141592653589793d0

contains

  real (fp) function area(r)
    real (fp), intent(in) :: r
    area = pi * r**2
  end function area

  real (fp) function circumference(r)
    real (fp), intent(in) :: r
    circumference = 2.d0 * pi * r
  end function circumference

end module circle_mod
