! /codes//boolean1.f90

program boolean1

  implicit none
  integer :: i,k
  logical :: ever_zero
  real :: myTrulyTrulyVeryLongVariableNameToStoreRealVariable
  real :: a, b

  ever_zero = .false. !use dot notiation in fortran

  do i=1,10
    k = 3*i - 6
    print*, i, k, ever_zero, (k == 0)
    ever_zero = (ever_zero .or. (k == 0))
  end do

  if (ever_zero) then
    print *, "3*i - 6 takes the value 0 for some i"
  else
    print *, "3*i - 1 is never 0 for i tested"
  end if

  a = 1.0
  myTrulyTrulyVeryLongVariableNameToStoreRealVariable = 2.0
  b = a + myTrulyTrulyVeryLong& !end in & then the next line cont.
      &VariableNameToStoreRealVariable

  print*,a,b
end program boolean1
