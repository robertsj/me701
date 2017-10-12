import matplotlib.pyplot as plt
import numpy as np


plt.figure(1)
x = np.linspace(0, 5, 100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, x, z)
plt.savefig('basic_plot.pdf')

from nice_plots import init_nice_plots
init_nice_plots()

plt.figure(2)
plt.plot(x, y, 'k-', label='$\sin(x)$')
plt.plot(x, z, 'b-.', label='$\cos(x)$')
plt.xlabel('$x$')
plt.legend()
plt.savefig('basic_plot_nice.pdf')


plt.figure(3)
plt.plot(x, y, 'k-')
plt.plot(x, z, 'b-.')
plt.xlabel('$x$')
plt.annotate('$\sin(x)$', (3, 0.25), color='k', size=16)
plt.annotate('$\cos(x)$', (1.5, 0.25), color='b', size=16)
plt.savefig('basic_plot_nice_annotate.pdf')