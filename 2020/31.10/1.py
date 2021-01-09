class Shape:
    def __init__(self, *center: tuple):
        self.center = center

    def __str__(self):
        return f"Coords: {' '.join(str(i) for i in self.center)}"


class Dot(Shape):
    def __init__(self, *center):
        super().__init__(*center)


class Circle(Shape):
    def __init__(self, *center, radius):
        super().__init__(*center)
        self.radius = radius

    def __int__(self):
        return f"Radius: {self.radius}"

    def is_dot_in_circle(self, dot: Dot):
        if isinstance(dot, Dot):
            return self.radius ** 2 >= ((self.center[1] - dot.center[1])**2) + ((self.center[0] - dot.center[0])**2)
        raise TypeError(f"type of dot must be 'Dot', not '{str(type(dot))[17:-2]}'")


a = Dot(1, 2)
b = Dot(0, -1)
cir = Circle(0, 0, radius=1)
print(cir.is_dot_in_circle(a))
print(cir.is_dot_in_circle(b))
#print(cir.is_dot_in_circle(cir))