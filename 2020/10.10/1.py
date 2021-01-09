from typing import Union


class Number:
    def __init__(self, number: Union[int, float]):
        self.number = number

    def plus(self, other):
        return Number(self.number + other)

    def minus(self, other):
        return Number(self.number - other)

    def umnozh(self, other):
        return Number(self.number * other)

    def delit(self, other):
        return Number(self.number / other) if other != 0 else Number(10.*10**308)

a = Number(4)
b = a.delit(0)
if b.number == 10.*10**308:
    print("You are ivalid!")
else:
    print(b.number)