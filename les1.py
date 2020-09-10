# PEP 8
# varible
#snake_case = 1
#class
#CamelCase = 2


some_str = "Hello my friends"   # str()
some_str2 = 'Hello my friends'

some_int = 1     # int()
some_float = 2.3333     # float()
some_bool = True        # bool()

ask_name = " Введите имя \n"
ask_age = " Введите возраст \n"
name = input(ask_name)

#print('Привет', name, end = '!!!!!\n', sep='-----')

age = input(ask_age)

if age.isdigit():
    age = int(age)

    if age >= 18:
        print('Доступ к разделам XXX открыт')
    elif age > 16:
        print('Доступ к боевикам открыт')
    else:
        print("Смотри мультики")
else:
    print("Введено не число")

# последняя цифра
#a = 123456
#last_number = a % 10

# Без последней
# a // 10

a = 123456

while a:
    tmp = a % 10
    a = a // 10
    if tmp == 5:
        continue # пропустить следующиие операторы
        # break прервать цикл

    print(tmp, a)


# Проверить  тип переменной isinstance(2.0, int)





