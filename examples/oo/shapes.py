"""
This module defines several shape classes.
"""


class Shape:

    def __init__(self):
        pass

    @property
    def area(self):
        #print("I'm a SHAPE method, not a CIRCLE method!")
        return self._compute_area()

    def _compute_area(self):
        raise NotImplementedError

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def _compute_area(self):
        return 3.14159*self.radius**2
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width, self.height = width, height
        
    def _compute_area(self):
        print("Rectangle area!")
        return self.width * self.height

class Square(Rectangle):
    
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        
 


if __name__ == '__main__':
    A = Shape()
    C = Circle(2.0)
    R = Rectangle(2.0, 4.0)
    S = Square(2.0)
    
