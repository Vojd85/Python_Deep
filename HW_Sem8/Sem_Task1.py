# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def create_json_file(input_file, output_file):
    data = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        name, product = line.strip().split(': ')
        name = name.title()
        product = float(product)
        data.append({'name': name, 'product': product})

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


create_json_file('result.txt', 'result.json')