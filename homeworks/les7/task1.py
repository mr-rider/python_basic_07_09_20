"""
task 1
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой
матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    matrix_lists = [[]]

    def __init__(self, matrix_lists):
        self.matrix_lists = matrix_lists

    def __str__(self):
        return '\n'.join(''.join(str(i)) for i in self.matrix_lists)

    def __add__(self, other):

        result = self.matrix_lists
        for i in range(len(self.matrix_lists)):
            for j in range(len(self.matrix_lists[i])):
                result[i][j] = self.matrix_lists[i][j] + other.matrix_lists[i][j]
        return result


if __name__ == '__main__':
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix + matrix2)



