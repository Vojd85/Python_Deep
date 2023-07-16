# Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задачи должны решаться через вызов методов экземпляра.

import random as rnd
import os
import json
import csv


class FileWork:
    COUNT = 10

    def __init__(self, path_to_work_dir):
        self.directory = path_to_work_dir

    def dir_(self):
        return self.directory

    def two_nums(self, filename, min, max):
        with open(filename, 'w', encoding='utf-8') as f:
            for _ in range(self.COUNT):
                f.write(f'{rnd.randint(min, max)}|{round(rnd.uniform(min, max),2)}\n')

    def get_names(self, file_name, min_symbol, max_symbol):
        letterA = 'йцукенгшщзхфывапролджэячсмитьбю'
        letterB = 'уеыаоэяю'
        with open(file_name, 'w', encoding='utf-8') as file:
            for _ in range(self.COUNT):
                name = rnd.sample(letterA, rnd.randint(min_symbol, max_symbol))
                if not set(letterA) & set(letterB):
                    half = len(name) // 2
                    name = name[:half] + rnd.sample(letterB, half)
                    rnd.shuffle(name)
                name = ''.join(name).capitalize()
                file.write(f'{name}\n')

    def result_list(self, names_file, nums_file, result_file):
        with(open(names_file, 'r', encoding='utf-8') as f_names,
             open(nums_file, 'r', encoding='utf-8') as f_nums,
             open(result_file, 'w', encoding='utf-8') as f_res):
            data = []
            for item in zip(f_names, f_nums):
                # print(item[0].strip(), item[1].strip())
                a, b = map(float, item[1].strip().split('|'))
                # print(type(a), a, type(b), b)
                data.append({'Name': item[0].strip(), 'Result': a * b})
            
            json.dump(data, f_res, indent=4, ensure_ascii=False)

    def json_to_csv(self, json_file, csv_file):
        with(open(json_file, "r", encoding="utf-8") as json_f,
            open(csv_file, "w", newline='', encoding="utf-8") as csv_f
            ):
            json_dict = json.load(json_f)
            rows = []
            for dict in json_dict:
                rows.append(dict)
            csv_write = csv.DictWriter(csv_f, fieldnames=['Name', 'Result'])
            csv_write.writeheader() 
            csv_write.writerows(rows)


if __name__ == '__main__':
    file = FileWork(os.getcwd)
    file.two_nums('test.txt', -100, 100)
    file.get_names('names.txt', 4, 8)
    file.result_list('names.txt', 'test.txt', 'result.json')
    file.json_to_csv('result.json', 'result.csv')