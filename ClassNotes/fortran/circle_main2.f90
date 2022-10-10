! /codes/circle2/circle_main2.f90

program circle_main2

  use circle_mod2, only: fp, pi, initialize, area
  implicit none
  real (fp) :: a

  call initialize()   ! sets pi

  ! print module variable pi:
  print *, 'pi = ', pi

  ! test the area function from module:
  a = area(2.0_fp)
  print *, 'area for a circle of radius 2: ', a

end program circle_main2
