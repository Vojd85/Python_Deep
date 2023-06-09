MIN_LIMIT = 1
MAX_LIMIT = 999

result = 0

number = int(input('Введите число от ' + str(MIN_LIMIT) + ' до ' + str(MAX_LIMIT) + ':\n'))
while number < MIN_LIMIT or number > MAX_LIMIT:
    number = int(input('Число должно быть в заданном диапазоне. Попробуйте еще раз: '))
if number < 10:
    result = number*number
elif 9 < number < 100:
    result = (number // 10) * (number % 10)
else:
    while number != 0:
        digit = number % 10
        result = result * 10 + digit
        number = number // 10
print(result)