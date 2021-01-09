dictt = {}
with open("kek.txt", "r", encoding="UTF-8") as file:
    for i in file:
        line = i.strip().split() # apple - яблоко, яблочко;  --> ['apple', '-', 'яблоко,', 'яблочко;']
        for j in line[2:]: # без англ слова и "-"
            dictt[j[:-1]] = line[0] # {"яблоко": "apple"}
with open("kek_naoborot.txt", "w", encoding="UTF-8") as file:
    for i in dictt.keys():
        line = i + " - " + dictt[i] + ";\n" # "яблоко - apple;\n"
        file.write(line)