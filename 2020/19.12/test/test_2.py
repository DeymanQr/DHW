import pytest
from proga import get_random_number

def test_get_random_number_1():
    assert isinstance(get_random_number(12), int)


def test_get_random_number_2():
    assert get_random_number(12) <= 12


def test_get_random_number_3():
    assert isinstance(get_random_number(20), int)


def test_get_random_number_4():
    assert get_random_number(20) <= 20


def test_get_random_number_5():
    assert isinstance(get_random_number(123), int)


def test_get_random_number_6():
    assert get_random_number(123) <= 123
