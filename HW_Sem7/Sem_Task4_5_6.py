# Создайте функцию, которая создаёт файлы с указанным расширением. 
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

# ✔ Доработаем предыдущую задачу. 
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
# ✔ Расширения и количество файлов функция принимает в качестве параметров. 
# ✔ Количество переданных расширений может быть любым. 
# ✔ Количество файлов для каждого расширения различно. 
# ✔ Внутри используйте вызов функции из прошлой задачи.

# * Генерируйте файлы в указанную директорию — отдельный параметр функции.

# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки). 

# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import random as rnd
import string
import os

def create_file_with_ext(ext, dir_name=os.getcwd(), min_len_name=6, max_len_name=30, min_bytes=256, max_bytes=4096, \
                         count_files=42):
    if dir_name not in os.listdir():
        os.mkdir(dir_name)
    for _ in range(count_files):
        name = rnd.choices(string.ascii_letters, k=rnd.randint(min_len_name, max_len_name))
        bytes_ = rnd.choices(string.ascii_letters, k=rnd.randint(min_bytes, max_bytes))
        name = "".join(name) + '.' + ext        
        if os.path.exists(os.path.join(dir_name, name)):
            print(f'Файл с именем {name} уже существует! Перезапись не разрешена')
        else:
            with open(f'{os.path.join(dir_name, name)}', 'wb') as file:
                file.write(''.join(bytes_).encode(encoding='utf-8'))


def mult_create_files_to_dir(dir_name=os.getcwd(), **kwargs):
    for ext, count in kwargs.items():
        create_file_with_ext(ext, dir_name, count_files= count)


if __name__ == '__main__':
    mult_create_files_to_dir('New_Dir',txt=2, jpeg=3, avi=1)