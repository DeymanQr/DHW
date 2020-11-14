from abc import ABC, abstractmethod
from typing import Optional, List
from datetime import datetime
import random
from string import ascii_lowercase


class AbstractTask(ABC):
    pass


class AbstractNote(ABC):
    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def add_task(self, note):
        pass

    @abstractmethod
    def del_task(self, id):
        pass

    @abstractmethod
    def change_task(self, id, **kwargs):
        pass


class AbstractBook(ABC):
    @abstractmethod
    def add_note(self, note):
        pass

    @abstractmethod
    def del_note(self, id):
        pass

    @abstractmethod
    def change_note(self, id, **kwargs):
        pass


class IdError(Exception):
    pass


class Task(AbstractTask):
    def __init__(self, id: int, text: str, is_made: Optional[bool] = False):
        self._id = id
        self._text = text
        self._is_made = is_made

    def __str__(self):
        return "; ".join((f"{str(i)[1:]}: {str(self.__dict__[i])}" for i in ('_id', '_text', '_is_made')))


class Note(AbstractNote):
    def __init__(self, id: int, url: str, tasks: Optional[List[Task]] = None):
        self._id = id
        self._url = url
        self.tasks = tasks
        self._make_data = datetime.now().strftime("%d|%m|%Y")
        if tasks is None:
            self._tasks = []

    def __iter__(self):
        for i in self._tasks:
            yield i

    def write(self):
        with open(self._url, "w", encoding="UTF-8") as f:
            for i in self._tasks:
                f.write(str(i)+'\n')
            f.write(self._make_data + "\n")
        return

    def add_task(self, task: Task):
        for i in self._tasks:
            if i._id == task._id:
                raise IdError('Task with this id is already in Note.')
        self._tasks.append(task)
        return

    def del_task(self, id: int):
        for i in self._tasks:
            if i._id == id:
                self._tasks.remove(i)
        return

    def change_task(self, id: int, **kwargs):
        for i in kwargs:
            self.__dict__[f"task_{str(id)}"].__dict__[str(i)] = kwargs[i]

    def __getattr__(self, item: str) -> Task:
        if item[:5] == 'task_' and item[5:].isdigit():
            for i in self._tasks:
                if i._id == int(item[5:]):
                    return i


class Book(AbstractBook):
    def __init__(self, notes: Optional[List[Note]] = None):
        self._notes = []
        if notes is None:
            self._notes = []

    def __iter__(self):
        for i in self._notes:
            yield i

    def add_note(self, note: Note):
        for i in self._notes:
            if i._id == note._id:
                raise IdError('Note with this id is already in Book.')
        self._notes.append(note)
        return

    def del_note(self, id: int):
        for i in self._notes:
            if i._id == id:
                self._notes.remove(i)
        return

    def change_note(self, id, **kwargs):
        for i in kwargs:
            self.__dict__[f"note_{str(id)}"].__dict__[str(i)] = kwargs[i]


    def __getattr__(self, item: str) -> Note:
        if item[:5] == 'note_' and item[5:].isdigit():
            for i in self._notes:
                if i._id == int(item[5:]):
                    return i


book = Book()
for i in range(10):
    book.add_note(Note(i+1, 'note_'+str(i+1)+'.txt'))
    for j in range(3):
        book.__dict__['_notes'][-1].add_task(
            Task(j+1, "".join([random.choice(ascii_lowercase)for i in range(random.randint(50, 100))]))
        )

for i in book:
    i.write()
