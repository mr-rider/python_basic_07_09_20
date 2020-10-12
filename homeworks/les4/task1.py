"""
Task 1.
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys


def pay_for_work (hours:float, rate_per_hour:float, bonus:float)->float:
    """
    Функция расчета заработной платы сотрудника.
    :param hours: float
    :param rate_per_hour: float
    :param bonus:float
    :return: float
    """
    pay = (float(hours) * float(rate_per_hour)) + float(bonus)
    return pay


if len(sys.argv) > 3:
       _, hours_arg, rate_per_hour_arg, bonus_arg = sys.argv
       print(f'Заработная плата сотрудника: {pay_for_work(hours_arg, rate_per_hour_arg, bonus_arg)}')

















