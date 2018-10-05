class Point:
    """Represents a point in 3-D space.
    """

    def __init__(self, x, y, z):
        """Initialize a point with its three coordinates.
        """

        self.x, self.y, self.z = x, y, z

    
    def __str__(self):
        return "Point({}, {}, {})".format(self.x, self.y, self.z)
    