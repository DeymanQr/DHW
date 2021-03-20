from abc import ABC, abstractmethod
from time import time, sleep


class AbstractFileChanger(ABC):

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def read(self, times=None, type=None):
        pass

    @abstractmethod
    def update(self, item_id: int, **kwargs):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_cost_sum(self, times=None, with_tax=True, type=None):
        pass

    @abstractmethod
    def get_tax_sum(self, from_time, to_time):
        pass


def kwargs_check(f):
    def wrapper(self, *args, **kwargs):
        for i in kwargs.keys():
            if i == 'type' and kwargs[i] not in self._sold_types:
                raise ValueError('type is not defined')
            if i not in tuple(self._keys.keys()):
                raise ValueError(f"'{i}' is not a key")
            if not isinstance(kwargs[i], self._keys[i]):
                raise TypeError(f"'{i}' must be {self._keys[i]}, not {type(kwargs[i])}")
        return f(self, *args, **kwargs)
    return wrapper


class FileChanger(AbstractFileChanger):
    def __init__(self, path, tax_cost):
        self._path = path
        self._tax_cost = tax_cost
        self._sold_types = ('Regular purchase', 'Tax', 'Tax free purchase')
        self._keys = {'id': int, 'name': str, 'cost': float, 'time': float, 'type': str}

    def get_path(self):
        return self._path

    def change_tax_cost(self, new_cost):
        self._tax_cost = new_cost

    @kwargs_check
    def create(self, **kwargs):
        if len(kwargs.keys()) < len(self._keys.keys()):
            raise TypeError('')
        with open(self._path, 'a', encoding='UTF-8') as f:
            obj = {}
            for i in kwargs:
                obj[i] = str(kwargs[i])
            f.write(', '.join(obj.values()) + '\n')

    def read(self, times=None, type=None):
        if times is None and type is None:
            raise ValueError('no keys')
        if type is not None and type not in self._sold_types:
            return ValueError
        if times is not None and len(times) != 2:
            raise ValueError('len of times must be 2')
        with open(self._path, 'r', encoding='UTF=8') as f:
            data = []
            for i in f:
                list_obj = i.strip().split(', ')
                changed_list_obj = [self._keys[i[1]](list_obj[i[0]]) for i in enumerate(self._keys.keys())]
                dict_obj = {i[1]: changed_list_obj[i[0]] for i in enumerate(self._keys.keys())}
                if times is not None and not times[0] <= dict_obj['time'] <= times[1]:
                    continue
                if type and dict_obj['type'] != type:
                    continue
                data.append(dict_obj)
            return data

    def __read_all(self):
        with open(self._path, 'r', encoding='UTF=8') as f:
            data = []
            for i in f:
                list_obj = i.strip().split(', ')
                changed_list_obj = [self._keys[i[1]](list_obj[i[0]]) for i in enumerate(self._keys.keys())]
                dict_obj = {i[1]: changed_list_obj[i[0]] for i in enumerate(self._keys.keys())}
                data.append(dict_obj)
        return data

    @kwargs_check
    def update(self, item_id, **kwargs):
        if not isinstance(item_id, int):
            return ValueError
        data = self.__read_all()
        with open(self._path, 'w', encoding='UTF-8') as f:
            for i in data:
                if i['id'] == item_id:
                    dict_obj = i
                    for i in kwargs:
                        dict_obj[i] = kwargs[i]
                    f.write(', '.join([str(j) for j in dict_obj.values()]) + '\n')
                else:
                    f.write(', '.join([str(j) for j in i.values()]) + '\n')

    @kwargs_check
    def delete(self, id):
        data = self.__read_all()
        with open(self._path, 'w', encoding='UTF-8') as f:
            for i in data:
                if i['id'] != id:
                    f.write(', '.join([str(j) for j in i.values()]) + '\n')

    def get_cost_sum(self, times=None, with_tax=True, type=None):
        if type is not None and type not in self._sold_types:
            return ValueError
        data = self.read(times=times, type=type)
        if with_tax:
            return sum((i['cost'] for i in data))
        else:
            summ = 0
            for i in data:
                if i['type'] == 'Tax free purchase':
                    summ += i['cost']
                elif i['type'] == 'Regular purchase':
                    summ += i['cost'] * (100 - self._tax_cost) / 100
        return summ

    def get_tax_sum(self, from_time, to_time):
        data = self.read(times=[from_time, to_time])
        summ = 0
        for i in data:
            if i['type'] == 'Tax':
                summ += i['cost']
            elif i['type'] == 'Regular purchase':
                summ += i['cost'] * self._tax_cost / 100
        return summ


if __name__ == '__main__':
    obj = FileChanger('db.csv', tax_cost=10)
    print(obj.read(times=(1612001540.1396177, 1612001554.2756152)))