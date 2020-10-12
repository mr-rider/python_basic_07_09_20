"""
Task 4
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
"""

numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

try:
    with open('numbers_en.txt', 'r', encoding='UTF-8') as file_in:
        for line in file_in:
            number_en = line.split(' ')[0]
            number_ru = numbers_dict.get(number_en)
            print(number_ru)
            if number_ru is not None:
                line = line.replace(number_en, number_ru)

            with open('numbers_ru.txt', 'a', encoding='UTF-8') as file_out:
                file_out.write(line)

except IOError:
    print('Ошибка ввода вывода')

except ValueError:
    print('Ошибка типа данных')



