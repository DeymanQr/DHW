import json
import random


class Person:
    def __init__(self):
        self.id = None
        self.name = None
        self.byear = None

    def input(self, id, name, byear):
        self.id, self.name, self.byear = id, name, byear

    def print(self):
        print(self.id, self.name, self.byear, end=' ')


class Passenger(Person):
    def __init__(self):
        super().__init__()
        self.dsity = None
        self.asity = None

    def input(self, id, name, byear, dsity, asity):
        super().input(id, name, byear)
        self.dsity, self.asity = dsity, asity

    def print(self):
        super().print()
        print(self.dsity, self.asity, end=' ')


class File_Reader:
    def __new__(cls, file_name, *args, **kwargs):
        with open(f"{file_name}.json", "r", encoding="UTF-8") as f:
            return json.load(f)


a = File_Reader('cities')
"""dpk = 10
price = 0"""

with open('cities.json', 'r', encoding='UTF-8') as f:
    cities_data = json.loads(f.read())

with open('passengers.json', 'r', encoding='UTF-8') as f:
    passengers_data = json.loads(f.read())

passengers = [Passenger() for _ in range(len(passengers_data))]
for i, j in enumerate(passengers):
    j.input(*passengers_data[i])

"""for i in passengers:
    for j in cities_data:
        if i.dsity == j[0] and i.asity == j[1] or i.dsity == j[1] and i.asity == j[0]:
            price += j[2] * dpk
            break

print(price)"""

cities = ["A", "B", "C", "D"]

passengers_updated = []
lol = True
for i in passengers:
    for k, j in enumerate(passengers_updated):
        if i.id == j.id:
            if i.dsity == j.asity and i.asity != j.dsity: # A -> B ; B -> D
                lol = False
                passengers_updated[k].dsity = j.dsity
            if i.dsity != j.asity and i.asity == j.dsity: # B -> C; A -> B
                lol = False
                asity, dsity = j.asity, i.dsity
                passengers_updated[k].asity, passengers_updated[k].dsity = asity, dsity
    if lol:
        passengers_updated.append(i)
    lol = True


max_length = 0
max_length_passenger = None

for i in passengers_updated:
    i.print()
    print()

for i in passengers_updated:
    for j in cities_data:
        if i.dsity == j[0] and i.asity == j[1] or i.dsity == j[1] and i.asity == j[0]:
            if max_length < j[2]:
                max_length, max_length_passenger = j[2], i

print(max_length_passenger.name, max_length)