class Woman:
    def __init__(self, age):
        self._age = age

    @property
    def her_age(self):
        print('This is true')
        return self._age - 10

    @her_age.setter
    def her_age(self, data):
        self._age = data
