# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

DIGIT_SYSTEM = 16

hex_dict = {0:'0', 1:'1', 2:'2', 3: '3', 4: '4',
            5: '5', 6: '6', 7: '7', 8: '8', 
            9: '9', 10: 'a', 11: 'b', 12: 'c',
            13: 'd', 14: 'e', 15: 'f'}

decimal_num = int(input('Введите целое число: '))
temp = decimal_num
hex_num = ''
while decimal_num > 0:
    digit = decimal_num % DIGIT_SYSTEM
    hex_num = hex_dict[digit] + hex_num
    decimal_num //= DIGIT_SYSTEM

print(f'Число {temp} в шестнадцатеричной системе равно {hex_num}')
print(f'Число {temp} в шестнадцатеричной системе равно {hex(temp)[2:]}')