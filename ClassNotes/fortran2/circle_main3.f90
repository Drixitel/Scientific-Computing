! /codes/circle3/circle_main3.f90

program circle_main3
  ! Remove pi from the only: , after checking private 
  use circle_mod3, only: fp, initialize, area !, pi
  ! Lint error: not found in module (bc Private)
  implicit none
  real (fp) :: a

  call initialize()   ! sets pi

  ! Check if we can call pi from module:
  !   uncommment below, recall it was set to private
  ! print module variable pi:
  ! print *, 'pi = ', pi
  ! Lint error: No implicit type i.e. - DNE
  !       Implicit none, throws this warning 

  ! test the area function from module:
  a = area(2.0_fp)
  print *, 'area for a circle of radius 2: ', a

end program circle_main3
