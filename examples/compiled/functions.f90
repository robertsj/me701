program functions
  interface add
    real function add_d(x, y)
      real, intent(in) :: x, y
    end function add_d
    integer function add_i(x, y)
      integer, intent(in) :: x, y
    end function add_i
  end interface
  print *, add(1, 2)
  print *, add(1.0, 2.0) !!!
end program functions
real function add_d(x, y)
  real, intent(in) :: x, y
  print *, "add reals"
  add_d = x + y
end function add_d
integer function add_i(x, y)
  integer, intent(in) :: x, y
  print *, "add ints"
  add_i = x + y
end function add_i
