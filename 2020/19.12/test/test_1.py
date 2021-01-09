import pytest
from proga import count_sum

def test_count_sum_1():
    assert count_sum('15762') == 21

def test_count_sum_2():
    assert count_sum('08352') == 18

def test_count_sum_3():
    assert count_sum('67254') == 24

def test_count_sum_4():
    assert count_sum('40976') == 26

def test_count_sum_5():
    assert count_sum('13553') == 17

def test_count_sum_6():
    assert count_sum('87532') == 25

def test_count_sum_7():
    assert count_sum('05321') == 11

def test_count_sum_8():
    assert count_sum('24512') == 14

def test_count_sum_9():
    assert count_sum('12352') == 13

def test_count_sum_10():
    assert count_sum('46423') == 19

