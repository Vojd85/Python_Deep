# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

MIN_LIMIT = 1
MAX_LIMIT = 999

result = ''

number = int(input('Введите число от ' + str(MIN_LIMIT) + ' до ' + str(MAX_LIMIT) + ':\n'))
while number < MIN_LIMIT or number > MAX_LIMIT:
    number = int(input('Число должно быть в заданном диапазоне. Попробуйте еще раз: '))
if not number // 10 and number % 10:
    result = 'Введена цифра. Ответ: %d' % (number*number)
elif number // 10 and not number // 100:
    result = 'Введено двузначное число. Ответ: %d' % ((number // 10) * (number % 10))
else:
    temp = 0
    while number:
        digit = number % 10
        temp = temp * 10 + digit
        number = number // 10
    result = 'Введено трехзначное число. Ответ: %d' % (temp)
print(result)