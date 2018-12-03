"""
Exercise 6 -  2-D Heat Transfer
"""

import numpy as np
import matplotlib.pyplot as plt

from mpi4py import MPI
comm = MPI.COMM_WORLD

# Get rank and size
rank = comm.Get_rank()
size = comm.Get_size()

def solve(q, k, n):

  Delta = 1.0/(n-1)

  # Initialize temperature (with BC's)
  T = np.zeros((n, n))
  for i in range(n): 
      T[i, n-1] = 1.0
  T_old = T.copy()

  # Jacobi
  r = 1.0
  it = 0
  while r > 1e-4 and it < 100:

      # Swap
      T_old, T = T, T_old

      # Update temperatures
      for i in range(1, n-1): 
          for j in range(1, n-1):
              tmp = 0.25*(T_old[i+1,j]+T_old[i-1,j]+T_old[i,j+1]+T_old[i,j-1])
              T[i, j] = tmp + Delta*Delta/k/4.0*q;
      
      # Compute residual and update counter
      r = np.linalg.norm(T-T_old, 2)
      it += 1

  return T

def plot_temperature(n, T):
    x = np.linspace(0, 1, n)
    y = x.copy()
    xx, yy = np.meshgrid(x, y)
    plt.contourf(xx, yy, T.T, cmap='inferno')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == "__main__":


    q = 0   # heat generation rate
    k = 1   # conductivity
    n = 100 # number of cells per dimension

    T = solve(q, k, n)
    
    plot_temperature(n, T)

