import random

NAMES = ('Шарик', 'Бобик', 'Пират')


class Animal:
    _name = 'SOME NAME' # модификатор доступа protected
    __age = 0   # модификатор доступа privat
    _mass = 1
    _population = []

    def __init__(self, a_type, mass):
        print(id(self))
        self.a_type = a_type
        self.mass = mass
        self._population.append(self)

    def say(self):
        print(f'{self.a_type} say: ваыдоуывадо')

    def get_age(self):
        return self.__age

    def get_population(self):
        return tuple(self.__population)

    def breeding(self, other):
        cls = random.choice((type(self), other))
        return cls(self.a_type, random.randint(1, 10))

class Dog(Animal):
    def __init__(self, name ):
        self.name = name
        super().__init__('Собака', random.randint(1, 3))

    def say(self):
        super().say()
        print('ГАВ ГАВ')

    def breeding(self, other):
        cls = random.choice((type(self), other))
        return cls(random.choice(NAMES))

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__('Кошка', random.randint(1, 3))

    def say(self):
        print('МЯУ')


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = {}

    def add_animal(self, animal):
        if self.__animals.get(animal.a_type):
            self.__animals.get(animal.a_type).append(animal)
        else:
            self.__animals[animal.a_type] = [animal]

    def atype_population(self, atype):
        return self.__animals.get(atype)


zoo = Zoo('')

animal1 = Animal('Пес', 27)
dog1 = Dog('Шарик')
dog2 = Dog('Хатико')
print(id(animal1))
animal12 = Animal('Кот', 8)
print(id(animal12))

cat1 = Cat('Барсик')
cat2 = Cat('Борис')

