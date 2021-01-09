def isnormal(length_el, length):
    if length_el + 1 != length:
        raise ValueError(f'len of fill must be {length-1}')
    if len()


def del_user(file="", id=0):
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    for i in info:
        if int(i[0]) == id:
            info.remove(i)
            break
    else:
        raise ValueError("element with given id does not exist")
    with open(file, "w", encoding="UTF-8") as f:
        for i in info:
            f.write(",".join(i))
            if info.index(i) != len(info) - 1:
                f.write("\n")


def add_el(file="", fill=[]):
    for i in range(len(fill)):
        fill[i] = str(fill[i])
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(",")) # 1,София,Николаенко,46,5 -> ['1', 'София', 'Николаенко', '46', '5']
    issamelength(length_el=len(fill), length=len(info[0]))
    with open(file, "a", encoding="UTF-8") as f:
        el ="\n" + str(int(info[-1][0]) + 1) + "," + ",".join(fill)
        f.write(el)


def find_el(file="", id=0):
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
        for i in info:
            if int(i[0]) == id:
                return i
        raise ValueError("element with given id does not exist")


def change_el(file="", id=0, fill=[]):
    for i in range(len(fill)):
        fill[i] = str(fill[i])
    info = []
    with open(file, "r", encoding="UTF-8") as f:
        for i in f:
            info.append(i.strip().split(","))
    issamelength(length_el=len(fill), length=len(info[0]))
    for i in info:
        if int(i[0]) == id:
            j = [i[0]]
            j.extend(fill)
            info[info.index(i)] = j
    with open(file, "w", encoding="UTF-8") as f:
        for i in info:
            f.write(",".join(i))
            if info.index(i) != len(info) - 1:
                f.write("\n")


def del_department(dep_file="", user_file="", id=0):
    with open(dep_file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    for i in info:
        if int(i[0]) == id:
            info.remove(i)
    with open(dep_file, "w", encoding="UTF-8") as f:
        for i in info:
            f.write(",".join(i))
            if info.index(i) != len(info) - 1:
                f.write("\n")
    with open(user_file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    del_els = []
    for i in info:
        if int(i[-1]) == id:
            del_els.append(i)
    for i in del_els:
        info.remove(i)
    with open(user_file, "w", encoding="UTF-8") as f:
        for i in info:
            f.write(",".join(i))
            if info.index(i) != len(info) - 1:
                f.write("\n")


def max_age(file="", id=None):
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    ages = []
    for i in info:
        if id == None or int(i[-1]) == id:
            ages.append(int(i[-2]))
    return max(ages)


def min_age(file="", id=None):
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    ages = []
    for i in info:
        if id == None or int(i[-1]) == id:
            ages.append(int(i[-2]))
    return min(ages)


def middle_age(file="", id=None):
    with open(file, "r", encoding="UTF-8") as f:
        info = []
        for i in f:
            info.append(i.strip().split(","))
    answ = 0
    ages = 0
    for i in info:
        if id == None or int(i[-1]) == id:
            answ += int(i[-2])
            ages += 1
    if ages != 0:
        return answ/ages
    else:
        raise ValueError("elements with given id does not exist")

