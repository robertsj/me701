program control
  integer :: a = 1
  select case (a)
    case (1)
      print *, "a = 1"
    case (2)
      print *, "a = 2"
    case default
      print *, "a < 1 || a > 2"
 end select
end program control
