# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
# Распечатайте его как pickle строку.

import csv
import pickle


def csv_to_pickle_string(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_f:
        csv_file = csv.reader(csv_f)
        for line in csv_file:
            print(pickle.dumps(line))
              
if __name__ == '__main__':
    csv_to_pickle_string('new_user.csv')