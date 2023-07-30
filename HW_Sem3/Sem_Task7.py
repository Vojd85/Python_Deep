#   Пользователь вводит строку текста. 
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования 
#   метода count и с ним. 

# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи 
#   символа в строке. 

# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают 
#   или не совпадают в ваших решениях.

str1 = input()

dict = {}
dict2 = {}

for symbol in str1:
    dict[symbol] = str1.count(symbol)

for item in str1:
    if item in dict2:
        dict2[item] += 1
    else:
        dict2[item] = 1

print(f'{dict}\n{dict2}')

# У меня получилось что символы в словарь записываются в порядке итерации в строке, 
# потому что они меняют только значение, а не ключи