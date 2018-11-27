import numpy as np
import matplotlib.pyplot as plt

x, y, T = np.loadtxt('temperatures.txt', unpack=True)

n = int(np.sqrt(len(x)))

x = x.reshape((n, n))
y = y.reshape((n, n))
T = T.reshape((n, n))

plt.contourf(x, y, T, cmap='inferno')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.title('temperatures')

plt.show()
