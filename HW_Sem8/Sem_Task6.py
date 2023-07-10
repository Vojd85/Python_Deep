# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. 
# Для тестированию возьмите pickle версию файла из предыдущей задачи. 
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle


def pickle_to_csv(pic_file, csv_file):
    with (open(pic_file, 'rb') as pic_f,
          open(csv_file, 'w', newline='', encoding='utf-8') as csv_f):
        new_list = pickle.load(pic_f)
        headers = [item for item in new_list[0]]
        csv_write = csv.DictWriter(csv_f, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(new_list)

if __name__ == '__main__':
    pickle_to_csv('new_user.pickle', 'new_user.csv')