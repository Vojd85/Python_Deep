# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import json
import pytest
from project import Project
from user import User
from exceptions import AccessException, LevelException

FILE = 'users.json'

@pytest.fixture
def create():
    project = Project.load(FILE)
    return project

@pytest.fixture
def get_users():
    with open(FILE, 'r', encoding='utf-8') as f:
        users_dict = json.load(f)
        users = []
    for level, user in users_dict.items():
        for id, name in user.items():
            users.append(User(id, name, level))
    return users

@pytest.fixture
def strange_human():
    return User('99', 'jdfj', 1)

def test_human(get_users):
    first = get_users[0]
    assert first in get_users

def test_human_2(get_users):
    sec = get_users[1]
    assert sec in get_users

def test_fail_human(get_users, strange_human):
    # user = User(99, 'jdfj', 1)
    assert strange_human not in get_users

def test_login(create, get_users):
    create.login(get_users[0].user_id, get_users[0].name)
    assert create.admin == get_users[0]

def test_login_exception(create, strange_human):
    with pytest.raises(AccessException):
        create.login(strange_human.user_id, strange_human.name)

def test_add_user(create):
    create.login('324', 'Саня')
    create.add_user(444, 'Фёдор', 6)
    new_user = User(444, 'Фёдор')
    assert new_user in create.users 

def test_add_user_exception(create):
    create.login('324', 'Саня')
    with pytest.raises(LevelException):
        create.add_user(444, 'Фёдор', 2)



if __name__ == '__main__':
    pytest.main()