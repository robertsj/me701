import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import minimize

x = np.linspace(0, 1, 100)
y = np.sin(x)

def error_lin(c, x, y_ref, p):
    """ c are the unknown coefficients
        x is the independent variable
        y_ref is the reference dependent variable
        
        returns ||y_model - y_ref||_p
    """
    
    a, b = c[0], c[1]
    
    y_model = a*x + b
    
    error = y_model - y_ref
    
    return np.linalg.norm(error, ord=p)
