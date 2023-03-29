import pytest

def func(x):
    return x + 1

def func2(y):
    return y - 5


def test_1():
    assert func(3) == 4


def test_2():
    assert func2(7) == 2



