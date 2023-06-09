# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

MAX_LIMIT = 100000
MIN_LIMIT = 1

result = True

number = int(input('Введите число для проверки: '))
while number < MIN_LIMIT or number > MAX_LIMIT:
    number = int(input('Число должно быть не отрицательным и не более ' + str(MAX_LIMIT) + '\n Попробуйте еще раз: '))
for num in range(MIN_LIMIT + 1, number):
    if number % num == 0:
        result = False
        break
    
if result == True: print('Число простое')
else: print('Число составное')
