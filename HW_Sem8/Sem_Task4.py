# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json


def csv_to_json(csv_file, json_file):
    with(open(csv_file, 'r', encoding='utf-8')as c_f,
         open(json_file, 'w', encoding='utf-8')as j_f):
        file = [*csv.reader(c_f)]
        header_id, header_name, header_access = file[0]
        lst = []
        for id, name, access in file[1:]:
            lst.append({header_id: id, header_name: name, header_access: access, 'hash': hash(name + id)})

        json.dump(lst, j_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    csv_to_json('users.csv', 'new_user.json')