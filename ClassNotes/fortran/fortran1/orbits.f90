! File: Orbits.f90
! Author: Ian May

program orbits

  use utility, only: fp
  use timestep, only: take_step

  implicit none
  
  integer, parameter :: nSteps = 1000  ! Number of time steps to use
  integer :: nT                        ! Loop variable for time updates
  !!! Step 1

  ! Give all particles initial mass, position, and momentum
  call set_ics()

  ! Fill rest of the array by integrating in time
  do nT=1,nSteps-1
    call take_step(dt,mass,pos(:,:,nT),mom(:,:,nT),pos(:,:,nT + 1),mom(:,:,nT + 1))
  end do

  ! Write the arrays to a file for plotting
  call write_data()

contains

  subroutine set_ics()
    implicit none
    !!! Step 2
    ! Set particle masses

    
    ! First particle position and momentum
    

    
    ! Second particle position and momentum


    
  end subroutine set_ics

  subroutine write_data()
    implicit none
    open(20,file = "data/sol.dat",status = "replace")
    do nT=1,nSteps
      write(20,*) pos(:,:,nT),mom(:,:,nT)
    end do
    close(20)
  end subroutine write_data

end program orbits
