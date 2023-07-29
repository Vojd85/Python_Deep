# Создайте класс Матрица. Добавьте методы для: 
# - вывода на печать
# - сравнения
# - сложения
# * умножения матриц

m = [[1,2,3],[5,9,3],[3,4,0]]
v = [[3,5,3],[1,4,9],[8,2,7]]

class Matrix:
    """Собственно класс Матрица представляющий из себя двумерный список"""
    def __init__(self, value:list= [[]]):
        self.value = value

    def __str__(self):
        return 'Экземпляр класса Matrix'
    
    def print(self):
        for item in self.value:
            print(" ".join(map(str, item)))
        return ''

    def get_size(self):
        return sum(1 for item in self.value), sum(1 for item in self.value[0])
    
    def __add__(self, other):
        if self.get_size() == other.get_size():
            result = [[self.value[i][j] + other.value[i][j]  for j in range
                      (len(self.value[0]))] for i in range(len(self.value))]
            return Matrix(result)
        raise ValueError('Размеры матриц неверны!')
    
    def __sub__(self, other):
        if self.get_size() == other.get_size():
            result = [[self.value[i][j] - other.value[i][j]  for j in range
                      (len(self.value[0]))] for i in range(len(self.value))]
            return Matrix(result)
        raise ValueError('Размеры матриц неверны!')

matrix_1 = Matrix(m)
matrix_2 = Matrix(v)
m_3 = matrix_1 + matrix_2
m_4 = matrix_1 - matrix_2
print(matrix_1.print())
print(matrix_2.print())
print(m_3.print())
print(m_4.print())
