program integrate
!------------------------------------------------------------------------------!
! This short program applies the midpoint rule and the Monte Carlo method
! to integrate the N-dimensional function 
!   f(x1, x2, ..., xN) = sqrt(x1 * x2 * ... * xN)
!------------------------------------------------------------------------------!
  implicit none
  integer :: dimensions(3) = (/1,3,10/)
  integer :: max_divisions(3)  = (/100, 20, 3/)
  integer :: wunit=6, io, m, n, i
  double precision :: ref, mc, mp
  character(len=20) :: output_file
  open (unit = wunit, file = "errors.txt", action = "write", &
        status = "unknown", position = "rewind", iostat = io)
  if (io > 0) stop "*** error opening errors.txt ***"
  call random_seed()
  do i = 1, 3
    n = dimensions(i)
    if (n < 10) then
      write(output_file, "(a6, i1, a4)") "errors", n, ".txt"
    else
      write(output_file, "(a6, i2, a4)") "errors", n, ".txt"
    end if
    open (unit = wunit, file = output_file, action = "write", &
          status = "unknown", position = "rewind", iostat = io)
    if (io > 0) stop "*** error opening errors.txt ***"
    ref = (2./3.)**n
    do m = 2, max_divisions(i)
      mc = monte_carlo(m, n)
      mp = midpoint(m, n)
      ! write to command line (*) and to the file (wunit)
      write (0, '(i10, es16.6, es16.6)') m, abs(mc-ref)/ref, abs(mp-ref)/ref
      write (wunit, '(i10, es16.6, es16.6)') m, abs(mc-ref)/ref, abs(mp-ref)/ref
    end do
    close (unit = wunit)
  end do
  
contains

double precision function monte_carlo(m, n)
!------------------------------------------------------------------------------!
! Integrate the function by Monte Carlo.
!------------------------------------------------------------------------------!
  integer, intent(in) :: m ! number of divisions per dimension
  integer, intent(in) :: n ! number of dimensions
  double precision, allocatable, dimension(:) :: x ! n-dimensional point
  integer :: dart, size_seed
  double precision :: a, f
  allocate(x(n))
  monte_carlo = 0.0
  do dart = 1, m**n
    call random_number(x)
    !call random_number(a)
    !if (a <= fun(n, x)) then
    !  monte_carlo = monte_carlo + 1.0
    !end if
    monte_carlo = monte_carlo + fun(n, x)
  end do
  monte_carlo = monte_carlo / m**n
  deallocate(x)
end function monte_carlo

double precision function midpoint(m, n)
!------------------------------------------------------------------------------!
! Integrate the function by the midpoint rule.
!------------------------------------------------------------------------------!
  integer, intent(in) :: m ! number of divisions per dimension
  integer, intent(in) :: n ! number of dimensions
  double precision, allocatable, dimension(:) :: x ! n-dimensional point
  double precision :: volume ! "volume" of a cell
  integer :: cardinal ! cardinal index
  allocate(x(n))
  midpoint = 0.0_8
  volume = (1.0/dble(m))**n
  do cardinal = 1, m**n ! we have n dimensions each with m divisions
    call get_point(cardinal, m, n, x)
    midpoint = midpoint + fun(n, x) * volume
  end do
  deallocate(x)
end function midpoint

double precision function fun(n, x)
!------------------------------------------------------------------------------!
! Evaluate the function at the n-dimensional point x
!------------------------------------------------------------------------------!
  integer, intent(in) :: n
  double precision, dimension(:), intent(in) :: x
  integer :: i
  fun = 0.0_8
  do i = 1, n
    fun = fun + x(i)
  end do
  fun = fun**2
end function fun

subroutine get_point(cardinal, m, n, x)
!------------------------------------------------------------------------------!
! Given the cardinal index, the number of points per axis, and the dimension,
! compute the point x in n-dimensional space.
!------------------------------------------------------------------------------!
  integer, intent(in) :: cardinal ! cardinal index
  integer, intent(in) :: m        ! number divisions per dimension
  integer, intent(in) :: n        ! number of dimensions
  double precision, dimension(:), intent(out) :: x ! n-dimensional point
  double precision :: delta ! mesh width
  integer, allocatable, dimension(:) :: indices  ! i, j, k, ...
  integer :: i
  allocate(indices(n))
  call get_indices(cardinal, m, n, indices)
  delta = 1.0 / dble(m)
  do i = 1, n
    x(i) = (indices(i) - 0.5) * delta
  end do
  deallocate(indices)
end subroutine get_point

subroutine get_indices(cardinal, m, n, indices)
!------------------------------------------------------------------------------!
! In order to implement the midpoint rule for arbitrary dimension, we use
! a cardinal index that we can map to the i, j, k, ... indices in each of
! n dimensions.  This allows a quick computation of the n-dimensional
! point in n-space and, hence, quick evaluation of the function at that point.
!------------------------------------------------------------------------------!
  integer, intent(in)                :: cardinal ! cardinal index
  integer, intent(in)                :: m        ! number of divisions per axis
  integer, intent(in)                :: n        ! dimension of problem
  integer, intent(out), dimension(:) :: indices  ! i, j, k, ...
  integer :: i, j, s
  indices = 0
  do i = 1, n
    s = 0
    do j = 1, i-1
      s = s + indices(j) * m**(n-j)
    end do
    indices(i) = (cardinal - 1 - s) / m**(n-i)
  end do
  indices = indices + 1
end subroutine get_indices

end program integrate
