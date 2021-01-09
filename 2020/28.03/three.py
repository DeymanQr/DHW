slovar = "a b c, c b e, e f g"


def str_to_dict(string=""):
    dictt = {}
    for i in string.split(", "):
        slova = i.split()
        dictt[slova[0]] = [slova[1], slova[2]]
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
    for i in dictt.items():
        if slovo == i[0]:
            answ.append(i[0])
        elif slovo == i[1][0]:
            answ.append(i[1][0])
        elif slovo == i[1][1]:
            answ.append(i[1][1])
    if answ != []:
        return answ


def func(slovo=""): 
    answ = []
    dictt = str_to_dict(slovar)
    for i in dictt.items():
        if slovo == i[0]:
            answ.append(i[0])
            answ.append(func_copy(i[1][0]))
            answ.append(func_copy(i[1][1]))
        elif slovo == i[1][0]:
            answ.append(func_copy(i[0]))
            answ.append(i[1][0])
            answ.append(func_copy(i[1][1]))
        elif slovo == i[1][1]:
            answ.append(func_copy(i[0]))
            answ.append(func_copy(i[1][0]))
            answ.append(i[1][1])
    if answ == []:
        return "Это слово не найдено. Попробуйте другое."
    return unic_els(spis=answ, slovo=slovo)


while True:
    word = input()
    print(func(slovo=word))