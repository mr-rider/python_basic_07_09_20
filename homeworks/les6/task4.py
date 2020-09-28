"""
Task 5
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = True

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        self.type = type
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        self.type = type
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        self.type = type
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        self.type = type
        super().__init__(speed, color, name, is_police)


car = Car(50, 'red', 'Toyota', False )
print(car.speed)
print(car.color)
print(car.name)
print(car.is_police)
car.show_speed()
car.go()
car.stop()
car.turn('Лево')


town_car = TownCar(70, 'blue', 'BMW', False, 'Town car' )
print(town_car.speed)
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
print(town_car.type)
town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('Право')

sport_car = SportCar(155, 'white', 'Ferrari', False, 'Sport Car' )
print(sport_car.speed)
print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
print(sport_car.type)
sport_car.show_speed()
sport_car.go()
sport_car.stop()
sport_car.turn('Право')


work_car = WorkCar(55, 'orange', 'Zil', False, 'Work Car' )
print(work_car.speed)
print(work_car.color)
print(work_car.name)
print(work_car.is_police)
print(work_car.type)
work_car.show_speed()
work_car.go()
work_car.stop()
work_car.turn('Право')

police_car = PoliceCar(120, 'White-Blue', 'Ford', True, 'Police Car' )
print(police_car.speed)
print(police_car.color)
print(police_car.name)
print(police_car.is_police)
print(police_car.type)
police_car.show_speed()
police_car.go()
police_car.stop()
police_car.turn('Лево')
