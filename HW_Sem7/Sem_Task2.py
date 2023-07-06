# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random as rnd

MIN = 4
MAX = 7

def get_names(count, name, min_symbol, max_symbol):
    letterA = 'йцукенгшщзхфывапролджэячсмитьбю'
    letterB = 'уеыаоэяю'
    with open(name, 'w', encoding='utf-8') as file:
        for _ in range(count):
            name = rnd.sample(letterA, rnd.randint(min_symbol, max_symbol))
            if not set(letterA) & set(letterB):
                half = len(name) // 2
                name = name[:half] + rnd.sample(letterB, half)
                rnd.shuffle(name)
            name = ''.join(name).capitalize()
            file.write(f'{name}\n')

if __name__ == '__main__':
    get_names(7, 'names.txt', MIN, MAX)