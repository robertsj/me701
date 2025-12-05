program hello_world
use omp_lib
implicit none
integer :: nt, id
!$omp parallel
nt = omp_get_num_threads()
id = omp_get_thread_num()
print *, "hello world from ", &
         id, " of ", nt
!$omp end parallel
end program hello_world
