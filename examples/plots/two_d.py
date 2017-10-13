import numpy as np
import matplotlib.pyplot as plt


n = 100
x = np.linspace(0, 1, n)
y = np.linspace(0, 1,n)
xx, yy = np.meshgrid(x, y)
f = np.sin(xx*yy)

# compute gradient, but on small grid
n = 12
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
xxx, yyy = np.meshgrid(x, y)
dfdx = yyy*np.cos(xxx*yyy)
dfdy = xxx*np.cos(xxx*yyy)

# plot both
plt.figure(1)
plt.contourf(xx, yy, f, cmap='jet')
plt.quiver(xxx, yyy, dfdx, dfdy, color='white')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,1,0,1])
plt.savefig('two_d_jet.png')

# plot both
plt.figure(2)
plt.contour(xx, yy, f, 10)
plt.streamplot(xxx, yyy, dfdx, dfdy)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,1,0,1])

