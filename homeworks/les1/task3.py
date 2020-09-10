'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

user_number = input('Input any number: ')
if user_number.isdigit():
    user_number = int(user_number)
else:
    print('You did\'t input number')

count = user_number
next_number = user_number
sum = 0
while count:
    print(f'next_number = {next_number} ')
    sum += next_number
    next_number = next_number * 10 + user_number
    count -= 1

print(f'Result sum : {sum}')