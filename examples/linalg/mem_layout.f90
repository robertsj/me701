program mem_layout
  implicit none
  double precision :: A(0:2, 0:2), k
  integer :: i, j
  k = 0_8
  do i = 0, 2
      do j = 0, 2
          A(i, j) = k
          k = k + 1_8
      end do
  end do
  print '(f6.2)', A
end program mem_layout
   
