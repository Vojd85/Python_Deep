# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

list = [1, 5, 3, 43, 2, 1, 7, 43, 6, 6, 3, 10, 2, 5, 20, 7]

list2 = []

for i in range(len(list)):
    if list[i] not in list2 and list[i] in list[i+1:]:
        list2.append(list[i])

print(f'{list}\n{list2}')