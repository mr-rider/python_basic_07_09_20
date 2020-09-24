"""
Task 6
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
 типы занятий. Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

learn_dict = {}
study_hours = 0
number = ''

try:
    with open('learn_hours.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            index = line.find(':')
            subject_key = line[:index]
            for char in line:
                if char.isdigit():
                    number = number + char
                elif number != '':
                    study_hours += int(number)
                    number = ''
            learn_dict[subject_key] = study_hours
            study_hours = 0
            print(learn_dict)
except IOError:
    print('Ошибка ввода вывода')
