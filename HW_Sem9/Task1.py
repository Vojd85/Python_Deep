# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
from random import randint
import math
from typing import Callable

CSV_FILE = 'nums.csv'
JSON_FILE = 'nums.json'
MIN_ROWS = 100
MAX_ROWS = 1000


def sqrt_to_json(func):
    def wrapper(*args, **kwargs):
        res_dict = [{'nums': item[0], 'roots': item[1]} for item in func(*args, **kwargs)]
        with open(JSON_FILE, "w", encoding='UTF-8') as file:
            json.dump(res_dict, file, indent=2)
        return res_dict
    return wrapper

def search_sqrt(func):
    
    def wrapper(*args, **kwargs):
        res_list = []
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            for row in reader:
                a, b, c = row[0], row[1], row[2]
                result = func(a, b, c)
                res_list.append((row, result))
        return res_list
    return wrapper   

def fill_csv(csv_file, min, max):
    with open(csv_file, 'w', encoding='utf-8') as csv_f:
        writer = csv.writer(csv_f, lineterminator='\r')
        for _ in range(randint(min, max)):
            writer.writerow([randint(10, 100) for _ in range(3)])

@sqrt_to_json
@search_sqrt
def sqrt_(a, b, c):
    if a == 0:
        return None
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


# fill_csv(FILE, MIN_ROWS, MAX_ROWS)
result = sqrt_()
