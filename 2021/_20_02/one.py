class Segment:
    def __init__(self, name):
        self.name = str(name)
        self.segments = []

    def __repr__(self):
        if self.segments:
            return f'{self.name}: {self.segments}'
        return self.name

    def add_segment(self, segment):
        self.segments.append(segment)

    def add_segments(self, *segments):
        self.segments.extend(segments)

def func(instance, symblols, replace_symbol='_'):
    for i in symblols:
        instance.name = instance.name.replace(i, replace_symbol)
    for i in instance.segments:
        func(i, symblols, replace_symbol)


if __name__ == '__main__':
    a1 = Segment('a1∃')
    b1, b2 = Segment('b∆1'), Segment('b2∃')
    c1, c2 = Segment('c∄1∄'), Segment('∄c2')
    d1, d2, d3 = Segment('d∆1'), Segment('d2'), Segment('∆d3')
    e1 = Segment('e∃1')
    a1.add_segments(b1, b2)
    b2.add_segments(c1, c2)
    c1.add_segment(d1)
    d1.add_segment(e1)
    c2.add_segments(d2, d3)
    print(a1)
    func(a1, '∃∄∆')
    print(a1)
