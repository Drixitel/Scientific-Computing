! /codes/array1

program array1

  ! demonstrate declaring and using arrays

  ! MATRIX: ROW X COLOUMN 
  implicit none
  integer, parameter:: dp = selected_real_kind(5) ! Integer constant for precision
  ! SET the SIZES for arrays
  integer, parameter :: m = 3, n = 2               ! Integer constants for array sizes
  ! CREATE ARRAYS
  ! MATRIX:
  real (dp), dimension(m,n) :: A                   ! Rank 2 array (matrix 3 x 2)
  ! ARRAY
  real (dp), dimension(m) :: b                     ! Rank 1 array, size 3
  ! ARRAY
  real (dp), dimension(n) :: x                     ! Rank 1 array, size 2
  ! OTHER USED VARIABLES
  integer :: i, j                                  ! Loop variables

  ! Initialize matrix A and vector x:
  ! NOTE: that i and j get promoted to double precision on assignment into A
  do j=1,n
    do i=1,m
      A(i,j) = i + j
    end do
    x(j) = 1.
  end do

  ! multiply A*x to get b:
  do i=1,m
    b(i) = 0.
    do j=1,n
      b(i) = b(i) + A(i,j)*x(j)
    end do
  end do

  print *, "A = "
  do i=1,m
    print *, A(i,:)   ! i'th row of A
  end do
  print "(2d16.6)", ((A(i,j), j=1,2), i=1,3)
  print *, "x = "
  print "(d12.4)", x
  print *, "b = "
  print "(d16.6)", b

end program array1
