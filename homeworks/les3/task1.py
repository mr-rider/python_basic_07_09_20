"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def devision(num1, num2):
    '''
    devision num1 by num2
    :param num1: any number
    :param num2: any number, except zero
    :return:
    '''
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Деление на ноль")


    return result

print(devision(4, 0))