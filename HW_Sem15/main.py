# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. 
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
from Task1 import dir_content

def parse_arg():
    parser = argparse.ArgumentParser(description='Walk in directory')
    parser.add_argument('-p', metavar='p', type=str, help='Enter a path to directory')
    args = parser.parse_args()
    dir_content(args.p)


if __name__ == '__main__':
    parse_arg()