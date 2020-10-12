"""
Task2
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

count_line = 0
count_word_in_line = 0
try:
    with open('text.txt', 'r', encoding='UTF-8') as file:
        for data_string in file:
            count_line += 1
            count_word_in_line = len(data_string.split(' '))
            print(f'В строке {count_line} - {count_word_in_line} слов')
    print(f'Количество строк в файле: {count_line}')

except IOError:
    print('Input, Output error.')





