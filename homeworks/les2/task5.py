'''
 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]
print(f'Исходный рейтинг: {my_list}')

while True:
    new_element = input('Введите число: ')
    if new_element.isdigit():
        new_element =int(new_element)
        break


my_list.append(new_element)
my_list.sort()
my_list.reverse()
print(my_list)