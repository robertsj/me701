import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nice_plots import init_nice_plots
init_nice_plots()

def make_data():
    return np.random.random((30,30))
    
def time_dep(f, t_max=100.0, dt=1.0):
    data = []
    for i in np.linspace(0,t_max,t_max/float(dt)):
        print(i)
        data.append(f())
    return np.array(data)

def make_2D_imshow(data):
    im = []
    for i in range(len(data)):
        plot = plt.imshow(data[i])
        im.append((plot,))
    fig = plt.figure()
    ani = animation.ArtistAnimation(fig, im, interval=100, blit=True)
    plt.show()
    
make_2D_imshow(time_dep(make_data))
