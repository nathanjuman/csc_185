import math

class Point:
    """ Create a class Point to represent a point in 2-dimensional space: """

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getDistanceFromOrigin(self):
        'returns the distance of this point from the origin'
        return math.sqrt(self.x**2 + self.y**2)

    def double(self):
        'doubles the x and y coordinates of this point'
        self.x = self.x * 2
        self.y = self.y * 2

    def halfway(self, target):
        'returns a new point that is halfway between this point and another target point'
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def isAbove(self, other):
        'compares points with different y-values to check whether one lies above the other'
        return self.y > other.y

    def reflect_x(self):
        'reflects a point about the x-axis and check if the new y-coordinate is the negative of the original.'
        return Point(self.x, -self.y)

    def move(self, dx, dy):
        'moves a point by positive and negative values.'
        self.x += dx
        self.y += dy

    def __sub__(self, other):
        'subtracts one point from another and verify the resulting x and y coordinates'
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        'returns a string containing the data in the point object'
        return f"Point is at {self.x, self.y}."

def main():
    #1a and 1b
    a = Point(3, 4)
    b = Point(5, 6)
    print(a.x, a.y) #expect: 3 4
    print(b.x, b.y) #expect: 5 6

    #1c.i
    dista = a.getDistanceFromOrigin()
    print(dista) #expect: 5
    distb = b.getDistanceFromOrigin()
    print(distb) #expect: 7.810...

    #1c.ii
    print(a.x, a.y) #expect: 3 4
    a.double()
    print(a.x, a.y) #expect: 6 8

    #1c.iii
    c = a.halfway(b)
    print(c.x, c.y) #expect: 5.5 7.0
    print(type(c)) #expect: class point

    #1c.iv
    print(a) #expect: Point is at (6, 8)
    print(b) #expect: Point is at (5, 6)

    #1c.v
    print(b.isAbove(a)) #expect: False (because a was doubled)

    #1c.vi
    print(a.reflect_x()) #expect: Point is at (6, -8)

    #1c.vii
    a = Point(3, 5)
    print(a.move(1, 2)) #expect: 4 7

main()