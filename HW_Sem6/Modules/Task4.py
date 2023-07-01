# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными верными вариантами отгадок и количество попыток на угадывание.
# Функция возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

__all__ = ['riddle_res', 'show_res']

def riddle(text="Сорок одёжок и все без застёжек", solution=['капуста', 'капустка'], attempt=5):
    count = 1
    print (f"Отгадайте загадку: {text}")
    while count<attempt:
        a = (input("Введите отгадку: ")).lower()
        if a in solution:
            print (f"Вы угадали c {count} попытки.")
            return count
        else:
            print ("Ошибка")
            count +=1
        if count == attempt:
            print ("Вы исчерпали количество попыток")
            return 0
        
def riddle_list():
    dic ={"Зимой и летом одним цветом": ["ель", "елка", "елочка"],
    "Не лает, не кусает, в дом не пускает": ['замок','вахтер'],
    "Висит груша, нельзя скушать":['лампа','лампочка']}
    for i,j in dic.items():
        riddle_res(i, riddle(i,j))

def riddle_res(text, count):
    _riddle_list[text] = count

def show_res():
    print("\n".join([f"'{key}': с попытки №{value}" for key, value in _riddle_list.items()]))


_riddle_list = {}