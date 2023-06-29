# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


OPERATION_MULTIPLICITY = 50
REACH_LIMIT = 5000000
REACH_PERCENT = 0.1
POP_PERCENT = 0.015
THIRD_COUNT_PERCENT = 0.03
MIN_COMISSION = 30
MAX_COMISSION = 600


def show_balance(balance):
    print(f'Ваш баланс: {balance}')


def logger(number, lst: list):
    lst += [number]


def add_(balance, index):
    add_summ = int(input('Введите сумму пополнения кратную 50 у.е.: '))
    if add_summ % index == 0:
        logger(add_summ, log_list)
        return add_summ
    else:
        print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')
        return 0


def pop_(balance, index, min, max):
    pop_summ = int(input('Введите сумму для снятия кратную 50 у.е.:'))
    if pop_summ % index == 0:
        percent = pop_summ * POP_PERCENT
        if percent < min: percent = min
        elif percent > max: percent = max
        if pop_summ + percent > balance:                    
            print('На счете недостаточно средств')  
            return 0                  
        else:
            logger((-1)*(pop_summ + percent), log_list)
            return pop_summ + percent
    else:
        print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')
        return 0


def add_count_percent(balance, index):
    result = balance * index
    logger(result, log_list)
    return result


def pop_reach_percent(balance, index):
    result = balance * index
    logger((-1)*result, log_list)
    return result


print('Добро пожаловать в банкомат!')
balance = 0
count = 0
log_list = []

while True:
    if count % 3 == 0 and count != 0:
        balance += add_count_percent(balance, THIRD_COUNT_PERCENT)
    if balance > REACH_LIMIT:
        balance -= pop_reach_percent(balance, REACH_PERCENT)
    print('Выберите действие(1 Пополнить счет; 2 Снять средства; 3 Выход): ')
    choice = input()
    match choice:
        case '1':
            balance += add_(balance, OPERATION_MULTIPLICITY)
            show_balance(balance)
            count += 1
        case '2':
            balance -= pop_(balance, OPERATION_MULTIPLICITY, MIN_COMISSION, MAX_COMISSION)
            show_balance(balance)
            count += 1
        case '3':
            show_balance(balance)
            print('До свидания!')
            break
    print(f'Последние 5 операций: {log_list[-5:]}')