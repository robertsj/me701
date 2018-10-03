import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from nice_plots import init_nice_plots
init_nice_plots()

N = 25
dx = 1.0 / N

T = np.zeros((N,N))

# Make initial plot
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
    
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
X, Y = np.meshgrid(x, y)

ax.plot_surface(X, Y, T)

def update_plot(T, k):
    T = update_T(T)
    plt.cla()
    ax.plot_surface(X, Y, T, cmap='viridis')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Iteration {}'.format(k))
    ax.set_zlim([0, 6])
    plt.draw()
    plt.pause(0.01)

def update_T(T):
    # One sweep of the poison distribution after finite difference
    # d/dx(df/dx) + d/dy(df/dy) = 100
    # The boundary is set to zero, source to 100
    for i in range(1,N-1):
        for j in range(1,N-1):
            T[i,j] = 0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1]+dx**2 * 100)
    return T

for k in range(200):
    update_plot(T, k)

