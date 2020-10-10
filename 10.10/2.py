class Fraction:
    """Class for working with fractions"""

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError("division by zero")

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}" # numerator=2, dominator=3 -> 2/3

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Finds the greatest common divisor"""
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return abs(a + b)


    def reduce_fraction(self):
        """Reduses fraction"""
        gcd = self.gcd(self.numerator, self.denominator)
        while gcd > 1:
            self.numerator //= gcd
            self.denominator //= gcd
            gcd = self.gcd(self.numerator, self.denominator)
        return Fraction(self.numerator, self.denominator)

    def __add__(self, other):
        final_fraction = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator*other.denominator) # a/b + c/d = a*d+c*b / b*d
        return final_fraction.reduce_fraction()

    def __sub__(self, other):
        final_fraction = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator*other.denominator) # a/b - c/d = a*d-c*b / b*d
        return final_fraction.reduce_fraction()

    def __mul__(self, other):
        final_fraction = Fraction(self.numerator*other.numerator, self.denominator*other.denominator) # a/b * c/d = a*c / b*d
        return final_fraction.reduce_fraction()

    def __truediv__(self, other):
        if other.numerator != 0:
            final_fraction = Fraction(self.numerator*other.denominator, self.denominator*other.numerator) # a/b / c/d = a*d / b*c
            return final_fraction.reduce_fraction()
        raise ZeroDivisionError("division by zero")

    def __pow__(self, power, modulo=None):
        final_fraction = Fraction(self.numerator**power, self.denominator**power) # a/b * c/d = a*c / b*d
        return final_fraction.reduce_fraction()
