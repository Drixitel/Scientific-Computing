! /codes/circle3/circle_main3.f90

program circle_main3

  use circle_mod3Private, only: fp, initialize, area
  implicit none
  real (fp) :: a

  call initialize()   ! sets pi

  print *, 'File circle_main3.f90'
  ! not allowed to pint pi, bc it's private
  ! print module variable pi:
  ! print *, 'pi = ', pi

  ! test the area function from module:
  a = area(2.0_fp)
  print *, 'area for a circle of radius 2: ', a

end program circle_main3
