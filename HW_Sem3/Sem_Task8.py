# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. 
# Ответьте на вопросы:
#   ✔ Какие вещи взяли все три друга
#   ✔ Какие вещи уникальны, есть только у одного друга
#   ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
#   ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей

rucksacks = {'Вован':('Термос', 'Носки', 'Бумага', 'Спички', 'Вода'),
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


    

print(set1)

