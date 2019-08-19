import unittest
import root_finder

class TestRootFinder(unittest.TestCase):
    
    def test_bisection_quadratic(self):
        """ Tests solution of (x-1)^2-2 given the range [0, 4].
        """
        
        f = lambda x: (x-1)**2-2
        L, R = 0.0, 4.0
        tolerance = 1e-8 
        expected = 1.4142135623730951 
        got = root_finder.bisection(f, L, R, tolerance)
        self.assertAlmostEqual(expected, got, places=7,
                               msg='expected {:.8f} but got {:.8f}'.format(expected, got))
        
      
        
if __name__ == '__main__':
    
    unittest.main()