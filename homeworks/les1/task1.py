"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
  запросите у пользователя несколько чисел и строк и сохраните в переменные,
  выведите на экран.
"""

some_str = "Hello"
some_int = 33

print(f'some_var = {some_str}')
print(f'some_int = {some_int}')

user_number = input('Input number: ')
if user_number.isdigit():
     user_number = int(user_number)
     print(f'number = {user_number}')
else:
    print('It\'s not the number' )

user_string = input('Input string:')
print(f'Your string is -\"{user_string}\"')



