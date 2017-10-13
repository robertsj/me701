"""Goal: show 1-D diffusion"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

def live_animation():
    # number particles
    n = 1000
    # initialize particle positions
    x = (np.random.rand(n)*2-1)/2
    y = np.random.rand(n)
    # set up live
    plt.ion()
    plt.show()
    for i in range(200):
        # shift x randomly left or right by 0.1
        if i > 0 :
            x += 0.25*(-1+2*np.random.randint(0, 2, n))
        plt.figure(1)
        plt.clf()
        plt.plot(x, y, 'ko', ms=3)
        plt.title('step = {}'.format(i))
        plt.axis([-5, 5, 0, 1])
        plt.draw()
        plt.pause(0.1)
   
def saved_animation():
    import matplotlib.animation as animation

    # number particles
    n = 1000
    # initialize particle positions
    x = (np.random.rand(n)*2-1)/2
    y = np.random.rand(n)
    
    fig, ax = plt.subplots()
    line, = plt.plot([], [], 'ko', ms=3, animated=True)  
    
    ax.set_xlabel('x')
    ax.axis([-5, 5, 0, 1])
    
    def update(step, x, y):
        # shift x randomly left or right by 0.1
        if step > 0 :
            x += 0.25*(-1+2*np.random.randint(0, 2, n))
        plt.title('step {}'.format(step))
        print('step = ', step, x[0])
        line.set_data(x, y)
    
        return line,
    
    ani = animation.FuncAnimation(fig, update, 
                                  fargs=(x, y), 
                                  frames=range(0, 200), 
                                  blit=True, interval=100, repeat=False)
    ani.save('diffusion.mp4', fps=15)

    plt.show()
    
#live_animation()
saved_animation()

