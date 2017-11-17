program triad

implicit none

integer, parameter :: N = 1000, R = 1000000
integer :: i, j
double precision :: A(N), B(N), C(N), D(N)
double precision :: omp_get_wtime, t0, te

do i = 1, N
  A(i) = 0_8
  B(i) = 1_8
  C(i) = 2_8
  D(i) = 3_8
end do

t0 = omp_get_wtime()

do j = 1, R
  do i = 1, N
    A(i) = B(i) + C(i)*D(i)
  end do
  if (A(5) .lt. 0) call dummy(A, B, C, D, n)
end do

te = omp_get_wtime() - t0

print '(a e20.4)', "Elapsed time = ", te, " seconds"
print '(a f20.16)', "MFLOPS/s = ", (R*N*2)/te/1d6
print *, (R*N*2)/te/1d6

end program triad

subroutine dummy(A, B, C, D, n)
  integer :: n
  double precision :: A(n), B(n), C(n), D(n)
  ! do nothing!
end subroutine dummy
