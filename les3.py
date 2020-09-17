from typing import Callable, Iterable, List
"""
map
zip
round
sum
filter
min
max
abs
sort
reduce
"""


def my_map(func: Callable, some: Iterable) -> List:
    """
    Реализация функции map
    :param func: call object
    :param some: iterable object
    :return: list result
    """
    result = []
    for itm in some:
        result.append(func(itm))

    return result

def some_append(itm, some: list) -> list:
    some.append(itm)
    return some

a = [1,2,3,4,5]
#b = my_map(str, a)
#c = my_map(some=a, func=str)

some = ['1', '2']

b = some_append('HELLO', a)
print(b)

#all  all true
#any - any true


def some_f(*args):
    """
    много позиционных аргументов
    :param args:
    :return:
    """
    print(type(args))
    print(args)


def my_min(*args: int, **kwargs):
    result = float('inf')
    for itm in args:
        if result > itm:
            result = itm
    return result