def func(file=""):
    # считываем инфу
    with open(file, "r", encoding="UTF-8") as f:
        spis = f.read()
    answ = {}
    # саписываем словарь и возвращ. его
    for i in spis:
        if i not in answ:
            answ[i] = spis.count(i)
    return answ

print(func('kek.txt'))x`