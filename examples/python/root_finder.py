"""
Root finder - a module with functions to find roots.
"""

def sign(x):
    return x > 0

def bisection(f, L, R, tolerance=1e-6, max_it=1000):
    """ Finds the root of a function using bisection.
    
    Inputs:
        f - function (callable) of one variable with one root
            in the range provided
    
    """
    C = (L+R)/2
    it = 0
    while abs(f(C)) > tolerance and it < max_it:
        if sign(f(L)) == sign(f(C)):
            # root is in right half
            L = C
        else:
            # root is in left half
            R = C
        # update center point and increment counter 
        C = (L+R)/2
        it += 1   
       
    return C

def newton():
    pass


if __name__ == '__main__':
    
    
    def fun(x):
        return x - 0.9