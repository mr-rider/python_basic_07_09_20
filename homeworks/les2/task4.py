'''
 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если
в слово длинное, выводить только первые 10 букв в слове.
'''

list_string = input('Введите несколько слов, разделенных пробелами: ').split()

for id, word in enumerate(list_string):
    if len(word) > 10:
        word=word[:10]
    print(id+1, word)


