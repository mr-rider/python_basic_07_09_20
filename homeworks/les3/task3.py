"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""

def my_func (num1,num2,num3):
    """
    sum of two bigest numbers from free
    :param num1: any number
    :param num2: any number
    :param num3: any number
    :return: int
    """
    num_list = [num1, num2, num3]
    result = sum(num_list) - min(num_list)
    return result


print(my_func(4,5,1))