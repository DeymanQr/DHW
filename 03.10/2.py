class Rectangle:
    """Прямоугольник"""
    def __init__(self, x1, y1, x2, y2):
        self.width, self.height = abs(x1 - x2), abs(y1 - y2)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


rect = Rectangle(int(input()), int(input()), int(input()), int(input()))
print(f"Периметр: {rect.perimeter()}")
print(f"Площадь: {rect.area}")