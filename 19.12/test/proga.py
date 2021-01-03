import random
import pytest


def count_sum(string: str):
    return sum([int(i) for i in string if i.isdigit()])


def get_random_number(x: int):
    return random.randint(1, x)


def count_symbol(id: str, string: str):
    return string.lower().count(id)
