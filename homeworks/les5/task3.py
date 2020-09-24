"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

count_line = 0
sum_pay = 0

try:
    with open('wokers_data.txt', 'r', encoding='UTF-8') as file:

        for strings in file:
            list_splited = strings.split(' ')[1]
            pay = float(list_splited)
            sum_pay += pay
            count_line += 1
            if float(list_splited) < 20000:
                print('Зарплата меньше 20000: ')
                print(strings.split(' ')[0])

        mean = sum_pay/count_line
        print(f'Средняя величина дохода: {round(mean, 2)}')


except IOError:
    print('Input, Output error.')
except ValueError:
    print('Ошибка ввода данных ')