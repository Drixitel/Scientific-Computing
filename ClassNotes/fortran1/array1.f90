! /codes/array1

program array1

  ! demonstrate declaring and using arrays

  ! MATRIX: ROW X COLOUMN 
  implicit none
  integer, parameter:: dp = selected_real_kind(15) ! Integer constant for precision
  ! SET the SIZES for arrays
  integer, parameter :: m = 2, n = 3              ! Integer constants for array sizes
  ! CREATE ARRAYS
  ! MATRIX:
  real (dp), dimension(m,n) :: A                   ! Rank 2 array (matrix 3 x 2)
  ! ARRAY
  real (dp), dimension(m) :: b                     ! Rank 1 array, size 3
  ! ARRAY
  real (dp), dimension(n) :: x                     ! Rank 1 array, size 2 
  ! OTHER USED VARIABLES
  integer :: i, j                                  ! Loop variables
  !------------ADDED FOR TESTING --------------------------------------------
  integer, parameter:: fp = selected_real_kind(15) ! Integer constant for precision
  real (fp), dimension(size(A,1))  :: y1           ! Result size, similar to what we have
  integer ::   rows, cols                          ! integers to keep track of A(rows,cols)


  ! Initialize matrix A and vector x:------------------------------TO TEST WITH
  ! NOTE: that i and j get promoted to double precision on assignment into A
  do j=1,n
    do i=1,m
      A(i,j) = i + j
    end do
    x(j) = 1.
  end do
  !--------------------------------------------------------------------------

  ! multiply A*x to get b:------------------------------------ORIGINAL WAY-----
  ! This requires we change the integers from the above declarations, each time
  do i=1,m
    b(i) = 0.
    do j=1,n
      b(i) = b(i) + A(i,j)*x(j)
    end do
  end do

  !---TEST THE FUNCTION WE CREATED ------------------------------------------
  !   We use A and x that were already defined from the prev. program
  y1 = matvecprod(A,x)

  !--------------------------------------------------------------------------

  ! Check out what A looks like ---------------------------
  print *, "A = "
  do i=1,m
    print *, A(i,:)   ! i'th row of A
  end do

  ! Check out x - notice the formatting, it gives .500D+01 = 5 (stupid)
  print *, 'x = '
  print "(d12.4)", x

  ! CHECK OUT THE FINAL RESULT!!! 
  print *, 'y = Ax'
  print *, 'y = '
  print "(d12.4)", y1


  !---------------------------------------------------------

  !-----OLD PRINTS FOR TESTING ------------------
  ! print "(2d16.6)", ((A(i,j), j=1,2), i=1,3)
  ! print *, "x = "
  ! print "(d12.4)", x
  ! print *, "b = "
  ! print "(d16.6)", b.
  print *, 'Number of Cols ', size(A(1,:))
  print *, 'Number of Rows ', size(A(:,1))
  print *, 'Number of elements', size(A(:,:))
  ! print *, A(:,1)
  ! print *, x(1)
  print *, 'size of x', size(x)


  contains 

  function matvecprod(A1,x1) result(y)
    implicit none
    real (fp), intent(in)            :: A1(:,:)            ! Rank 2 matirx 
    real (fp), intent(in)            :: x1(:)              ! Rank 1 matrix/ column vector 
    real (fp), dimension(size(A,1))  :: y                 ! y = Ax, size of a column in A
    integer :: r,s
    cols= size(A1(1,:))
    rows = size(A1(:,1))
    ! Multiply y = A*x
    do r =1,rows
      y(r) = 0
      do s = 1, cols
        y(r) = y(r) + A1(r,s) * x1(s)
      end do
    end do
  end function matvecprod
    

end program array1
