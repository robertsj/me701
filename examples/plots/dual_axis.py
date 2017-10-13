import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

def normal(x, sigma, mu):
    return np.sqrt(1/2/np.pi/sigma**2) * np.exp(-(x-mu)**2/2/sigma**2)
    

x = np.linspace(-10, 10, 100)
y = normal(x, 1, 1)
Y = np.array([quad(lambda z: normal(z, 1, 1), -10, i)[0] for i in x])

plt.figure(1)
plt.plot(x, y, label='f(x)')
plt.plot(x, Y, 'r', label='F(x)')
plt.xlabel('x')
plt.legend()


plt.figure(2)
fig, ax1 = plt.subplots()
ax1.plot(x, y, 'b', label='pdf')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(x, Y, 'r')
ax2.set_ylabel('F(x)', color='r')
ax2.tick_params('y', colors='r')
