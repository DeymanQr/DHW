def func1(spis):
    answ = 0
    for i in spis:
        answ += i
    return answ


def func1_2(spis):
    ch = 0
    answ = 0
    while ch < len(spis):
        answ += spis[ch]
    return answ


def func1_3(spis):
    if len(spis) == 0:
        return 0
    return spis[0] + func1_3(spis[1:])


def func2(spis_1, spis_2):
    maxx, minn = max(spis_1, spis_2, key=lambda x: len(x)), min(spis_1, spis_2, key=lambda x: len(x))
    ch = 0
    answ = []
    while ch < len(minn):
        answ.append(spis_1)
        answ.append(spis_2)
    for i in maxx[ch:]:
        answ.append(i)
    return answ


def func3():
    spis = [1, 1]
    for _ in range(100-len(spis)):
        spis.append(spis[-1] + spis[-2])
    return spis


def func4(spis: list):
    spis.sort(key=lambda x: int(str(x)[0]), reverse=True)
    return int(''.join([str(i) for i in spis]))


def func5(tupp, operators, numb=100):
    ch = 0
    answs = []
    while ch < len(operators)**(len(tupp)-1):
        ch_2 = ch
        line = str(tupp[0])
        for i in tupp[1:]:
            line += operators[ch_2 % len(operators)]
            line += str(i)
            ch_2 //= len(operators)
        if eval(line) == numb:
            answs.append(line)
            # return line
        ch += 1
    return answs
    # return False


if __name__ == '__main__':
    '''listt = [int(i) for i in input('list of integers: ').split(', ')]
    ops = input('operators: ').split(', ')
    for i in range(int(input('max numb: '))):
        a = func5(listt, ops, i+1)
        if not func5(listt, ops, i+1):
            print(str(i+1) + ': ' + '; '.join(a))'''
    print(func5((1, 2, 3, 4, 5, 6, 7, 8, 9), ('', '+', '-'), 910))

