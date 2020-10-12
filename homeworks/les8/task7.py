"""
Task 7
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    # z = a + bi
    def __init__(self, z: str, a: float, b: float):
        self.z = z
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.z} = {self.a} + {self.b}i'

    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        print(f'Z = {res_a} + {res_b}i')

    # z = z1⋅z2 = (a1a2−b1b2) + (a1b2 + b1a2)i
    def __mul__(self, other):
        res_a = self.a * other.a - self.b * other.b
        res_b = self.a * other.b + self.b * other.a
        print(f'Z = {res_a} + {res_b}i')


z1 = ComplexNumber('Z1', 2, 3)
print(z1)
z2 = ComplexNumber('Z2', -1, 1)
print(z2)

z1 + z2
z1 * z2





