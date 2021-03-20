class MainModel:
    def __init__(self):
        if self.__class__.__name__ != 'MainModel':
            for i in self.__class__.__dict__.keys():
                if i not in ('__module__', '__doc__'):
                    self.__dict__[i] = self.__class__.__dict__[i]


class StudentModel(MainModel):
    id = int
    name = str


st = StudentModel()

print(st.__dict__)
