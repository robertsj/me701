double precision function bigger(a, b)
    implicit none
    double precision, intent(in) :: a, b
    if (a > b) then
        bigger = a
    else
        bigger = b
    end if
end function bigger

double precision function norm(a, n, p)
    implicit none
    double precision, intent(in) :: a(n)
    integer, intent(in) :: n, p
    integer :: i
    do i = 1, n
        norm = norm + abs(a(i))**p
    end do
    norm = norm**(1.0_8/p)
end function norm

subroutine range(a, n, start)
    implicit none
    double precision, intent(out) :: a(n)
    integer, intent(in) :: n, start
    integer :: i
    do i = 1, n
        a(i) = start + i - 1
    end do
end subroutine range
