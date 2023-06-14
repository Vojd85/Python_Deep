# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

YEAR_CONST1 = 4
YEAR_CONST2 = 100
GREG_CALENDAR = 1582

result = None

year = int(input('Напишите год для проверки на високосность: '))
if year < GREG_CALENDAR:
    result = 'Грегорианский календарь был введен только в феврале 1582г.'
elif year % YEAR_CONST1 != 0 or year % YEAR_CONST2 == 0 and year % (YEAR_CONST1 * YEAR_CONST2) != 0:
    result = 'Обычный год'
else: 
    result = 'Високосный год'
print(result)