from dataclasses import dataclass, replace
from typing import List


# class Lazy:
#     def __init__(self, callable, *args, **kwargs):
#         self.callable = callable
#         self.args = args
#         self.kwargs = kwargs
#         self.obj = None
#
#     def initObj(self):
#         if self.obj in None:
#             self.obj = self.callable(*self.args, **self.kwargs)
#
#     def __getattr__(self, item):
#         self.initObj()
#         return getattr(self.obj, item)
#
#     def __setattr__(self, item, value):
#         self.initObj()
#         return setattr(self.obj, item, value)
#
#     def __len__(self):
#         self.initObj()
#         return len(self.obj)
#
#     def __getitem__(self, item):
#         self.initObj()
#         return self.obj[item]


@dataclass
class PhoneField:
    id: int
    name: str
    surname: str
    phone_number: str


class Query:
    def __init__(self, query: List):
        self.query = query

    def __repr__(self):
        return f'{self.__class__.__name__}(len={len(self.query)})'

    def __iter__(self):
        for i in self.query:
            yield i

    def sort(self, **kwargs):
        new_query = []
        for i in self.query:
            for j in kwargs:
                if i.__dict__.get(j) is not None and i.__dict__[j] != kwargs[j]:
                    # self.query.remove(i)
                    break
            else:
                new_query.append(i)
        # return self.query
        return Query(new_query)

    def get(self, **kwargs):
        for i in self.query:
            for j in kwargs:
                if i.__dict__.get(j) is not None and i.__dict__[j] != kwargs[j]:
                    # self.query.remove(i)
                    break
            else:
                return i


class DbTool:
    def __init__(self, path: str, field_type):
        self._path = path
        self._field_type = field_type

    def get_path(self):
        return self._path

    def _field_to_str(self, field):
        if field.__class__ != self._field_type:
            raise ValueError(f'field type is not {self._field_type.__name__}')
        return ', '.join([str(i) for i in field.__dict__.values()])

    def _str_to_field(self, string):
        return self._field_type(**{i: self._field_type.__annotations__[i](j) for i, j in zip(
            self._field_type.__annotations__.keys(),
            string.split(', ')
        )})

    def create(self, field):
        with open(self._path, 'a', encoding='UTF-8') as f:
            f.write(self._field_to_str(field)+'\n')
        return

    def read(self, **kwargs):
        if not kwargs:
            return Query([])
        data = []
        with open(self._path, 'r', encoding='UTF-8') as f:
            for i in f:
                item = self._str_to_field(i.strip())
                for j in kwargs:
                    if item.__dict__.get(j) is not None and item.__dict__[j] != kwargs[j]:
                        break
                else:
                    data.append(item)
        return Query(data) # , PhoneField)

    def __read_all(self):
        data = []
        with open(self._path, 'r', encoding='UTF-8') as f:
            for i in f:
                data.append(self._str_to_field(i.strip()))
        return Query(data) # , PhoneField)

    def edit(self, item_id: int, **kwargs):
        data = self.__read_all()
        # if kwargs.get('id') is not None and
        with open(self._path, 'w', encoding='UTF-8') as f:
            for i in data:
                if i.id == item_id:
                    i = replace(i, **kwargs)
                f.write(self._field_to_str(i)+'\n')
        return

    def delete(self, id: int):
        data = self.__read_all()
        # if kwargs.get('id') is not None and
        with open(self._path, 'w', encoding='UTF-8') as f:
            for i in data:
                if i.id != id:
                    f.write(self._field_to_str(i)+'\n')
        return



