import pytest
from proga import count_symbol


def test_count_symbol_1():
    assert count_symbol('a', 'Hello, world!') == 0


def test_count_symbol_2():
    assert count_symbol('h', 'Hello, world!') == 1


def test_count_symbol_3():
    assert count_symbol(' ', 'Hello, world!') == 1


def test_count_symbol_4():
    assert count_symbol('o', 'Hello, world!') == 2


def test_count_symbol_5():
    assert count_symbol('8', 'Hello, world!') == 0
