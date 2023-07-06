# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. 

# * При переименовании в конце имени добавляется порядковый номер.

# * принимать в качестве аргумента расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.

# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os


def mass_rename(search_ext, new_name, new_ext):
    files = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file) and file.split('.')[1] == search_ext]
    for count, value in enumerate(files):
        os.rename(value, f'{value.split(".")[0]}_{new_name}_{count}.{new_ext}')


if __name__ == '__main__':
    mass_rename('mov', 'Supa', 'gpg')


