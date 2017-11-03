module basic_arrays_module

implicit none

! module-wide variable declarations, et.c
integer, parameter :: m = 5
double precision, allocatable, dimension(:, :) :: a2

contains

subroutine pass_array_1(a)
    double precision, dimension(:) :: a
    ! do something with the array
    print  '(f6.2)', a(2)
    ! change an element
    a(2) = 99 
end subroutine pass_array_1

subroutine pass_array_2(a)
    double precision, dimension(:), intent(out) :: a
    ! do something with the array
    print  '(f6.2)', a(2)
    ! change an element
    a(2) = 101 
end subroutine pass_array_2

subroutine pass_array_3(a)
    double precision, dimension(:), intent(inout) :: a
    ! do something with the array
    print  '(f6.2)', a(2)
    ! change an element
    a(2) = 103
end subroutine pass_array_3

end module basic_arrays_module
