
import json
from user import User
from exceptions import AccessException, LevelException

def add_user_to_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            my_dict = json.load(f)
    except Exception:
        my_dict = {str(level): {} for level in range(1, 8)}
        print(f'{my_dict = }')
    while True:
        name, user_id, level, *_ = input("Введите имя, личный идентификатор и уровень доступа через пробел: ").split()
    # если идентификатора нет в ключах словаря, то добавляем пару {идентификатор : имя} в словарь
        try:
            if user_id not in my_dict[level].keys():
                my_dict[level].update({user_id: name})
                # break
            else:
                print('Идентификатор не уникален')
                break
        except KeyError as e:
            print(f'Ошибка ввода уровня {e}')
    print(f'{my_dict = }')
    with open(filename, "w", encoding="utf-8") as f:
        # записываем словарь в json-файл с отступом=1
        json.dump(my_dict, f, indent=1, ensure_ascii=False)


class Project:
    def __init__(self, users):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                users_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}. ')
        else:
            users = []
            for level, user in users_dict.items():
                for user_id, name in user.items():
                    users.append(User(user_id, name, level))
            return Project(users)

    def __str__(self):
        return str(self.users)
    
    def __repr__(self):
        return f'Project({self.users}, {self.admin})'

    # вход в систему
    def login(self, user_id, name):
        user_new = User(user_id, name)
        if user_new not in self.users:
            raise AccessException(user_id)
        for user in self.users:
            if user_new == user:
                self.admin = user

    # добавление пользователя
    def add_user(self, user_id, name, level):
        if int(self.admin.level) >= int(level):
            raise LevelException(level)
        self.users.append(User(user_id, name, level))


if __name__ == '__main__':
    filename = 'users.json'
    # add_user_to_file(filename)
    project = Project.load(filename)
    for user in project.users:
        print(user)
