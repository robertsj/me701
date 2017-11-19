! gaussian elimination

! Solve Ax = b using very simple gaussian elimination 
subroutine dgesv(n, nrhs, A, lda, ipiv, b, ldb, info)
  ! Inputs:
  !        n    - system size
  !     nrhs    - n/a
  !        A    - n x n array 
  !     ipiv    - n/a
  !        b    - n x 1 array.  starts as b, ends as solution.
  !      ldb    - n/a
  !     info    - n/a
  implicit none
  integer, intent(in) :: n, nrhs, lda, ldb
  integer, intent(out) :: info, ipiv(n)
  double precision, dimension(:, :), intent(inout) :: A(n, n)
  double precision, dimension(:), intent(inout) :: b(n)
  ! Local Variables:
  integer :: i, j, k
  double precision :: temp
  info = 0
  ! loop over all rows
  do k = 1, n-1         
      ! do all rows below the pivot.
      do i = k+1, n    
          ! protect against divide by zero
          if (abs(A(k, k)) .le. 1D-16) stop "zero on diagonal"
          temp = A(i, k) / A(k, k)            
          A(i, k+1:n) = A(i, k+1:n) - A(k, k+1:n) * temp
          b(i) = b(i) - temp * b(k)      
          ! lower triangle is filled with zeros
          A(i, k) = 0.0_8  
      end do
  end do   
  ! backsubstitute to get solution
  do i = n, 1, -1     
      temp = b(i)         
          do j = i+1, n            
              temp = temp - A(i, j) * b(j)         
          end do         
      b(i) = temp / A(i, i)      
  end do
end subroutine dgesv
  
  
