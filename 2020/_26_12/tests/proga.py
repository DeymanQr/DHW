from abc import ABC, abstractmethod


class AbstractCRUD(ABC):
    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def read(self, **kwargs):
        pass

    @abstractmethod
    def update(self, item_id, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass


class KwargsError(Exception):
    pass


def kwargs_check(f):
    def wrapper(self, *args, **kwargs):
        for i in kwargs.keys():
            if i not in tuple(self._keys.keys()):
                raise KwargsError(f"'{i}' is not a key")
            if not isinstance(kwargs[i], self._keys[i]):
                raise TypeError(f"'{i}' must be {self._keys[i]}, not {type(kwargs[i])}")
        return f(self, *args, **kwargs)
    return wrapper


class CRUD(AbstractCRUD):
    def __init__(self, path):
        self.path = path
        self._keys = {'id': int, 'name': str, 'surname': str, 'bd': str, 'zodiac_sign': str, 'loves_green': int}

    @kwargs_check
    def create(self, **kwargs):
        if len(kwargs) < len(self._keys):
            raise KwargsError('Not all kwargs')
        data = self.read(id = kwargs['id'])
        if data:
            raise ValueError('id is alreay in use')
        with open(self.path, 'a', encoding='UTF-8') as f:
            f.write(', '.join([str(kwargs[i]) for i in self._keys.keys()]) + '\n')

    @kwargs_check
    def read(self, **kwargs):
        data = []
        with open(self.path, encoding='UTF-8') as f:
            for i in f:
                list_obj = i.strip().split(', ')
                changed_list_obj = [self._keys[i[1]](list_obj[i[0]]) for i in enumerate(self._keys.keys())]
                dict_obj = {i[1]: changed_list_obj[i[0]] for i in enumerate(self._keys.keys())}
                for j in kwargs.keys():
                    if dict_obj[j] != kwargs[j]:
                        break
                else:
                    data.append(dict_obj)
        return data

    @kwargs_check
    def update(self, item_id, **kwargs):
        data = self.read()
        for i in data:
            if i['id'] == item_id:
                break
        else:
            raise ValueError('id didn\'t used yet')
        if kwargs.get('id') is not None:
            for i in data:
                if i['id'] == kwargs['id']:
                    raise ValueError('new id is alreay in use')
        with open(self.path, 'w', encoding='UTF-8') as f:
            for i in data:
                if i['id'] == item_id:
                    dictt = {}
                    for j in self._keys.keys():
                        if j in kwargs.keys():
                            dictt[j] = kwargs[j]
                        else:
                            dictt[j] = i[j]
                    f.write(', '.join([str(dictt[j]) for j in self._keys.keys()]) + '\n')
                else:
                    f.write(', '.join([str(i[j]) for j in self._keys.keys()]) + '\n')

    @kwargs_check
    def delete(self, **kwargs):
        data = self.read()
        with open(self.path, 'w', encoding='UTF-8') as f:
            for i in data:
                for j in kwargs.keys():
                    if kwargs[j] != i[j]:
                        f.write(', '.join([str(i[j]) for j in self._keys.keys()]) + '\n')


if __name__ == '__main__':
    a = CRUD('C:/Users/skaku/Documents/all/Programming/Python_home/_26_12/tests/text.csv')
    # while True:
    #     eval(input())
