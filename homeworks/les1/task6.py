'''
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
 Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена
составить не менее b километров. Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22

Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
'''

distance = input('Input distance in first day: ')
if distance.isdigit():
    distance = int(distance)
else:
    print('It\'s not a number')

aim_distance = input('Input your aim: ')
if aim_distance.isdigit():
    aim_distance = int(aim_distance)
else:
    print('It\'s not a number')

aim_day=1
current_distance = distance

while aim_distance > current_distance:
    current_distance += current_distance * 0.1
    aim_day +=1




print(f'Ответ: на {aim_day}-й день спортсмен достиг результата — не менее {aim_distance} км.')
