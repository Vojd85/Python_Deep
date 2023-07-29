# Создайте класс МояСтрока где будут доступны все возможности str и 
# дополнительно хранится имя автора строки и время создания (time.time)

import time

class My_String(str):
    """My own string class"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance
    
    # def __init__(self, value, name):

    
    def __str__(self):
        return f'Экземпляр класса My_String. Автор {self.name}. Время создания {self.time}'


string_1 = My_String('new', 'string_1')
print(string_1)
print(string_1.upper())
print(string_1.title())
print(string_1.time)
print(string_1.name)