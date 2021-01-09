def func(string=""):
    simbls = [".", ",", "?", "!", ";"]
    spis = string.split()
    answ = {}
    for i in range(len(spis)):
        if spis[i][-1] in simbls:
            spis[i] = spis[i][:-1:]
        if spis[i] not in answ:
            answ[spis[i]] = 1
        else:
            answ[spis[i]] += 1
    return answ


a = input()
print(func(a))