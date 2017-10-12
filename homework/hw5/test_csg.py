"""
You may test your csg module by replace line 13 with the name of your
module, e.g., csg_template if you are using my template file directly.

This file is an example of a *unit-test suite*.  It is good practice to 
develop such a suite for a Python module.  The unittest module makes
this much easier, but it is not the only way.  In reality, a set of 
tests that *covers* all of the functions/methods of one's code is
the best way to avoid bugs (in the present and in the future).

"""

from csg import *
import unittest
import numpy as np

class TestCSG(unittest.TestCase) :

    def setUp(self) :
        pass

    #-------------------------------------------------------------------------#
    # TESTS OF POINT CLASS
    #-------------------------------------------------------------------------#

    def testPoint_translate(self) :        
        p0 = Point(1.0, 2.0)
        p1 = p0 + Point(2.0, 3.0)
        self.assertEqual(p1.x, 3.0)
        self.assertEqual(p1.y, 5.0)
    
    def testPoint_scale(self) :
        p0 = Point(1.0, 2.0)
        p1 = p0 * 2.0
        self.assertEqual(p1.x, 2.0)
        self.assertEqual(p1.y, 4.0) 
        
    #-------------------------------------------------------------------------#
    # TESTS OF SURFACE CLASSES
    #-------------------------------------------------------------------------#
    
    def testQuadraticSurface_f_plane(self) :
        
        # vertical plane at x = 3
        v = QuadraticSurface(D=1, F=-3)
        self.assertAlmostEqual(v.f(Point(1, 0)), -2)
        
        # create a circle of radius 2 centered at (2, 2)      
        c = QuadraticSurface(A=1, B=1, D=-4, E=-4, F=4)
        self.assertAlmostEqual(c.f(Point(0, 2)), 0.0)

    def testQuadraticSurface_intersections(self) :
        
        # ray starting at origin and with a direction of 45 degrees
        ray = Ray(Point(0, 0), Point(1, 1))
                
        # vertical plane at x = 3
        v = QuadraticSurface(D=1, F=-3)
        ints = v.intersections(ray)
        self.assertEqual(len(ints), 1)
        self.assertAlmostEqual(ints[0].x, 3)
        self.assertAlmostEqual(ints[0].y, 3)
                
        # create a circle of radius 2 centered at (2, 2)      
        c = QuadraticSurface(A=1, B=1, D=-4, E=-4, F=4)
        ints = c.intersections(ray)
        ints.sort(key=lambda p: p.x)
        self.assertEqual(len(ints), 2)
        self.assertAlmostEqual(ints[0].x, (np.sqrt(8)-2)*np.cos(np.pi/4))
        self.assertAlmostEqual(ints[0].y, (np.sqrt(8)-2)*np.sin(np.pi/4))     
        self.assertAlmostEqual(ints[1].x, (np.sqrt(8)+2)*np.sin(np.pi/4))
        self.assertAlmostEqual(ints[1].y, (np.sqrt(8)+2)*np.sin(np.pi/4))
        
    def testPlaneV(self) :
        v = PlaneV(3)
        self.assertEqual(v.D, 1)
        self.assertEqual(v.F, -3)
        
    def testPlaneH(self) :
        v = PlaneH(3)
        self.assertEqual(v.E, 1)
        self.assertEqual(v.F, -3)        

    def testPlane(self) :
        v = Plane(1, 1)
        self.assertEqual(v.D, -1)
        self.assertEqual(v.E, 1)
        self.assertEqual(v.F, -1)
        
    def testCircle(self) :
        c = Circle(1, 1, 1)
        self.assertEqual(c.A, 1)
        self.assertEqual(c.B, 1)
        self.assertEqual(c.D, -2)
        self.assertEqual(c.E, -2)
        self.assertEqual(c.F, 1)

    #-------------------------------------------------------------------------#
    # TESTS OF NODE CLASSES
    #-------------------------------------------------------------------------#
      
    def testPrimitive(self) :

        # unit circle centered at origin        
        c = Circle(1, 0, 0)
        
        # create node that represents the inside of the circle.  the 
        # "sense" argument specifies whether the node should represent
        # everything inside (true) or outside (false) of the surface.
        inside_c = Primitive(c, sense=True)
        self.assertTrue(inside_c.contains(Point(0, 0)))
        self.assertFalse(inside_c.contains(Point(2, 2)))
    
        outside_c = Primitive(c, sense=False)
        self.assertFalse(outside_c.contains(Point(0, 0)))
        self.assertTrue(outside_c.contains(Point(2, 2)))
        
    def get_circles(self) :
        # unit circle centered at origin
        c0 = Circle(1)
        # circle of radius two centered at the origin
        c1 = Circle(2)
        return c0, c1
        
    def testUnion_surface(self) :
        c0, c1 = self.get_circles()
        self.assertTrue(c0.f(Point(1.5, 0)) > 0.0)
        self.assertTrue(c1.f(Point(1.5, 0)) > 0.0)
        
    def testUnion_contains(self) :
        c0, c1 = self.get_circles()
        l, r = Primitive(c0, True), Primitive(c1, False)
        # everything outside c1 and inside c0
        u = Union(l, r)
        self.assertTrue(u.contains(Point(0, 0)))
        self.assertTrue(u.contains(Point(2, 0)))
        self.assertFalse(u.contains(Point(1.5, 0)))

    def testIntersection_contains(self) :
        
        c0, c1 = self.get_circles()
        l, r = Primitive(c0, False), Primitive(c1, True)
        # everything between c0 and c1
        i = Intersection(l, r)
        self.assertFalse(i.contains(Point(0, 0)))
        self.assertFalse(i.contains(Point(2, 0)))
        self.assertTrue(i.contains(Point(1.5, 0)))

    def testIntersection_intersections(self) :
        
        c0, c1 = self.get_circles()
        l, r = Primitive(c0, False), Primitive(c1, True)
        # everything between c0 and c1
        i = Intersection(l, r)
        # ray starting at (-3, 0) along x-axis
        ray = Ray(Point(-3, 0), Point(1, 0))
    
        # get intersections        
        ints = i.intersections(ray)
        # the order of the intersections depends on the implementation, but
        # the values should be unique.  hence, sort them according to 
        # x value.
        ints.sort(key = lambda p: p.x)
        reference_ints = [Point(i, 0) for i in (-2,-1, 1, 2)]        
        for i in range(4) :
            self.assertAlmostEqual(ints[i].x, reference_ints[i].x)
        
    #-------------------------------------------------------------------------#
    # TESTS OF REGION CLASS
    #-------------------------------------------------------------------------#
      
    def get_region(self) :
        c0, c1 = self.get_circles()
        # produce a region that represents the area between the two circles
        region = Region()
        region.append(surface=c0, sense=False, operation="I")
        region.append(surface=c1, sense=True, operation="I")
        return region

    def get_region_2(self) :
        L = PlaneV(0)
        R = PlaneV(1)
        B = PlaneH(0)
        T = PlaneH(1)
        region = Region()
        region.append(surface=L, sense=False)
        region.append(surface=R, sense=True, operation="I")
        region.append(surface=B, sense=False, operation="I")
        region.append(surface=T, sense=True, operation="I")
        return region
        
    def testRegion_contains(self) :
        
        region = self.get_region()
        self.assertFalse(region.node.contains(Point(0, 0)))
        self.assertFalse(region.node.contains(Point(2, 0)))
        self.assertTrue(region.node.contains(Point(1.5, 0)))
  
        region = self.get_region_2()
        print region.node.contains(Point(0.5, 0.5))

    def testRegion_intersections(self) :
        
        region = self.get_region()
        ray = Ray(Point(-3, 0), Point(1, 0))        
        ints = region.intersections(ray)
        self.assertAlmostEqual(ints[0].x, -2)
        self.assertAlmostEqual(ints[1].x, -1)
        self.assertAlmostEqual(ints[2].x,  1)
        self.assertAlmostEqual(ints[3].x,  2)
        
if __name__ == '__main__' :
    unittest.main()    
    
