import time
import math


def decor(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        timme = str(time.time() - start)
        print(timme[:timme.index('.')+6] + 's')
        return res
    return wrapper


def func(string):
    if '==' not in string and '=' in string:
        string = string.replace('=', '==')
    letters_set = tuple(set(i for i in string if i not in '+-*/=1234567890(.) '))
    numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    if len(letters_set) > 9:
        return ()


    '''def per(p, q, s):
        if p == q:
            yield s[:len(letters_set)]
        else:
            for i in range(p, q):
                s[i], s[p] = s[p], s[i]
                for ii in per(p+1, q, s):
                    yield ii[:len(letters_set)]
                s[i], s[p] = s[p], s[i]'''


    def per(mas, length):
        if length == 1:
            for i in mas:
                yield str(i)
        for i in mas:
            mas2 = mas.copy()
            mas2.remove(i)
            for j in per(mas2, length-1):
                answ = str(i) + j
                yield answ


    for i in per(numbs, len(letters_set)):
        new_string = string
        for j in enumerate(i):
            new_string = new_string.replace(letters_set[j[0]], str(j[1]))
        try:
            if eval(new_string):
                print(new_string.replace('==', '='))
                break
        except SyntaxError:
            continue


if __name__ == '__main__':
    # 'eleve + lecon == devoir',
    strs = (
        'abcde * a == eeeeee',
        'aba + abc + acc == 1416',
        'pi**(0.5) + e == pie**(0.5)',
        'abc * 3 == ccc',
        'abc / 5 == a * b * c',
        'aaa + bbb + ccc = baac',
        'aa + bb + cc = abc',
    )
    # decor_func = decor(func)
    # decor_func('')
    for string in strs:
        func(string)