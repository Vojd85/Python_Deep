# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки

from random import randint as ri

BOARD = 8
QUEENS_COUNT = 8
MIN_RND = 0
MAX_RND = 7
SUCCESS_COUNT = 4


def no_fight(queens_coor: tuple) -> bool:
    list_row = [x[0] for x in queens_coor]
    list_col = [y[1] for y in queens_coor]
    for queen in queens_coor:
        if list_row.count(queen[0]) != 1 or list_col.count(queen[1]) != 1 \
            or queen[0] in list_col or queen[1] in list_row:
            return False
    return True

def good_position(count, count_queens):
    result = []
    while count:
        temp = tuple((ri(MIN_RND,MAX_RND), ri(MIN_RND,MAX_RND)) for _ in range(count_queens))
        if no_fight(temp):
            result.append(temp)
            count -= 1
    return result


print(*good_position(SUCCESS_COUNT, QUEENS_COUNT), sep='\n')
