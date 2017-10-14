import numpy as np
import matplotlib.pyplot as plt

plt.ioff()
exp = np.exp 

def Q(rho_e, rho_h) :
    return rho_e + rho_e**2*(exp(-1.0/rho_e)-1.0) + \
           rho_h + rho_h**2*(exp(-1.0/rho_h)-1.0)
    
def sig_Q(rho_e, rho_h) :
    a = rho_e**2 + 2.*rho_e**3*(exp(-1.0/rho_e)-1) + \
        0.5*rho_e**3*(1-exp(-2.0/rho_e))
    b = rho_h**2 + 2.*rho_h**3*(exp(-1.0/rho_h)-1) + \
        0.5*rho_h**3*(1-exp(-2.0/rho_h))
    c = 2.*rho_e*rho_h + 2.*rho_e**2*rho_h*(exp(-1.0/rho_e)-1) + \
        2.*rho_h**2*rho_e*(exp(-1.0/rho_h)-1)
    d = 2.*(rho_e*rho_h)**2/(rho_e-rho_h)*(exp(-1.0/rho_e)-exp(-1.0/rho_h))
    return np.sqrt( a+b+c+d-Q(rho_e,rho_h)**2)
   
def R(rho_e, rho_h) :
    return 100*sig_Q(rho_e, rho_h)/Q(rho_e, rho_h)
    
n = 100
H = np.logspace(-2, 2, n)
E = np.logspace(-2, 2, n) 

H, E = np.meshgrid(H, E, sparse=False, indexing='ij')
res = R(E, H)

plt.figure(1, figsize=(8,8))
plt.contour(np.log10(E),np.log10(H), res, colors='k')
plt.savefig('new_contour.png')
