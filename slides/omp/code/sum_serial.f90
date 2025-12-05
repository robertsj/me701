program sum_serial
implicit none
integer*8, parameter :: &
 n = 100000
integer :: i
real*8 :: s, s_ref, v(n)
do i = 1, n
  s = s + (i-1)
end do
s_ref = 0.5_8*(n*n- n)
print *, "sum is ", s, &
         " expected ", s_ref
end program sum_serial
