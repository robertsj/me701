import numpy as np
import matplotlib.pyplot as plt

#%% This is a cell.  It can be executed independently.

x = np.linspace(0, 3, 50)
y = np.sin(x)
z = np.cos(x)

plt.figure(1)
plt.plot(x, y, 'r--', x, z)

def fun_thing(z):
    z[0] = 123
    return



#%% Another cell

y = x.copy()
xx, yy = np.meshgrid(x, y)
zz = 1 - xx**2 - yy**2
dzdx = -2*xx
dzdy = -2*yy

plt.figure(2)
plt.contourf(xx, yy, zz)
plt.colorbar()

plt.quiver(xx, yy, dzdx, dzdy, color='white')
plt.show()
# now, visualize the gradient!
