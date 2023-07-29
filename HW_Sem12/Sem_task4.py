# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и 
# встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if value < 0:
            raise TypeError(f'Значение {value} должно быть положительным ')

class Rectangle:
    """Класс Прямоугольник имеющий свойства: length, width"""


    length = Range()
    width = Range()

    def __init__(self, *args):
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width, *_ = args

    def __str__(self) -> str:
        return f'Экземпляр класса Rectangle с длиной {self.length} и шириной {self.width}'
    
    @property
    def len(self):
        return self.length
    
    @property
    def wid(self):
        return self.width
    
    @len.setter
    def len(self, value):
        if value > 0:
            self.length = value
        else:
            raise ValueError('Значение должно быть больше нуля!')

    @wid.setter
    def wid(self, value):
        if value > 0:
            self.width = value
        else:
            raise ValueError('Значение должно быть больше нуля!')

    def get_perimeter(self):
        """Метод получения периметра"""
        return self.length * 2 + self.width * 2

    def get_square(self):
        """Метод получения площади"""
        return self.length * self.width
    

if __name__ == '__main__':
    rec_1 = Rectangle(5,6)
    rec_2 = Rectangle(7,4)
    print(rec_1)
    print(rec_2)

    # rec_1.len = -7
    # rec_2.wid = 12

    rec_1.length = -7
    rec_2.width = 12

    print(rec_1)
    print(rec_2)