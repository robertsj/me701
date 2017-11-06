import class_cpp_demo
import numpy as np

a = np.array([1.0, 1.0, 1.0])
p = class_cpp_demo.Polynomial(a)
print(p)
print(p.eval(1.0))


