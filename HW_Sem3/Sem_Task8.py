# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
#   ✔ Какие вещи взяли все три друга
#   ✔ Какие вещи уникальны, есть только у одного друга
#   ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#   ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей

rucksacks = {'Вован':('Термос', 'Бумага', 'Спички', 'Вода'),
             'Саня':('Пистолет', 'Бумага', 'Спички', 'Вода'),
             'Кирилл':('Спички', 'Вода', 'Носки', 'Термос'),
             }

set1 = set()
for values in rucksacks.values():
    if len(set1) == 0:
        set1 = set(values)
    else:
        temp_set = set(values)
        set1 = set1 & temp_set
print(f'Все взяли с собой {set1}')

set2 = ()
for values in rucksacks.values():
    set2 += values
for key in rucksacks:
    for item in rucksacks[key]:
        if set2.count(item) == 1:
            print(f'{item} есть только у {key}!')

set3 = set()
for item in set2:
    if set2.count(item) == len(rucksacks) - 1:
        set3.add(item)
for key in rucksacks:
        temp_set = set(rucksacks[key])
        temp_set = set3 - temp_set
        if len(temp_set):
            print(f'{temp_set.pop()} не взял только {key}')
    
