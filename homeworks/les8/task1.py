"""
Task 1
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Data:
    user_data=''

    def __init__(self, user_data):
        self.user_data = user_data

    @classmethod
    def getdata(cls, data_str):
        data_splited =data_str.split('-')
        day = int( data_splited[0])
        month = int(data_splited[1])
        year = int(data_splited[2])
        print(f'День: {day}, месяц: {month}, год: {year}')
        return day, month, year

    @staticmethod
    def valid_data(day, month, year):
        if day > 0 and day <=31:
            print('Day valid')
        else:
            print('Day data error')
        if month > 0 and month <=12:
            print('Month valid')
        else:
            print('Month data error')
        if year > 0 :
            print('Year valid')
        else:
            print('Year data error')


day, month, year = Data.getdata('01-08-82')
Data.valid_data(day, month, year)

