# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV

import csv
import json


def json_csv(jsonfile):
    csvfile = 'users.csv'
    with(open(jsonfile, "r", encoding="utf-8") as json_f,
        open(csvfile, "w", newline='', encoding="utf-8") as csv_f
        ):
        json_dict = json.load(json_f)
        print(json_dict)
        rows = []
        for level, in_dict in json_dict.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})

        print(rows)

        csv_write = csv.DictWriter(csv_f, fieldnames=['id', 'level', 'name'])
        csv_write.writeheader() 
        csv_write.writerows(rows)


if __name__ == '__main__':
    jsonfile = 'users.json'
    json_csv(jsonfile)