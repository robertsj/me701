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


# Option One -- Using std::vector
# T = cpp_demo.vec_dbl(10, 0.0)
# cpp_demo.compute_temperature_vector(T)
# print T
# print np.asarray(T)

# Option Two -- Using array (enclosed in a class)
"""
D = cpp_demo.ProblemData()
cpp_demo.initialize(D, 10)
cpp_demo.compute_temperature_array(D)
a = cpp_demo.numpy_temp(D)
print(D.T)
print(a)
cpp_demo.finalize(D)
"""
