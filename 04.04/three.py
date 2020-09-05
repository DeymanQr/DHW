from two import add_el_1
from random import randint, choice

names = ["Андрей", "Арсений", "Богдан", "Влад", "Глеб", "Даниил", "Евгений", "Захар", "Игорь", "Михаил"]
surnames = ["Волков", "Иванов", "Перец", "Шевченко", "Морозов", "Захаров", "Королев", "Баланко", "Бахтин", "Авдеенко"]


def generator():
    for i in range(100):
        yield [choice(names), choice(surnames), randint(100, 10000)]


spis = generator()
dict1 = {}
for i in range(100):
    kek = next(spis)
    add_el_1(dictt=dict1, key=f"{kek[0]} {kek[1]}", item=kek[2])
print(dict1)