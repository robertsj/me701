subroutine dgemv(trans, m, n, alpha, A, lda, x, incx, beta, y, incy)
! Simplified DGEMV that does
!     y := A*x
! We follow the BLAS signature for compatibility.  For more,
! see http://netlib.org/blas/.
  implicit none
  ! input/output
  character*1, intent(in)         :: trans
  integer, intent(in)             :: m, n, lda, incx, incy
  double precision, intent(in)    :: alpha, beta
  double precision, intent(in)    :: A(m, n)
  double precision, intent(in)    :: x(n)
  double precision, intent(inout) :: y(m)
  ! local
  integer :: i, j
  ! do y = A*x
  do i = 1, n
    do j = 1, n
      y(i) = y(i) + A(i, j) * x(j)
    end do
  end do
end subroutine dgemv
