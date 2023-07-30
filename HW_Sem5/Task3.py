# Создайте функцию генератор чисел Фибоначчи
NUMBER_COUNT = 15

def fibonachi_gen(number: int):
    num1, num2 = 0, 1
    for _ in range(number):
        yield num1
        num1, num2 = num2, num1 + num2

print(*fibonachi_gen(NUMBER_COUNT))