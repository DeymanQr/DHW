class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return 2*(self.a+self.b)

    def area(self):
        return self.a*self.b


class Square(Rectangle):
    def __init__(self, a, b=None):
        super().__init__(a, b)
        self.b = a


cc = Square(12)
print(cc.area())