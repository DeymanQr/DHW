def decode(to_type):
    def main(func):
        def wrapper(self, other):
            types = {'mm': 1000000, 'cm': 100000, 'dm': 10000, 'm': 1000, 'km': 1}
            self.value *= types[to_type] / types[self.value_type]
            other.value *= types[to_type] / types[other.value_type]
            return func(self, other)
        return wrapper
    return main


class Length:
    def __init__(self, value, value_type):
        # value_type: 'mm', 'cm', 'dm', 'm', 'km'
        self.value = value
        if value_type not in ['mm', 'cm', 'dm', 'm', 'km']:
            raise TypeError('value_type must be in [\'mm\', \'cm\', \'dm\', \'m\', \'km\']')
        self.value_type = value_type

    def __repr__(self):
        return f'{self.value} {self.value_type}'

    @decode(to_type='m')
    def __add__(self, other):
        return Length(self.value + other.value, 'm')

    @decode(to_type='m')
    def __sub__(self, other):
        return Length(self.value - other.value, 'm')

    @decode(to_type='m')
    def __mul__(self, other):
        return Length(self.value * other.value, 'm')

    @decode(to_type='m')
    def __truediv__(self, other):
        return Length(self.value / other.value, 'm')


print((Length(1, 'mm') + Length(123, 'cm') - Length(12, 'km') * Length(1000, 'm')) /
      (Length(100, 'm') - Length(300, 'dm') + Length(15, 'mm') - Length(20, 'km')))
