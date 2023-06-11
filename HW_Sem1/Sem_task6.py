YEAR_CONST1 = 4
YEAR_CONST2 = 100
GREG_CALENDAR = 1582

result = None

year = int(input('Напишите год для проверки на високосность: '))
if year < GREG_CALENDAR:
    result = 'Грегорианский календарь был введен только в феврале 1582г.'
elif year % YEAR_CONST1 != 0:
    result = 'Обычный год'
elif year % (YEAR_CONST1 * YEAR_CONST2) == 0:
    result = 'Високосный год'
elif year % YEAR_CONST2 == 0:
    result = 'Обычный год'
else: 
    result = 'Високосный год'
print(result)