!! /codes/lapack/solve1.f90
!! This routine solves Ax=b using DGESV routine in LAPACK.
!!
!! Recall that the naming convention follows (see http://www.netlib.org/lapack/lug/node26.html)
!!   D:  double precision
!!   GE: general type of matrix
!!   SV: simple driver by factoring A and overwriting B with the solution x
!!
!! See also:
!! a. https://software.intel.com/sites/products/documentation/doclib/mkl_sa/11/mkl_lapack_examples/dgesv.htm
!! b. http://www.netlib.org/clapack/old/double/dgesv.c
!!


program solve1
  implicit none
  integer, parameter :: n=3, fp = selected_real_kind(15)
  real (fp), dimension(n) :: x,b
  real (fp), dimension(n,n) :: a
  integer :: i, info, lda, ldb, nrhs
  integer, dimension(n) :: ipiv

  a = reshape((/1._fp, 2._fp, 2._fp, 0._fp, -4._fp, -6._fp, 0._fp, 0._fp, -1._fp/), (/n,n/)) ! Matrix
  b = (/3._fp,-6._fp,1._fp/)  ! targt 
  x = b ! solutoni

  nrhs = 1
  lda = n
  ldb = n
  ! this is a function from lapack and is not defined anywere in our program
  call dgesv(n, nrhs, a, lda, ipiv, x, ldb, info)
  ! dgesv: 
  !     d: double precision floats (1st character tells the type of data being used)
  !     g: (type of matrix) ge is general matrix
  !     sv... : tells the action sv = solver
  !   Arguments: 
  !       (number of linear equations, # of right hand side matix, matrix itself, # of rows in matix, 
  !             )
  print*, 'solving Ax = b'
  do i = 1,n
    print *, i, x(i)
  end do

end program solve1
