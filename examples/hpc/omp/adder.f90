program hello_world
use omp_lib
implicit none
integer :: i, n
real(8) :: s, s_tmp
!$omp parallel private(i, s_tmp) shared(s)
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
write (*,"(f16.0)") s
end program hello_world
