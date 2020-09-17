"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    """
    x raise to power y
    :param x: positive int
    :param y: negative number
    :return: float
    """
    result = 0
    pow_res = 1
    while y:
        pow_res= pow_res*x
        y +=1

    result = 1 / pow_res


    return result

print(f'my_res: {my_func(2, -1)}')