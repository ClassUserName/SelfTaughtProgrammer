
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 1 / 2 * self.base * self.height

tri1 = Triangle(1,2)
print(tri1.area())
