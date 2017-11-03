! demonstration of basic arrays in Fortran
program basic_arrays

use basic_arrays_module

implicit none
integer, parameter :: n = 5
! a statically-sized array
double precision :: a(n)
! a dynamically-sized array
double precision, dimension(:), allocatable :: b
! loop variables
integer :: i, j, k

a = 1.0_8 ! yes, all at once
a(:) = 1.0_8 ! equivalent

allocate(b(n))
do i = 1, n
    b(i) = 2.0_8
end do

! How to pass arrays?
print 666, '           original value of b(2): ', b(2)
call pass_array_1(b)
print 666, ' value of b(2) after pass_array_1: ', b(2)
call pass_array_2(b)
print 666, ' value of b(2) after pass_array_2: ', b(2)
call pass_array_3(b)
print 666, ' value of b(2) after pass_array_3: ', b(2)
 
! what about 2-D arrays?
allocate(a2(3, 3))
a2 = reshape((/ 1, 2, 3, 4, 5, 6, 7, 8, 9 /), (/3, 3/))
print *, a2
print *, a2(1, 1), a2(2, 1)


666 format(a, f6.2)

end program basic_arrays


