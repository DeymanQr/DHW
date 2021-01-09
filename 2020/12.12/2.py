from abc import ABC


class AbstractNumber(ABC):
    pass


class AbstractEvenNumber(ABC):
    pass


def zero_format(a):
    while str(a)[-1] == '0':
        a //= 10
    return a


def decode__fracts(f):
    def wrapper(self, other):
        if len(str(self.fract)) > len(str(other.fract)):
            other.fract *= 10 ** (len(str(self.fract)) - len(str(other.fract)))
        else:
            self.fract *= 10 ** (len(str(other.fract)) - len(str(self.fract)))
        return f(self, other)
    return wrapper


class Number(AbstractNumber):
    def __init__(self, integer, fract):
        self.integer = integer
        self.fract = fract

    def __repr__(self):
        return f"{self.integer}.{self.fract}"

    @decode__fracts #2, 22 -> 20, 22
    def __add__(self, other):
        integer = self.integer + other.integer + (self.fract + other.fract) // 10 ** len(str(self.fract))
        fract = (self.fract + other.fract) % 10 ** len(str(self.fract))
        return Number(integer=integer, fract=zero_format(fract))

    @decode__fracts
    def __sub__(self, other): # 2.3 - 1.4 -> 2.3 + (-1.4)
        return self + Number(integer=other.integer * -1, fract=other.fract * -1)

    @decode__fracts
    def __mul__(self, other): # (a+b)(c+d) = ac (int) + ad (notint) + bc (notint) + cd (notint)
        integer = self.integer * other.integer + () // 10 ** len(self.fract)
        fract = (self.fract + other.fract) % 10 ** len(self.fract)
        return Number(integer=integer, fract=fract)

    @decode__fracts
    def __truediv__(self, other):
        pass


class EvenNumberWithError(AbstractEvenNumber, Number):
    def __init__(self, integer, fract):
        super().__init__(integer, fract)
        for i in str(self.integer):
            if int(i) % 2 == 1:
                raise TypeError()
        for i in str(self.fract):
            if int(i) % 2 == 1:
                raise TypeError()


def change_even_numbs(f):
    def wrapper(self, integer, fract):
        f()
        odd_numbs = ('1', '3', '5', '7', '9')
        integer = str(self.integer)
        fract = str(self.fract)
        for i in enumerate(integer):
            numb = int(i[1])
    return wrapper


class EvenNumber(AbstractEvenNumber, Number):
    def __init__(self, integer, fract):
        super().__init__(integer, fract)


a = Number(1, 2)
b = Number(2, 82)
print(a + b)