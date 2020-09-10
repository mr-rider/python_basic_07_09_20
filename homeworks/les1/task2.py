"""
    Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""

time_in_seconds = input('Input time in seconds: ')
if time_in_seconds.isdigit():
    time_in_seconds = int(time_in_seconds)
else:
    print('It is not the seconds')

hours = time_in_seconds // 3600

minutes = (time_in_seconds % 3600) // 60

seconds = (time_in_seconds % 3600) % 60

print(f'Time is {hours}:{minutes}:{seconds} ')





