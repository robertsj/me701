# Error Bars Demo

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
#rcParams['font.serif'] = ['Times']
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['axes.edgecolor'] = 'white'
rcParams['xtick.bottom'] = True
rcParams['xtick.top'] = False
rcParams['ytick.left'] = True
rcParams['ytick.right'] = False
rcParams['axes.grid'] = False

np.random.seed(1234)
n = 50
x = np.linspace(0, 10, n)
y = x**2*(1 + np.random.normal(loc=0, scale=0.1, size=n))
#y = (x + np.random.normal(loc=0, scale=0.1, size=n))**2
# least squares on sqrt(y)
import scipy.stats
t = scipy.stats.t.ppf(0.95, len(x)-2)
z = np.sqrt(y)
a, b = np.polyfit(x, z, 1)
# confidence band
sx = np.sqrt(sum((z-np.mean(z))**2)/(len(z)-1))
sz = np.sqrt(sum((z-np.mean(z))**2)/(len(z)-2))
zcb = t * sz * np.sqrt(1/len(z) + (x-np.mean(x))**2/((n-1)*sx**2))

z_trend = a*x+b
zl = z_trend-zcb
zu = z_trend+zcb
yl = zl**2
yu = zu**2

plt.figure(1)
plt.plot(x, z_trend, 'b--')
plt.plot(x, z, 'k')
plt.plot(x, z_trend+zcb, 'r')
plt.plot(x, z_trend-zcb, 'r')
plt.fill_between(x, zl, zu, color='r', alpha=0.1)
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
#
plt.figure(2)
y_trend = (a*x+b)**2
plt.plot(x, y, 'k')
plt.plot(x, yu, 'r')
plt.plot(x, yl, 'r')
plt.fill_between(x, yl, yu, color='r', alpha=0.1)
plt.xlabel('x')
plt.ylabel('z')
plt.title('does this seem valid?')
plt.legend()
#
#
plt.figure(3)
zl2 = np.array([max(zl[i], 0) for i in range(len(zl))])
yl2 = zl2**2
plt.plot(x, (a*x+b)**2, 'b--')
plt.plot(x, y, 'k')
plt.plot(x, yu, 'r', alpha=0.5)
plt.plot(x, yl2, 'r', alpha=0.5)
plt.fill_between(x, yl2, yu, color='r', alpha=0.1)
plt.xlabel('x')
plt.ylabel('z')
plt.title('does this seem better?')
plt.legend()