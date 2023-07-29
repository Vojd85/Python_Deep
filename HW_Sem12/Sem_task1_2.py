# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k рассчитанных факториалов.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json

class Factorial:
    def __init__(self, k):
        self.k = k
        self.history = []

    def __call__(self, num):
        temp = 1
        for i in range(1, num):
            temp *= i
        self.history.append({num: temp})
        self.history = self.history[-self.k:]
        return temp
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        file_name = 'history.json'
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.history, f)

    def get_history(self):
        return self.history


calc = Factorial(4)
# for i in range(3, 12):
#     print(calc(i))
# print(calc.history)
with calc as _:
    for i in range(3,12):
        calc(i)
