import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nice_plots import init_nice_plots
init_nice_plots()

def f(x):
    return np.sin(x)

x = np.linspace(0, 2 * np.pi, 120)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, f(x))

def updatefig(*args):
    global x
    x += np.pi / 15.
    line.set_ydata(f(x))
    fig.canvas.draw()
    return line,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
#ani.save('name.mp4', writer='avconv')
plt.show()
