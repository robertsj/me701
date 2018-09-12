import unittest
import root_finder
import math

class TestRootFinder(unittest.TestCase):
    
    def test_bisection_quadratic(self):
        """ Tests solution of (x-1)^2 given the range [0, 2].
        """
        
        f = lambda x: (x-1)**2-2
        L, R = 0.0, 4.0
        tolerance = 1e-8 
        expected = 2.4142135623730951
        got = root_finder.bisection(f, L, R, tolerance)
        self.assertAlmostEqual(expected, got, places=7,
                               msg='expected {:.8f} but got {:.8f}')
        
      
        
if __name__ == '__main__':
    
    unittest.main()