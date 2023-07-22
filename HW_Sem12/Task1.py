# Создайте класс студента. 
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и 
# наличие только букв. 
# - Названия предметов должны загружаться из файла CSV при создании 
# экземпляра. Другие предметы в экземпляре недопустимы. 
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты 
# тестов (от 0 до 100). 
# - Также экземпляр должен сообщать средний балл по тестам для каждого 
# предмета и по оценкам всех предметов вместе взятых. 

import csv

objects = ['Литература', 'Физика', 'Алгебра', 'Пение', 'Физ-ра']
file = 'HW_Sem12/objects.csv'
with open(file, 'w', encoding='utf-8') as f:
    csv_write = csv.writer(f, lineterminator='\r')
    for item in objects:
        csv_write.writerow([item])


class Validate:
    def __init__(self, *args):
        self.predicate = args

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        for param in self.predicate:
            if not param(value):
                raise ValueError('ФИО должны быть с большой буквы и иметь только буквы!')


class Student:
    MAX_TEST = 100

    name = Validate(str.istitle, str.isalpha)
    surname = Validate(str.istitle, str.isalpha)
    patronymic = Validate(str.istitle, str.isalpha)

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        with open(file, 'r', encoding='utf-8') as csv_file:
            temp = {}
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                temp[row[0]] = {'estimations': [], 'tests':[]}
        self._journal = temp
        self._upgrade = False
        
    def __str__(self):
        return f'Студент {self.name} {self.surname} {self.patronymic}'
    
    def fill_journal(self):
        for obj in self._journal.keys():
            temp = input(f'Введите через пробел оценки (значения от 2х до 5) по предмету {obj}: ').split()
            for digit in temp:
                if int(digit) not in range(2, 6):
                    raise ValueError('Оценки должны быть от 2 до 5')
            self._journal[obj]['estimations'] = temp
            temp = input(f'Введите через пробел результаты тестов (значения от 0 до 100) по предмету {obj}: ').split()
            for digit in temp:
                if int(digit) not in range(101):
                    raise ValueError('Результаты должны быть от 0 до 100')
            self._journal[obj]['tests'] = temp
        self._upgrade = True
        
    def info(self):
        print(self)
        estimations = []
        if self._upgrade:
            for key, value in self._journal.items():
                estimations.append(sum(map(int, value['estimations'])) / len(value['estimations']))
                print(f"Средний балл тестов по предмету {key} : {round(sum(map(int, value['tests'])) / len(value['tests']))}")
            print(f'Средний балл по оценкам всех предметов {sum(map(int, estimations)) / len(estimations)}')
        else:
            print('Нет данных')
        


if __name__ == '__main__':
    stud_1 = Student('Egor', 'Ara', 'Bulgakov')
    print(stud_1)
    stud_1.fill_journal()
    stud_1.info()