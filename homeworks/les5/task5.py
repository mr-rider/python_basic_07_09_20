"""
Task 5
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
sum_of_numbers = 0


def file_of_numbers(file_out:str, first_num:int, last_num:int):
    try:
        with open(file_out, 'a') as file:
            for num in range(first_num, last_num + 1):
                file.write(str(num))
                if num < (last_num):
                    file.write(' ')
    except IOError:
        print('Ошибка ввода вывода')


# file_of_numbers('sum_numbers.txt', 1, 10)

try:
    with open('sum_numbers.txt', 'r') as file:
        string_num = file.read()
        str_split = string_num.split(' ')

        for number in str_split:
            sum_of_numbers += int(number)

        print(f'Сумма чисел в файле {sum_of_numbers}')
except IOError:
    print('Ошибка ввода вывода')
except ValueError:
    print('Ошибка данных')


