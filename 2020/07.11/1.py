from abc import ABC, abstractmethod


class AbstractExample(ABC):
    def print_arg(self, arg):
        print(arg)

    @abstractmethod
    def lol(self):
        pass

    @abstractmethod
    def kek(self):
        pass


class ExampleOne(AbstractExample):
    def lol(self):
        print('lol')

    def kek(self):
        print('kek')


a = ExampleOne()
a.print_arg(123456789)