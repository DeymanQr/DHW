from abc import ABC, abstractmethod


class AbstractOst(ABC):
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def remove(self, index, value):
        pass

    @abstractmethod
    def index(self, key):
        pass

    @abstractmethod
    def indexes(self, key):
        pass


class Ost(AbstractOst):
    def __init__(self, *args):
        self.__length = len(args)
        self.__counter = 0
        for i in range(self.__length):
            self.__dict__[str(i)] = args[i]

    def __str__(self):
        return f"|{', '.join(repr(self.__dict__[str(i)]) for i in range(self.__length))}|"

    def __repr__(self):
        return f"|{', '.join(repr(self.__dict__[str(i)]) for i in range(self.__length))}|"

    def __getitem__(self, item):
        return self.__dict__[str(item)]

    def __setitem__(self, key, value):
        self.__dict__[str(key)] = value

    def __delitem__(self, key):
        for i in range(key, self.__length-1):
            self.__dict__[str(i)] = self.__dict__[str(i+1)]
        self.__length -= 1
        del self.__dict__[str(self.__length)]

    def __len__(self):
        return self.__length

    def __contains__(self, item):
        for i in range(self.__length):
            if self.__dict__[str(i)] == item:
                return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.__counter += 1
            return self.__dict__[str(self.__counter-1)]
        except KeyError:
            self.__counter = 0
            raise StopIteration

    def add(self, value):
        self.__dict__[str(self.__length)] = value
        self.__length += 1

    def remove(self, index=None, value = None):
        if index is not None:
            value = self.__dict__[str(index)]
            self.__delitem__(index)
            return value
        elif value is not None:
            for i in range(self.__length):
                if self.__dict__[str(i)] == value:
                    self.__delitem__(i)
                    return i

    def index(self, key):
        for i in range(self.__length):
            if self.__dict__[str(i)] == key:
                return i

    def indexes(self, key):
        result = [i for i in range(self.__length) if self.__dict__[str(i)] == key]
        return result


a = Ost(2, 3, Ost('abc', 'kek', 125), {1, 2, 3}, 'lol')
b = [1, 2, 3]