'''
  2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

list_data = []
while True:
    count_el = input('Введите количество элементов: ')
    if count_el.isdigit():
        count_el = int(count_el)
        break
    else:
        print('Введите число!')

for i in range(count_el):
    list_data.append(input(f'Введите {i+1}-й элемент: '))
print(f'Исходный список: {list_data}')

if count_el % 2:
   count_el -= 1

for element in range(0, count_el, 2):
    list_data[element], list_data[element + 1] = list_data[element + 1], list_data[element]


print(f'Изменненый список: {list_data}')