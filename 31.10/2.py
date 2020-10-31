called = False
answ = None


def wrapper(f):
    def decor(*args, **kwargs):
        global called, answ
        if not called:
            called = True
            answ = f(*args, **kwargs)
        return answ
    return decor


@wrapper
def func(a, b):
    return a * b


"""var = func(2, 3)
print(var, id(var))
var = func(1, 3)
print(var, id(var))"""


class map2:
    def __init__(self, func, iter):
        self.answ = [func(i) for i in iter]
        self.ch = 0


    def __iter__(self):
        for i in self.answ:
            yield i



a = map2(lambda x: x**3, [1, 2, 3])
b = map(lambda x: x**3, [1, 2, 3])
print(list(a))
print(b)
print(repr(b))