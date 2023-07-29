# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. 
# При этом должен создаваться новый экземпляр прямоугольника. 
# Складываем и вычитаем периметры, а не длинну и ширину. 
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """Класс Прямоугольник имеющий свойства: length, width"""

    def __init__(self, *args):
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width, _ = args

    def __add__(self, other):
        """Метод сложения"""
        p = self.get_perimeter() + other.get_perimeter()
        return Rectangle(p // 2 / 2)

    def __sub__(self, other):
        """Метод вычитания"""
        p = self.get_perimeter() - other.get_perimeter()
        return Rectangle(abs(p // 2 / 2))
    
    def __eq__(self, other):
        """Метод проверки на идентичность"""
        return self.get_square() == other.get_square()
    
    def __ne__(self, other):
        """Метод проверки на не идентичность"""
        return self.get_square() != other.get_square()

    def __gt__(self, other):
        """Метод который проверяет является ли данный прямоугольник больше другого"""
        return self.get_square() > other.get_square()

    def __lt__(self, other):
        """Метод который проверяет является ли данный прямоугольник меньше другого"""
        return self.get_square() < other.get_square()

    def __ge__(self, other):
        """Метод который проверяет является ли данный прямоугольник больше или равен другому"""
        return self.get_square() >= other.get_square()

    def __le__(self, other):
        """Метод который проверяет является ли данный прямоугольник меньше или равен другому"""
        return self.get_square() <= other.get_square()
    
    def __str__(self):
        return f'Экземпляр класса Rectangle с длиной {self.length} и шириной {self.width}'
    
    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'
    
    def get_perimeter(self):
        """Метод получения периметра"""
        return self.length * 2 + self.width * 2

    def get_square(self):
        """Метод получения площади"""
        return self.length * self.width
    
    


rec_1 = Rectangle(5)
rec_2 = Rectangle(7)
print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3.length = }\n{rec_3.width = }')
print(f'{rec_4.length = }\n{rec_4.width = }')
print(rec_3 > rec_4)
print(rec_3 != rec_4)
print(Rectangle.__doc__)
help(Rectangle)