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
        return f"{self.integer}.{abs(self.fract)}"

    @decode__fracts
    def __add__(self, other):
        integer = self.integer + other.integer + (self.fract + other.fract) // 10 ** len(str(self.fract))
        fract = (self.fract + other.fract) % 10 ** len(str(self.fract))
        return Number(integer=integer, fract=zero_format(fract))

    @decode__fracts
    def __sub__(self, other):
        return self + Number(integer=other.integer*-1, fract=other.fract*-1)

    @decode__fracts
    def __mul__(self, other): # (a+b)(c+d) = ac (int) + ad (notint) + bc (notint) + cd (notint)
        pass

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
        f(self, integer, fract)
        integerr = [int(i) for i in str(self.integer)]
        fractt = [int(i) for i in str(self.fract)]
        for i in enumerate(integerr):
            numb = i[1]
            if numb % 2 == 1:
                if numb == 9:
                    integerr[i[0]] = 8
                else:
                    integerr[i[0]] = numb + 1
        for i in enumerate(fractt):
            numb = i[1]
            if numb % 2 == 1:
                if numb == 9:
                    fractt[i[0]] = 8
                else:
                    fractt[i[0]] = numb + 1
        new_integer = 0
        new_fract = 0
        for i in enumerate(integer):
            new_integer += i[1] * 10 ** i[0]
        for i in enumerate(fractt):
            new_fract += i[1] * 10 ** i[0]
        self.integer = new_integer
        self.fract = new_fract
    return wrapper


class EvenNumber(AbstractEvenNumber, Number):
    @change_even_numbs
    def __init__(self, integer, fract):
        super().__init__(integer, fract)


a = EvenNumber(23, 12)
print(a)