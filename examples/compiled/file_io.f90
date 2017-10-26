program file_io
  integer :: i, n
  real,allocatable :: T(:), rho(:)
  n = num_lines("data.txt")
  allocate(T(n), rho(n))
  open (unit=5, file="data.txt", &
        action="read")
  do i = 1, n
   read(5, *) T(i), rho(i)
  end do
end program file_io

integer function num_lines(s)
  character(len=*) :: s
  integer :: io=0
  num_lines=0
  open(unit=5,file=s,action="read")
  do while (1 .eq. 1)
    read(5, *, iostat=io)
    if (io < 0) exit
    num_lines = num_lines + 1
  end do
  close(unit=5)
end function num_lines
