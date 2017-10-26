program loops
  integer :: i, j
  j = 0
  do i = 1, 100
    j = j + i
  end do
  i = 1
  j = 0
  do while (i < 100)
     j = j + i
     i = i + 1
  end do
end program loops
