# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import sys

__all__ = ['input_date']


def _visokos(year):
    ULIAN = 4
    GRIG_1 = 400
    GRIG_2 = 100

    return year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0

def input_date(date):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month == 2:
                if _visokos(year):
                    if 1 <= day <= 29:
                        return True
                else:
                    if 1 <= day <= 28:
                        return True
            if month in m_30 and 1<=day<=30:
                return True
            if month in m_31 and 1<=day<=31:
                return True
    return False

if __name__ == "__main__":
    input = sys.argv[1]
    print(input_date(input))