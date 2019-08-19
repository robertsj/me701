import simple_f90_demo
import numpy as np

# testing bigger
a = 1
b = 2
print(simple_f90_demo.bigger(a, b))

# testing norm
a = np.array([1, -2, 3], dtype='float64') 
print(simple_f90_demo.norm(a, 99))

# testing range
print(simple_f90_demo.range(5, 5))

