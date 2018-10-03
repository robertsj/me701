import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nice_plots import init_nice_plots
init_nice_plots()

def get_xy(t):
    a = 0.15
    b = 0.03
    x = a * np.cos(t)*np.exp(b*np.linspace(0,150,1000))
    y = a * np.sin(t)*np.exp(b*np.linspace(0,150,1000))
    return x, y
    
def updatefig(*args):
    global t
    t += 1
    x, y = get_xy(t)
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw()
    return line,
    
t = np.linspace(0,40,1000)
x, y = get_xy(t)
    
fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([-10,10,-10,10])
line, = ax.plot(x, y)
    
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
