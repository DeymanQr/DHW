slovar = "a b, b c, n e, z d"


def str_to_dict(string=""):
    dictt = {}
    for i in string.split(", "):
        slova = i.split()
        dictt[slova[0]] = slova[1]
    return dictt


def unic_els(spis=[], slovo=""):
    spis_2 = []
    for i in spis:
        if i not in spis_2 and i != slovo:
            spis_2.append(i)
    return spis_2


def func_copy(slovo=""): # копия ф-ции для "рекурсии" (почти оригинал 😀?    )
    answ = []
    dictt = str_to_dict(slovar)
    if slovo in dictt.keys():
        answ.append(dictt[slovo])
    if slovo in dictt.values():
        for i in dictt.items():
            if i[1] == slovo:
                answ.append(i[0])
    if answ != []:
        return answ


def func(slovo=""):
    answ = []
    dictt = str_to_dict(slovar)
    if slovo in dictt.keys():
        answ.append(dictt[slovo])
        a = func_copy(dictt[slovo]) # проверяем, есть ли синоним к синониму
        if a != None:
            answ.extend(a)
    if slovo in dictt.values():
        for i in dictt.items():
            if i[1] == slovo:
                answ.append(i[0])
                a = func_copy(i[1]) # проверяем, есть ли синоним к синониму
                if a != None:
                    answ.extend(a)
    if answ == []:
        return "Это слово не найдено. Попробуйте другое."
    return unic_els(spis=answ, slovo=slovo)


while True:
    word = input()
    print(func(slovo=word))
