import inspect
import sys


def plus(a, b):
    if not a and not b:
        raise ValueError('bad params')
    return a + b


def test1():
    assert plus(2, 2) == 4


def test2():
    assert plus(100, 9) == 109, 'Неверное значение'


def test3():
    assert plus(-1, 1) == 0


def test_zero():
    assert plus(0, 1) == 1

# генератор
# def my_range(start, end=None):
#     if end is None:
#         start, end = 0, start
#     while start < end:
#         yield start
#         start += 1
#
#
# r = my_range(1, 3)
# for i in r:
#     print(i)
