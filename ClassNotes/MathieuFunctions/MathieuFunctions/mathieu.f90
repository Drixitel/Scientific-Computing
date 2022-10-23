! File: mathieu.f90
! Author: Ian May
! Purpose: Compute Mathieu functions of the first kind numerically

program mathieu
  use utility, only : fp, pi
  use problemsetup, only : Npts, qIdx, outFile, problemsetup_Init
  use diffop, only : diffop_Mathieu
  implicit none
  
  ! Size of transform
  ! Problem data---all the lapack functions
  integer :: info,lwork                               ! dgeev return code and size of workspace
  real (fp) :: dx                                     ! grid spacing
  real (fp), allocatable :: x(:)                      ! grid points
  real (fp), allocatable :: wr(:), wi(:)              ! real and imaginary parts of e-vals
  real (fp), allocatable :: work(:)                   ! Workspace for dgeev
  real (fp), allocatable :: H(:,:), vr(:,:), vl(:,:)  ! operator, right e-vecs, left e-vecs

  ! Loop variables
  integer :: i,j
  
  ! Read in the input file---------------------
  call problemsetup_Init('mathieu.init')
  
  ! Set local variables
  lwork = 8*Npts
  dx = 2*pi/Npts
  
  ! Allocate arrays to match problem size
  allocate(x(Npts))
  allocate(wr(Npts))
  allocate(wi(Npts))
  allocate(work(lwork))
  allocate(H(Npts,Npts))
  allocate(vl(Npts,Npts))
  allocate(vr(Npts,Npts))
  
  ! Set up physical domain
  do i=1,Npts
    x(i) = (i-1)*dx
  end do
  
  ! Get Mathieu operator
  call diffop_Mathieu(qIdx,x,H)
  
  ! Use Lapack to find the eigenvalues/eigenvectors of H
  call dgeev('N','V',Npts,H,Npts,wr,wi,vl,1,vr,Npts,work,lwork,info)
  
  ! Open the output file and write the columns
  open(20,file=outFile,status="replace")
  do i=1,Npts
    write(20,*) x(i), wr(i), wi(i), (vr(i,j), j=1,Npts)
  end do
  close(20)
  
  ! Deallocate all used space
  deallocate(x)
  deallocate(wr)
  deallocate(wi)
  deallocate(work)
  deallocate(H)
  deallocate(vl)
  deallocate(vr)
end program mathieu
