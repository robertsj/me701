program control
  integer :: a = 1
  if (a == 1) then
    print *, "a = 1"
  else if (a == 2) then
    print *, "a = 2"
  else
    print *, "a < 1 || a > 2"
  end if
  if (a == 1) print *, "hi"
end program control
