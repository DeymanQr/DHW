def arithmetic(file):
    with open(file, "r", encoding="UTF-8") as file:
        info = []
        for i in file:
            info.append(i.strip())

    answ = []

    for i in info:
        if "+" in i:
            numbs = i.split("+")
            res = str(int(numbs[0]) + int(numbs[1]))
        elif "-" in i:
            numbs = i.split("-")
            res = str(int(numbs[0]) - int(numbs[1]))
        elif "*" in i:
            numbs = i.split("*")
            res = str(int(numbs[0]) * int(numbs[1]))
        elif "/" in i:
            numbs = i.split("/")
            if numbs[1] == "0":
                res = "Error"
            else:
                res = str(int(numbs[0]) / int(numbs[1]))
        answ.append(res)


    with open("answ.txt", "w", encoding="UTF-8") as file:
        for i in answ:
            file.write(i + '\n')
    return None

arithmetic("lol.txt")