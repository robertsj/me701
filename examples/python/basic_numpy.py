import numpy as np
import matplotlib.pyplot as plt

#%% This is a cell.  It can be executed independently.

x = np.linspace(0, 3, 50)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, x, z)


#%% Another cell

y = x.copy()
xx, yy = np.meshgrid(x, y)
zz = 1 - xx**2 - yy**2


plt.contourf(xx, yy, zz)


# now, visualize the gradient!