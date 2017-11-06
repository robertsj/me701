module polynomial

implicit none

double precision, allocatable, dimension(:) :: a_
integer :: n_

contains

subroutine initialize(a, n)
    double precision, intent(in) :: a
    integer, intent(in) :: n
    allocate(a_(n))
    a_ = a 
    n_ = n
end subroutine initialize

subroutine finalize()
    if (allocated(a_)) then
        deallocate(a_)
    end if
end subroutine finalize

double precision function eval(x)
    double precision, intent(in) :: x
    integer :: i
    eval = 0_8
    do i = 1, n_
        eval = eval + a_(i)*x**i
    end do
end function eval

end module polynomial
