program sum_parallel
  implicit none
  integer*8, parameter :: &
    n = 100000000
  integer :: i
  real*8 :: s, s_ref
  real*8, allocatable, &
    dimension(:) :: v
  allocate(v(n))
  do i = 1, n
    v(i) = dble(i-1)
  end do
  !$omp parallel do
  do i = 1, n
    !$omp atomic
    s = s + v(i)
  end do
  !$omp end parallel do
  s_ref = 0.5_8*(n*n-n)
  print *, "sum is ", s, &
    " expected ", s_ref
  deallocate(v)
end program sum_parallel
