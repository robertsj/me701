import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

x = np.linspace(0, 1, 100)
y = np.sin(x) #+ np.random.rand(len(x))*0.1

# y_lin = ax+b
A = np.column_stack((x**0, x**1))
AtA = A.T@A
Aty = A.T@y

x_lin = np.linalg.solve(AtA, Aty)
y_lin = A@x_lin
plt.plot(x, y, x, y_lin)


# y_quad = ax^2 + bx + c


# y_sin = a*sin(x) + b