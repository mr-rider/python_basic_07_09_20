"""
Task 2
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calculation(self, mass_sq_meter:float, fikness:float)->float:
        """
        расчет массы асфальта
        :param mass_sq_meter: float
        :param fikness: float
        :return: float
        """
        try:
            mass = (self._length * self._width * mass_sq_meter * fikness)/1000
        except ValueError:
            print("Ошибка типа данных")
            return mass


road = Road(5000, 20)
print(road.mass_calculation(25, 5))

