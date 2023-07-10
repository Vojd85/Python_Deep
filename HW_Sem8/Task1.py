# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle
from pathlib import Path

path_ = r'C:\Users\Вождь\Desktop\Python_DEEP\HomeWorks\Python_Deep\HW_Sem8'
lst = {'name': None, 'dirs':[], 'files':[]}
for path, dirs, files in os.walk(path_):
    lst['name'] = path_.rsplit('\\', 1)[1]
    for dir in dirs:
        if dir not in lst['dirs']:
            lst['dirs'].append(dir)
    for file in files:
        if file not in lst['files']:
            lst['files'].append(file)

print(lst)