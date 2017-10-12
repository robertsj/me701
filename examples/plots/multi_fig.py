import matplotlib.pyplot as plt
import numpy as np

from nice_plots import init_nice_plots
init_nice_plots()

plt.figure(1)

x = np.linspace(0, 5, 100)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))

ax[0, 0].plot(x, y)
ax[0, 0].set_xlabel('$x$')
ax[0, 0].set_ylabel('$\sin(x)$')

ax[0, 1].plot(x, z)
ax[0, 1].set_xlabel('$x$')
ax[0, 1].set_ylabel('$\cos(x)$')

ax[1, 0].plot(x, y**2)
ax[1, 0].set_xlabel('$x$')
ax[1, 0].set_ylabel('$\sin^2(x)$')

ax[1, 1].plot(x, z**2)
ax[1, 1].set_xlabel('$x$')
ax[1, 1].set_ylabel('$\cos^2(x)$')

plt.tight_layout()
plt.show()