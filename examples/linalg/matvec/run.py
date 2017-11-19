import os
import numpy as np
import matplotlib.pyplot as plt

# Things I like to use for nicer plots.
from matplotlib import rc
rc('font',**{'family':'serif'})
from matplotlib import rcParams
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams.update({'figure.autolayout': True})
 
#os.system('./driver-mv-row-x > out_row') 
#os.system('./driver-mv-col-x > out_col')
#os.system('./driver-mv-blas-x > out_blas') 
#os.system('./driver-mv-mkl-x > out_mkl') 

row = np.loadtxt('out_row').transpose()
col = np.loadtxt('out_col').transpose()
blas = np.loadtxt('out_blas').transpose()
mkl = np.loadtxt('out_mkl').transpose()

plt.plot(row[0], row[1], 'k-o',
         col[0], col[1], 'b-h',
         blas[0],  blas[1],  'r-*',
         mkl[0],  mkl[1],  'g-^')
plt.legend(['row', 'column', 'blas', 'mkl'], loc=0, numpoints=1)
plt.xlabel('matrix dimension')
plt.ylabel('Mflops')
plt.grid(True)
plt.show()
