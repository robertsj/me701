"""
Root finder - a module with functions to find roots.
"""

def sign(x):
    return x > 0

def bisection(f, L, R, tolerance=1e-6, max_it=1000):
    C = (L+R)/2
    it = 0
    while f(C) < tolerance:
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
    pass