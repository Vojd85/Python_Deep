# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def great_delimiter (num1, num2):
    if num1 > num2:
        temp = num2
    else:
        temp = num1
    for i in range(1, temp+1):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    return result

str_1 = input('Введите первое число через дробь: ')
str_2 = input('Введите второе число через дробь: ')

#   a   c       ad + cb                     ac
#   _ + _  =    _______      и умножение    __
#   b   d          bd                       bd

a = int(str_1[:str_1.index('/')])
b = int(str_1[str_1.index('/')+1:])
c = int(str_2[:str_2.index('/')])
d = int(str_2[str_2.index('/')+1:])
if a or b or c or d == 0:
    print('Ноль не может быть ни в числителе, ни в знаменателе')
    quit()

numerator = a*d + c*b
denumerator = b*d
gcd = great_delimiter(numerator, denumerator)
if numerator == denumerator:
    summ_fraction = 1
else:
    summ_fraction = str(int(numerator/gcd)) + '/' + str(int(denumerator/gcd))

numerator = a*c
denumerator = b*d
gcd = great_delimiter(numerator, denumerator)
if numerator == denumerator:
    mult_fraction = 1
else:
    mult_fraction = str(int(numerator/gcd)) + '/' + str(int(denumerator/gcd))


print('Сложение равно ', summ_fraction, 'через fraction', Fraction(str_1) + Fraction(str_2))
print('Умножение равно', mult_fraction,'через fraction', Fraction(str_1) * Fraction(str_2))
