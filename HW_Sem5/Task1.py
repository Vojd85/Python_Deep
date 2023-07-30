# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


path = input('Введите абсолютный путь: ')

def elements(absolute_path: str):
    file = absolute_path.replace('/', '\\').split("\\")[-1]
    file_name = str(file.split('.')[0])
    file_extension = file.split('.')[1]
    path = absolute_path.replace(file, '')
    return path, file_name, file_extension

print(elements(path))