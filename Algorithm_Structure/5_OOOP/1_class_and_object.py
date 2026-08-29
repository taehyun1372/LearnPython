class Symbol(object):
    id = 0

    def __init__(self, value):
        self.value = value
        self.__id = 0
        self.__id += Symbol.id 
        Symbol.id += 1

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        else:
            return NotImplemented

    def __hash__(self): 
        return hash(self.value)

    def get_id(self):
        return self.__id
    
import math

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "point ({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x,y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi*(self.radius**2)

    def circumference(self):
        return 2*math.pi*self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "circle ({0.radius!r}, {0.x!r})".format(self)

    def __str__(self):
        return repr(self)
    
if __name__ == "__main__":
    x = Symbol("Py")
    y = Symbol("Py")
    print(x.get_id())
    print(y.get_id())

    symbols = set()
    symbols.add(y)
    symbols.add(x)

    print(x is y) # value compare
    print(x == y) # object identity compare if __eq__ is not implemented
    print(len(symbols))
    print(symbols.pop().get_id())

    print("--------------")
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a is b) # object identity compare
    print(a == b) # value compare

    c = a
    print(a is c)

    print("--------------")
    a = Point(3, 4)
    print(a) # call __str__ first and __repr__ if __str__ is not there
    print(repr(a)) # object status or representation
    print(str(a)) 
    print(a.distance_from_origin())

    c = Circle(3,2,1)
    print(c)
    print(repr(c))
    print(str(c))
    print(c.circumference())
    print(c.edge_distance_from_origin())

    d = Circle(2,2,1)
    e = Circle(3,2,1)
    print(c == d)
    print(c == e)
