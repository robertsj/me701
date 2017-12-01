program hello_world
use omp_lib
implicit none
integer :: i, n
real(8) :: s, s_tmp, t
t = omp_get_wtime()
!$omp parallel private(i, s_tmp) &
!$omp   shared(s)
s = 0.0_8
s_tmp = 0.0_8
n = 2e7
!$omp do
do i = 1, n
  s_tmp = s_tmp + dble(i)
end do
!$omp end do
!$omp atomic
s = s + s_tmp
!$omp end parallel
t = omp_get_wtime() - t
write (*,"(f16.0, es10.2)") s, t
end program hello_world
