class Base:
    def __init__(self):
        self.base = []

    def add(self, *args):
        self.base.extend(args)

    def __repr__(self):
        return f"<{', '.join([str(i) for i in a.base])}>"


a = Base()
a.add(10, 20, 'abc')
print(a)