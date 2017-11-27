program hello_omp

use omp_lib

implicit none

!$omp parallel
print *, "hey from thread ", &
         omp_get_thread_num(), & 
         " of ", &
         omp_get_num_threads()
!$omp end parallel

end program hello_omp
