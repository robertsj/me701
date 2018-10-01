import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nice_plots import init_nice_plots
init_nice_plots()

def get_xy(t):
    a = 0.5
    b = 0.05
    x = a * np.cos(t)*np.exp(b*t)
    y = a * np.sin(t)*np.exp(b*t)
    return x, y
    
def updatefig(*args):
    global t_max
    t_max += 1
    x, y = get_xy(np.linspace(0,t_max,1000))
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw()
    return line,
    
t_max = 0
x, y = get_xy(np.linspace(0,t_max,1000))
    
fig = plt.figure()
ax = fig.add_subplot(111)
plt.axis([-10,10,-10,10])
line, = ax.plot(x, y)
    
ani = animation.FuncAnimation(fig, updatefig, interval=0, blit=True)
plt.show()
