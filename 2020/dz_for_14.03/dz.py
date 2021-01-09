def func(spis):
    while True:
        a = spis[-1] + spis[-2]
        yield a
        spis.append(a)

answ = func([1, 1])
print(next(answ))
print(next(answ))
print(next(answ))
print(next(answ))