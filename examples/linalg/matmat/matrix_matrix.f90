subroutine dgemm(transa, transb, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc)
! Simplified DGEMM that does
!     C := A * B
! We follow the BLAS signature for compatibility.  For more,
! see http://netlib.org/blas/.
!
! C = m * n
  implicit none
  ! input/output
  character*1, intent(in)         :: transa, transb
  integer, intent(in)             :: m, n, k, lda, ldb, ldc
  double precision, intent(in)    :: alpha, beta, A(m, n), B(n, k)
  double precision, intent(inout) :: C(m, k)
  ! local
  integer :: i, j, h
  ! do y = A*x
!  do i = 1, m
!    do j = 1, k
!      do h = 1, n
!        C(i, j) = C(i, j) + A(i, h) * B(h, j)
!      end do
!    end do
!  end do
  do j = 1, m
    do h = 1, k
      do i = 1, n
        C(i, j) = C(i, j) + A(i, h) * B(h, j)
      end do
    end do
  end do
end subroutine dgemm
