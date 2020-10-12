"""
Task 4
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


"""
Task 5
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

"""
Task 6
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class Stock:
    stock_list = {}

    def __init__(self, stock_name):
        self.stock_name = stock_name

    def device_input(self, device_name: str, count: int):
        try:
            self.stock_list.update({device_name: int(count)})
        except ValueError:
           print('Ошибка ввода данных')

    def device_out(self, device_name: str, count: int):
        device_count = self.stock_list.get(device_name)
        if device_count is not None:
            try:
                device_count -= int(count)
                self.stock_list.update({device_name: device_count})
            except ValueError:
                print('Ошибка ввода данных')


class OfficeEquipment:
    def __init__(self, weight, length, height, count):
        self.weight = weight
        self.length = length
        self.height = height
        self.count = count


class Printer(OfficeEquipment):
    def __init__(self, weight, length, height, count, equipment_type, speed_of_print):
        super.weight = weight
        super.length = length
        super.height = height
        super.count = count
        self.equipment_type = equipment_type
        self.speed_of_print = speed_of_print

class Scaner(OfficeEquipment):
    def __init__(self, weight, length, height, count, equipment_type, resolution):
        super.weight = weight
        super.length = length
        super.height = height
        super.count = count
        self.equipment_type = equipment_type
        self.resolution = resolution

class Xerox(OfficeEquipment):
    def __init__(self, weight, length, height, count, equipment_type, speed_of_coping):
        super.weight = weight
        super.length = length
        super.height = height
        super.count = count
        self.equipment_type = equipment_type
        self.speed_of_coping = speed_of_coping


if __name__ == '__main__':
    stock = Stock('Irkutsk')

    stock.device_input('xerox', 6)

    print(stock.stock_list)

    stock.device_out('xerox', 2)

    print(stock.stock_list)


