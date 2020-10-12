"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

result_list = []
firm_dict = {}
average_dict = {}
profit_list = []

try:
    with open('firms.txt', 'r') as file_in:
        for line in file_in:
            profit = float(line.split(' ')[2]) - float(line.split(' ')[3])
            firm_dict[line.split(' ')[0]] = profit
            if profit > 0:
                profit_list.append(profit)

    average_dict["average_profit"] = round(sum(profit_list) / len(profit_list), 2)
except IOError:
    print("Ошибка ввода вывода")
except ValueError:
    print("Ошибка ввода данных")


result_list.append(firm_dict)
result_list.append(average_dict)


try:
    with open("firms_json.json", "w") as file_out:
        json.dump(result_list, file_out)

except IOError:
    print("Ошибка записи данных")



