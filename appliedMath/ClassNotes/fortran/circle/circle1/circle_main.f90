! /codes/circle1/circle_main.f90

program circle_main

  use circle_mod, only: pi, area, fp
  implicit none
  real (fp) :: a

  print *, "File circle_main.f90"
  ! print parameter pi defined in module:
  print *, 'pi = ', pi

  ! test the area function from module:
  a = area(2.0_fp)
  print *, 'area for a circle of radius 2: ', a

end program circle_main
