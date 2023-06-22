# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки

str1 = input()

list = sorted(str1.split())
max_len = 0
for item in list:
    if len(item) > max_len:
        max_len = len(item)
for index, item in enumerate(list, start=1):
    print(f'{index} {item:>{max_len}}')

print(list)