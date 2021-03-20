from typing import NamedTuple


class Person(NamedTuple):
    id: int
    name: str = 'Pedro'


class Student(NamedTuple):
    name: str
    surname: str
    course: int = 1
    mark: int = 4


def replace(t, **kwargs):
    args = []
    for i, j in enumerate(t._fields):
        if j not in kwargs.keys():
            args.append(t[i])
        else:
            args.append(kwargs[j])
    return t.__class__(*args)


ps = Person(1)
print(ps)
ps = replace(ps, id=2)
print(ps)

st = Student('Lol', 'Kek', 2)
print(st)
st = replace(st, mark=13)
print(st)
