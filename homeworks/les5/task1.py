"""
Task1
1. Создать программно файл в текстовом формате, записать в него построчно данные
 вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

user_string = ' '
try:
    with open('text.txt', 'a', encoding='UTF-8') as file:
        while user_string:
            user_string = input('Введите строку: ')
            file.write(user_string + '\n')

except IOError:
    print('Input Output error')