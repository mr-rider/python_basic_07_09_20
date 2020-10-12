'''
4. Пользователь вводит целое положительное число.
 Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

user_number = input('Input number: ')
if user_number.isdigit():
    user_number = int(user_number)
else:
    print('You did\'t input number')


next_number = user_number
max_number = 0

while next_number:
    tmp = next_number % 10
    next_number = next_number // 10
    if max_number < tmp:
        max_number = tmp

print(f'Maximum number is : {max_number}')


