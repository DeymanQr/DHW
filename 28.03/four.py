def func(text=""):
    simbls = [".", ",", "?", "!", ";", ":"]
    spis = text.lower().split()
    answ = {}
    for i in range(len(spis)):
        if spis[i][-1] in simbls:
            spis[i] = spis[i][:-1:]
        if spis[i] not in answ:
            answ[spis[i]] = 1
        else:
            answ[spis[i]] += 1
    max_repeat_word = ""
    max_repeat = 0
    for i in answ.items():
        if i[1] > max_repeat or (i[1] == max_repeat and len(i[0]) < len(max_repeat_word)):
            max_repeat_word = i[0]
            max_repeat = i[1]
    return [max_repeat_word, max_repeat]


a = input()
print(func(a))