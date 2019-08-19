#%%
import math
class Point:
    """Represents a point in 3-D space.
    """
    
    dimension=3

    def __init__(self, x=0, y=0, z=0):
        """Initialize a point with its three coordinates.
        """

        self._x, self._y, self._z = x, y, z

    @property
    def x(self):
        return self.__get_x()
    
    @property
    def y(self):
        return self._y
    
    @property
    def z(self):
        return self._z
    
    def __get_x(self):
        return self._x
        
    def __str__(self):
        return "Point({}, {}, {})".format(self._x, self._y, self._z)
    
    def __add__(self, P):
         new_P = Point(self._x+P.x, self._y+P.y, self._z+P.z)
         return new_P
     
    def __mul__(self, a):
        return Point(self._x*a, self._y*a, self._z*a)
    
    def add(self, P):
        new_P = Point(self._x+P.x, self._y+P.y, self._z+P.z)
        return new_P
    
    def distance_from_origin(self):
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)
    
    def __repr__(self):
        return self.__str__()
#%%    
        
P = Point(1, 2, 3)
O = Point()