print('-----------------Задание 1-----------------------')

"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, list_of_lists):
        self.mat = list_of_lists

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                summa = other.mat[i][j] + self.mat[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.mat[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


a = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
b = [[2, 3, 3], [-2, 1, -6], [5, -3, 0]]
m = Matrix(a)
mm = Matrix(b)

print("\nМатрица №1")
print(m.__str__(), "\n")

print("Матрица №2")
print(mm.__str__(), "\n")

print("Сумма матриц №1 и №2")
print(m + mm)

#print('-------------------------------------------------')

print('-----------------Задание 2-----------------------')

"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_method_1(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def my_method_2(self):
        print("Параметры одежды:", end=' ')

    @abstractmethod
    def my_method_3(self):
        print("Расход ткани:", end=' ')


class Coat (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Пальто")

    def my_method_2(self):
        super().my_method_2()
        print("Размер")

    def my_method_3(self):
        super().my_method_3()
        return float(self.value) / 6.5 + 0.5


class Suit (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Костюм")

    def my_method_2(self):
        super().my_method_2()
        print("Рост")

    def my_method_3(self):
        super().my_method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 3           # введите размер пальто
size_suit = 4           # введите размер костюма

print("\n")
c = Coat(size_coat)
c.my_method_1()
c.my_method_2()
print("%.2f" % c.my_method_3())


print("\n")
s = Suit(size_suit)
s.my_method_1()
s.my_method_2()
print("%.2f" % s.my_method_3())


t = Total(size_coat, size_suit)
print("\nОбщий расход ткани: %.2f" % t.sum())

#print('-------------------------------------------------')

print('-----------------Задание 3-----------------------')

"""Реализовать программу работы с клетками. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение ( __add__() ), вычитание ( __sub__() ), умножение ( __mul__() ), деление ( __truediv__()) .
Данные методы должны выполнять увеличение, уменьшение, умножение и обычное (не
целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
округление значения до целого числа.
В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса и
количество клеток в ряду. Метод должен возвращать строку виду * ****\n*****\n*****. .., где
количество клеток между \n равно переданному аргументу, а количество рядов определяется,
исходя из общего количества клеток.
При создании экземпляра клетки должна происходить перезапись параметра, который хранит
количество клеток."""


class Cell:
    def __init__(self, quan_c):
        self.quan_c = quan_c        # количество клеток quantity cell

    def __add__(self, other):
        return self.quan_c + other

    def __sub__(self, other):
        return self.quan_c - other

    def __mul__(self, other):
        return self.quan_c * other

    def __truediv__(self, other):
        return round(self.quan_c / other)

    def make_cell(self, cell_in_row):       # количество клеток в ряду
        self.cell_fall = ""
        while self.quan_c > 0:
            self.quan_c -= cell_in_row
            if self.quan_c < 0:
                self.cell_fall += ("*" * (cell_in_row + self.quan_c) + "\n")
            else:
                self.cell_fall += ("*" * cell_in_row + "\n")
        return self.cell_fall

    def __call__(self, new_quan_c):
        self.quan_c = new_quan_c


c = Cell(52)                # введите количество клеток
print(c.make_cell(10))      # количество клеток в ряду
print(c+15)
c(99)
print(c.quan_c)
print(c/2)

print('-------------------------------------------------')