"""
Task 2
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = ''

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cloth_rate(self):
        pass


class Coat(Clothes):

    v = 0

    def __init__(self, name, v):
        self.name = name
        self.v = v

    @property
    def cloth_rate(self):
        result_rate = self.v / 6.5 + 0.5
        return result_rate

class Suit(Clothes):
    h = 0

    def __init__(self, name, h):
        self.name = name
        self.h = h

    @property
    def cloth_rate(self):
        result_rate = self.h * 2 + 0.3
        return result_rate

if __name__ == '__main__':
    coat = Coat('coat1', 6.5)
    print(coat.cloth_rate)

    suit = Suit('suit1', 3)
    print(suit.cloth_rate)

