# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

BACKPACK_LOAD_CAPACITY = 6

items = {'Термос': 1, 'Бумага': 0.1, 'Спички': 0.05, 'Вода': 1.5, 'Носки': 0.3, 'Палатка': 3.5
         , 'Спальник': 2, 'Пенка': 0.5, 'Горелка': 0.3, 'Продукты': 1.5}
backpack_result = set()

items_weight = sorted(items.values())

while len(items_weight) != 0 and BACKPACK_LOAD_CAPACITY >= items_weight[0]:
    for weight in items_weight[::-1]:
        if weight <= BACKPACK_LOAD_CAPACITY:
            for item in items:
                if items[item] == weight:
                    backpack_result.add(item)
                    BACKPACK_LOAD_CAPACITY -= weight
                    items.pop(item)
                    items_weight.remove(weight)
                    break
else:
    if len(backpack_result):    
        print(f'Содержимое рюкзака: {backpack_result}\nОстаток рюкзака {round(BACKPACK_LOAD_CAPACITY, 2)}кг')
    else: print('Извините, но в такой рюкзак ничего не влезет')