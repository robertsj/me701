class Region:
    
    def __init__(self) :
        self.node = None

    def append(self, node=None, surface=None, operation="U", sense=False) :
        assert((node and not surface) or (surface and not node))
        assert(operation in ["U", "I"])
        if isinstance(surface, Surface) :
            node = Primitive(surface, sense)
        if self.node is None :
            self.node = node
        else :
            O = Union if operation == "U" else Intersection
            self.node = O(self.node, node)

    def contains(self, p) :
        pass 
     
    def intersections(self, r) :
        pass
        
