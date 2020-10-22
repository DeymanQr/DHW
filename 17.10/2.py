import string
import random


class Human:
    def __init__(self, height, mass, birthday_date, eyes_color):
        self.height = height
        self.mass = mass
        self.birthday_data = birthday_date
        self.eyes_color = eyes_color


    def __eq__(self, other):
        return self.height + self.mass == other.height + other.mass

    def __lt__(self, other):
        return self.height + self.mass < other.height + other.mass

    def __gt__(self, other):
        return self.height + self.mass > other.height + other.mass

    def change_height(self, new_height):
        self.height = new_height

    def change_mass(self, new_mass):
        self.mass = new_mass

    def change_birthday_date(self, new_birthday_date):
        self.birthday_data = new_birthday_date

    def change_eyes_color(self, new_eyes_color):
        self.eyes_color = new_eyes_color


class Student(Human):
    def __init__(self, height, mass, birthday_date, eyes_color, stydy_date, specialization):
        super().__init__(height, mass, birthday_date, eyes_color)
        self.study_date = stydy_date
        self.specialization = specialization
        self.last_cursach = 0

    def write_kursach(self, lines, simbols_in_line):
        self.last_cursach += 1
        with open(f'kursach{self.last_cursach}.txt', 'w', encoding='UTF-8') as f:
            for i in range(lines):
                line = ''.join([random.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(simbols_in_line)])
                """
                line = string.digits + string.ascii_letters + string.punctuation
                random.shuffle(line)
                line = line[:simbols_in_line]
                """
                f.write(line + '\n')
            f.write(f"{self.study_date} {self.specialization}\n")

    def change_study_date(self, new_study_date):
        self.study_date = new_study_date

    def change_specialization(self, new_specialization):
        self.specialization = new_specialization


a = Human(175, 85, 2007, 'grey')