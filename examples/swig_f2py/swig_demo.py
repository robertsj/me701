import simple_cpp_demo
import numpy as np

# testing bigger
a = 1
b = 2
print(simple_cpp_demo.bigger(a, b))

# testing norm
a = np.array([1, -2, 3], dtype='float64') 
print(simple_cpp_demo.norm(a, 2))

# testing range
print(simple_cpp_demo.range(5, 5))

# testing add_ab
a = np.array([1, 2, 3], dtype='float64') 
b = np.array([2, 4, 5], dtype='float64')  
print(simple_cpp_demo.add_ab(a, b))
