! Driver program to test matrix-matrix multiplication
program test_matrix_matrix
  implicit none
  double precision, allocatable, dimension(:, :) :: A, B, C
  double precision :: alpha = 1.0, beta = 0.0, t, t2, omp_get_wtime, flops
  integer :: n, m, k, lda, ldb, ldc, i, j, maxi = 1000, ii
  character*1 :: transa = 'n', transb = 'n'
  do j = 1, 25
    ! Matrix size
    m   = 10 * 4 * j
    n   = m
    k   = m
    lda = m
    ldb = m
    ldc = m
    ! Create the matrix and vector
    allocate(A(m, n), B(m, n), C(m, n))
    ! Initialize A and x
    A = 1.0_8
    B = 1.0_8
    ! Start the timer.
    t = omp_get_wtime()
    ! Loop over and apply A several times for consistent timing
    ii = 0
    do i = 1, maxi
      ! Reset
      C = 0_8
      call dgemm(transa, transb, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc)
      t2 = omp_get_wtime()-t
      ii = ii + 1
      if (t2 > 0.2) exit
    end do
    if (C(1, 1) .ne. n) stop "bad result. stop."
    t2 = omp_get_wtime()-t
    ! we should subtract m for our own implementation, since
    ! we don't do y = Ax-y, just y = Ax
    !flops = (2*m*m*m)*maxi
    flops = 2_8*m**3*ii
    print '(i4, f20.4)', m,  flops / dble(1e6) / t2
    deallocate(A, B, C)
  end do
end program test_matrix_matrix
