program sum_parallel
  use omp_lib
  implicit none
  integer*8, parameter :: &
    n = 100000000
  integer :: i
  real*8 :: s, s_ref, s_p, et
  real*8, allocatable, &
    dimension(:) :: v
  allocate(v(n))
  do i = 1, n
   v(i) = dble(i-1)
  end do
  et = omp_get_wtime()
  !$omp parallel           &
  !$omp   default(private) &
  !$omp   shared(s, v)
  !$omp do
  do i = 1, n
    s_p = s_p + v(i)
  end do
  !$omp end do
  !$omp atomic
  s = s + s_p
  !$omp end parallel
  et = omp_get_wtime()-et
  s_ref = 0.5_8*(n*n-n)
  print *, "sum is ", s, &
    " expected ", s_ref
  print "(a, f8.6)", "etime ", et
  deallocate(v)
end program sum_parallel
