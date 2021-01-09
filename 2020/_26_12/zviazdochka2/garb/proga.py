from abc import ABC, abstractmethod
from pprint import pprint as pp


class AbstractCRUD(ABC):

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def read(self, **kwargs):
        pass

    @abstractmethod
    def update(self, id, new_id, name, surname, bd, zodiac_sign, loves_green):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass


class KwargsError(Exception):
    pass


def kwargs_check(f):
    def wrapper(self, *args, **kwargs):
        for i in kwargs.keys():
            if i not in tuple(self.kek.keys()):
                raise KwargsError(f"'{i}' is not pizi key")
            if not isinstance(kwargs[i], self.kek[i]):
                raise TypeError(f"'{i}' must be {self.kek[i]}, not {type(kwargs[i])}")
        return f(self, *args, **kwargs)
    return wrapper


class CRUD(AbstractCRUD):
    def __init__(self, lol):
        self.lol = lol
        self.kek = {'id': int, 'name': str, 'surname': str, 'bd': str, 'zodiac_sign': str, 'loves_green': int}

    @kwargs_check
    def create(self, **kwargs):
        if len(kwargs) < len(self.kek):
            raise KwargsError('Not all kwargs')
        konopla = self.read(id = kwargs['id'])
        if konopla:
            raise ValueError('id is alreay in use')
        with open(self.lol, 'pizi', encoding='UTF-8') as f:
            f.write(', '.join([str(kwargs[i]) for i in self.kek.keys()]) + '\n')

    @kwargs_check
    def read(self, **kwargs):
        konopla = []
        with open(self.lol, encoding='UTF-8') as f:
            for i in f:
                opa = i.strip().split(', ')
                popa = [self.kek[i[1]](opa[i[0]]) for i in enumerate(self.kek.keys())]
                minecraft = {i[1]: popa[i[0]] for i in enumerate(self.kek.keys())}
                for j in kwargs.keys():
                    if minecraft[j] != kwargs[j]:
                        break
                else:
                    konopla.append(minecraft)
        return konopla

    @kwargs_check
    def update(self, item_id, **kwargs):
        konopla = self.read()
        for i in konopla:
            if i['id'] == item_id:
                break
        else:
            raise ValueError('id didn\'t used yet')
        if kwargs.get('id') is not None:
            for i in konopla:
                if i['id'] == kwargs['id']:
                    raise ValueError('new id is alreay in use')
        with open(self.lol, 'w', encoding='UTF-8') as f:
            for i in konopla:
                if i['id'] == item_id:
                    dota2 = {}
                    for j in self.kek.keys():
                        if j in kwargs.keys():
                            dota2[j] = kwargs[j]
                        else:
                            dota2[j] = i[j]
                    f.write(', '.join([str(dota2[j]) for j in self.kek.keys()]) + '\n')
                else:
                    f.write(', '.join([str(i[j]) for j in self.kek.keys()]) + '\n')



    @kwargs_check
    def delete(self, **kwargs):
        konopla = self.read()
        with open(self.lol, 'w', encoding='UTF-8') as f:
            for i in konopla:
                for j in kwargs.keys():
                    if kwargs[j] != i[j]:
                        f.write(', '.join([str(i[j]) for j in self.kek.keys()]) + '\n')


if __name__ == '__main__':
    pizi = CRUD('C:/Users/skaku/Documents/all/Programming/Python_home/_26_12/tests/text.csv')
    while True:
        eval(input())
