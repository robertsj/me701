program command_line
 implicit none
 character(80)  :: s
 integer :: n = 1, io
 if (command_argument_count() &
     .lt. 1) then
  stop "usage: a.out <arg>"
 else
  call get_command_argument(1,s)
  print *, "s = ", s
  read (s, *, iostat=io) n
  if (io .ne. 0) n = 0
  print *, "n = ", n
  end if
end program command_line
