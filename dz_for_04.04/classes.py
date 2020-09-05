from random import randint
from time import sleep

class Unit1:
    def __init__(self, name="Unit", health=100, attack=20):
        self.name = name
        self.health = health
        self.attack = attack


    def Attack(self, who=None):
        if who != None:
            who.health -= self.attack
            print(f"{self.name} has attacked {who.name}\nHealth: {self.name} {self.health}; "
                  f"{who.name} {who.health}\n")


units = [Unit1("Gamer1", 100, 10), Unit1("Gamer2", 50, 20)]
while True:
    a = randint(0, 1)
    units[a].Attack(units[1-a])
    if units[1-a].health <= 0:
        print(f"{units[1-a].name} is dead")
        break
    sleep(0.2)