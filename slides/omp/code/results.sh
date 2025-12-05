[robertsj@vainamoinen code]$ time ./t1_c 
sum is 4999999950000000.000000, expected 4999999950000000.000000

real	0m0.313s
user	0m0.154s
sys	0m0.158s
[robertsj@vainamoinen code]$ export OMP_NUM_THREADS=4; time ./t1_c 
sum is 937740299046415.000000, expected 4999999950000000.000000

real	0m0.239s
user	0m0.227s
sys	0m0.148s
[robertsj@vainamoinen code]$ export OMP_NUM_THREADS=1; time ./t2_c 
sum is 4999999950000000.000000, expected 4999999950000000.000000

real	0m1.800s
user	0m1.641s
sys	0m0.156s
[robertsj@vainamoinen code]$ export OMP_NUM_THREADS=4; time ./t2_c 
sum is 4999999950000000.000000, expected 4999999950000000.000000

real	0m6.980s
user	0m23.346s
sys	0m0.158s
[robertsj@vainamoinen code]$ export OMP_NUM_THREADS=1; time ./t3_c 
sum is 4999999950000000.000000 expected 4999999950000000.000000
etime 0.112994

real	0m0.308s
user	0m0.148s
sys	0m0.157s
[robertsj@vainamoinen code]$ export OMP_NUM_THREADS=4; time ./t3_c 
sum is 4999999950000000.000000 expected 4999999950000000.000000
etime 0.040075

real	0m0.237s
user	0m0.199s
sys	0m0.160s

