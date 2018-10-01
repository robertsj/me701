import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nice_plots import init_nice_plots
init_nice_plots()

N = 30
dx = 1.0 / N

T = np.ones((N,N))

def update_T(T):
    k = 0
    while k < 100:
        for i in range(1,N-1):
            for j in range(1,N-1):
                T[i,j] = 0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1]+dx**2)
        yield T
        k += 1
    
def time_dep(T):
    data = []
    for temp in update_T(T):
        data.append(temp.copy())
    return np.array(data)

def make_2D_imshow(data):
    im = []
    for i in range(len(data)):
        plot = plt.imshow(data[i])
        im.append((plot,))
    fig = plt.figure(0)
    ani = animation.ArtistAnimation(fig, im, interval=100, blit=True)
    plt.show()
    
make_2D_imshow(time_dep(T))
