'''
5. Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
  или убыток — издержки больше выручки). Выведите соответствующее сообщение.
  Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
  Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

proceeds = input('Input proceeds: ')
if proceeds.isdigit():
    proceeds = int(proceeds)
else:
    print('It\'s not a number')

costs = input('Input costs: ')
if costs.isdigit():
    costs = int(costs)
else:
    print('It\'s not a number')

if proceeds > costs:
    print('You in profit.')

    profitability = (proceeds - costs) / proceeds
    print(f'Your profitability: {profitability} ')
elif proceeds < costs:
    print('You are declining.')
else:
    print('In the middle.')

workers_count = input('Input count of workers: ')
if workers_count.isdigit():
    workers_count = int(workers_count)
else:
    print('It\'s not a number')

worker_profit = (proceeds - costs)/workers_count
print(f'Worker profit: {worker_profit}')



