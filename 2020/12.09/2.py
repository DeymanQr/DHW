'''def lol():
    ch = 1
    while True:
        data = yield ch
        if data:
            data = yield f'{data}:{ch}'
        if data == 'stop':
            print('qwert')
            return
        ch += 1

gen = lol()
print(next(gen))
print(gen.send('kek'))
print(gen.send('stop'))'''


def kek():
    ch = 1
    while True:
        data = yield ch
        print(f"lol: {data}")
        if data == "stop":
            return
        ch += 1


gen = lol()
print(next(gen))


#a = <iterareble>
#iter_a = iter(a)
#while True:
#    try:
#        print(next(iter_a))
#    except StopIteration:
#        break