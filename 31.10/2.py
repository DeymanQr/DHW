class map2:
    def __init__(self, func, iter):
        self.answ = [func(i) for i in iter]
        self.ch = 0


    def __iter__(self):
        for i in self.answ:
            yield i

    def __str__(self):
        return f"<map2 object at {self.__repr__().split()[-1]}"



a = map2(lambda x: x**3, [1, 2, 3])
b = map(lambda x: x**3, [1, 2, 3])
print(repr(a))

# and -> &
# or -> |
