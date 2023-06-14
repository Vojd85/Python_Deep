# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

MIN_LIMIT = 0
MAX_LIMIT = 1000
COUNT = 10

rand_num = randint(MIN_LIMIT, MAX_LIMIT)
print(rand_num)
print('Загадано число от 0 до %d. Попробуйте его угадать за %d попыток' % (MAX_LIMIT, COUNT))
while COUNT > 0:
    number = int(input('Введите число: '))
    if number < MIN_LIMIT or number > MAX_LIMIT:
        print('Число не в заданном диапазоне. Минус попытка. Попробуйте еще раз)')
        COUNT -= 1
    elif number == rand_num:
        print('Поздравляю! Вы угадали число ' + str(rand_num))
        break
    elif number < rand_num:
        print('Число больше чем ваше)')
        COUNT -= 1
    elif number > rand_num:
        print('Число меньше чем ваше)')
        COUNT -= 1
else: 
    print('Увы, Вы израсходовали лимит попыток. До свидания')


