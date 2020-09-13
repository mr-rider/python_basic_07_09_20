'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

list_sessons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето',  'осень',
                'осень', 'осень', 'зима']
dict_sessons = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето',
                7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

while True:
    mounth_number = input('Введите номер месяца: ')
    if mounth_number.isdigit():
        mounth_number = int(mounth_number)
        if mounth_number in range(1, 13):
            break
        else:
            print('Номер месяца должен быть от 1 до 12')
    else:
        print('Введите число')


print(f'{mounth_number}-й месяц {list_sessons[mounth_number - 1]}')
print(f'{mounth_number}-й месяц {dict_sessons.get(mounth_number)}')