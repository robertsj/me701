import module_f90_demo
import numpy as np

a = np.array([1.0, 1.0, 1.0])

module_f90_demo.polynomial.initialize(a)

print(module_f90_demo.polynomial.eval(1.0))

module_f90_demo.polynomial.finalize()

