class Dot:
    def __init__(self, x: [int, float, complex], y: [int, float, complex]):
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        return (self.x - other.x ** 2 + self.y - other.y) ** 0.5


class Rectangle:
    def __init__(self, dot1: Dot, dot2: Dot):
        self.dot1 = dot1
        self.dot2 = dot2
        self.length = abs(self.dot1.x - self.dot2.x)
        self.height = abs(self.dot1.y - self.dot2.y)

    def perimeter(self):
        if self.area() == 0:
            return self.height + self.length
        return 2 * (self.height + self.length)

    def area(self):
        return self.height * self.length


a = Dot(2, 2)
b = Dot(1, 0)
c = Rectangle(a, b)
print(c.perimeter())