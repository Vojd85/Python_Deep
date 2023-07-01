# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

import sys
from random import randint

__all__ = ['guess']

LOW_LIMIT = 0
UP_LIMIT = 1001
COUNTS = 10


def guess(min, max, count):
    temp_count = 1
    num = randint(min, max)
    while temp_count <= count:
        number = int(input(f'Попытка {temp_count}. Введите число: '))
        if num == number:
            print('Вы угадали!')
            return True
        elif num < number:
            print('Число меньше')
        else:
            print('Число больше')
        temp_count += 1
    print(f'У вас закончились {count} попыток')
    return False


if __name__ == "__main__":
    _, *parameters = sys.argv
    print(guess(*map(int, parameters)))