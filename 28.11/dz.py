from abc import ABC, abstractmethod
import random


class AbstractFighter(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_damage(self):
        pass

    @abstractmethod
    def get_strength(self):
        pass

    @abstractmethod
    def get_agility(self):
        pass

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def attack(self, fighter):
        pass

    @abstractmethod
    def print_combat_history(self):
        pass

    @abstractmethod
    def heal(self, hp: int):
        pass

    @abstractmethod
    def deal_damage(self, hp: int):
        pass

    @abstractmethod
    def add_win(self):
        pass

    @abstractmethod
    def add_loss(self):
        pass


class Fighter(AbstractFighter):
    def __init__(self, name: str, damage: int, hp: int, strength: int, agility: int):
        if not isinstance(name, str):
            raise TypeError('attribute \'name\' must be string!')
        self._name = name
        if not isinstance(hp, int) or hp <= 0:
            raise TypeError('attribute \'damage\' must be positive integer!')
        self._damage = damage
        if not isinstance(hp, int) or hp <= 0:
            raise TypeError('attribute \'hp\' must be positive integer!')
        self._hp = hp
        self.__max_hp = hp
        if not isinstance(hp, int) or hp <= 0:
            raise TypeError('attribute \'strength\' must be positive integer!')
        self._strength = strength
        if not isinstance(hp, int) or hp <= 0:
            raise TypeError('attribute \'agility\' must be positive integer!')
        self._agility = agility
        self._wins = 0
        self._losses = 0

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_health(self):
        return self._hp

    def get_strength(self):
        return self._strength

    def get_agility(self):
        return self._agility

    def attack(self, fighter):
        if int(random.random() * 100) <= 100 - (fighter.get_strength() + fighter.get_agility()):
            fighter.deal_damage(self.get_damage())
            return True
        return False

    def print_combat_history(self):
        print(f'Name: {self.get_name()}, Wins: {self._wins}, Losses: {self._losses}')
        return

    def heal(self, hp: int):
        self._hp += hp
        if self._hp > self.__max_hp:
            self._hp = self.__max_hp
        return

    def deal_damage(self, hp: int):
        self._hp -= hp
        if self._hp <= 0:
            self._hp = 0
        return

    def add_win(self):
        self._wins += 1
        return

    def add_loss(self):
        self._losses += 1
        return


def battle(fighter1: Fighter, fighter2: Fighter):
    if fighter1.get_health() == 0:
        print(f'{fighter1.get_name()} is dead and can\' fight.')
        return
    if fighter2.get_health() == 0:
        print(f'{fighter2.get_name()} is dead and can\' fight.')
        return
    fighters = (fighter1, fighter2)
    ch = random.randint(0, 1)
    while fighter1.get_health() != 0 and fighter2.get_health() != 0:
        attack = fighters[ch].attack(fighters[(ch + 1) % 2])
        if attack:
            print(
                f'{fighters[ch].get_name()} makes {fighters[ch].get_damage()} damage to {fighters[(ch+1)%2].get_name()}'
            )
        else:
            print(f'{fighters[ch].get_name()} attack missed')
        ch += 1
        ch %= 2
    if fighter1.get_health() == 0:
        print(f'{fighter2.get_name()} has won!')
        fighter2.add_win()
        fighter1.add_loss()
    elif fighter2.get_health() == 0:
        print(f'{fighter1.get_name()} has won!')
        fighter1.add_win()
        fighter2.add_loss()
    return


fighter1 = Fighter('Maximus', 20, 100, 20, 15)
fighter2 = Fighter('Commodus', 25, 90, 25, 10)

battle(fighter1, fighter2)