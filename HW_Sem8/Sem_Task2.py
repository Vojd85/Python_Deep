# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import os
import json


def users_to_json(json_file):
    if os.path.isfile(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            dict_ = json.load(file)
    else:
        dict_ = {str(i):{} for i in range(1,8)}

    while True:
        data = input('Введите через пробел имя, id, уровень доступа от 1 до 7: ')
        if not data:
            break
        user_name, id, access = data.split()
        if id not in dict_[access]:
            dict_.setdefault(access, {id:user_name})[id] = user_name

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(dict_, file, ensure_ascii=False)

if __name__ == '__main__':
    users_to_json('users.json')