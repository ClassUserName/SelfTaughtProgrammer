import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        return area

circ1 = Circle(1)
print(circ1.area())
