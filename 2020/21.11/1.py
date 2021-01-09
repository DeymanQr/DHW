from abc import ABC, abstractmethod
#from typing import Optional, List
from datetime import datetime
#import random
#from string import ascii_lowercase


class AbstractBook(ABC):
    @abstractmethod
    def update_arg(self, arg, value):
        pass

    @abstractmethod
    def get_notes(self):
        pass


class AbstractNote(ABC):
    @abstractmethod
    def update_arg(self, arg, value):
        pass

    @abstractmethod
    def get_tasks(self):
        pass

    @abstractmethod
    def write(self):
        pass


class AbstractTask(ABC):
    @abstractmethod
    def update_arg(self, arg, value):
        pass


class Book(AbstractBook):
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def update_arg(self, arg, value):
        if arg == 'id':
            raise IndexError('не трогать id!')
        self.__dict__[arg] = value
        return

    def get_notes(self):
        return [i for i in Notes if i.book_id == self.id]

    def del_book(self):
        Books.remove(self)
        for i in self.get_notes():
            i.del_note()
        for i in self.__dict__.keys():
            self.__dict__[i] = None


class Note(AbstractNote):
    def __init__(self, id: int, name: str, path: str, book_id: int):
        self.id = id
        self.name = name
        self.path = path
        self.book_id = book_id

    def update_arg(self, arg, value):
        self.__dict__[arg] = value
        return

    def get_tasks(self):
        return [i for i in Tasks if i.note_id == self.id]

    def write(self):
        with open(self.path, 'w', encoding='UTF-8') as f:
            tasks = self.get_tasks()
            tasks.sort(key=lambda task: task.id)
            for i in tasks:
                f.write(str(i) + '\n')
                f.write(datetime.now().strftime("%d.%m.%Y") + '\n')

    def del_note(self):
        Notes.remove(self)
        for i in self.get_tasks():
            i.del_task()
        for i in self.__dict__.keys():
            self.__dict__[i] = None


class Task(AbstractTask):
    def __init__(self, id: int, name: str, content: str, note_id: int, is_made: bool = False):
        self.id = id
        self.name = name
        self.content = content
        self.is_made = is_made
        self.note_id = note_id

    def __str__(self):
        return '; '.join([f'{i}: {self.__dict__[i]}' for i in ('name', 'content', 'is_made')])

    def update_arg(self, arg, value):
        self.__dict__[arg] = value
        return

    def del_task(self):
        Tasks.remove(self)
        for i in self.__dict__.keys():
            self.__dict__[i] = None


class NazovuPotomList:
    def __init__(self):
        self.ch = 0

    def __iter__(self):
        for i in range(self.ch):
            yield self.__dict__[str(i)]

    def __len__(self):
        return self.ch

    def __repr__(self):
        return '|' + ', '.join([repr(i) for i in self.__iter__()]) + '|'

    def __getitem__(self, item):
        return self.__dict__[str(item)]

    def add(self, obj):
        if self.ch == 0 or type(self.__dict__['0']) == type(obj):
            self.__dict__[str(self.ch)] = obj
            self.ch += 1

    def remove(self, obj):
        for i in range(self.ch):
            if self.__dict__[str(i)] == obj:
                for j in range(i+1, self.ch):
                    self.__dict__[str(j)] = self.__dict__[str(j - 1)]
                del self.__dict__[str(self.ch-1)]
                self.ch -= 1
                return


Books = NazovuPotomList()
Notes = NazovuPotomList()
Tasks = NazovuPotomList()

for i in range(2):
    Books.add(Book(i+1, 'lol'))
    for j in range(3):
        Notes.add(Note(j+1, f'note{j+1}', f'note{j+1}.txt', i+1))
        for k in range(5):
            Tasks.add(Task(k+1, f'task{k+1}', 'Ctoto-kakto', j+1))

print(Books, Notes, Tasks, sep='\n')

Books[0].del_book()

print(Books, Notes, Tasks, sep='\n')