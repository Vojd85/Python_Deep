# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

BALANCE = 0
COUNT = 0
OPERATION_MULTIPLICITY = 50
REACH_LIMIT = 5000000
REACH_PERCENT = 0.1
POP_PERCENT = 0.015
THIRD_COUNT_PERCENT = 0.03
MIN_COMISSION = 30
MAX_COMISSION = 600


def show_balance():
    print(f'Ваш баланс: {BALANCE}')


def logger(number, lst: list):
    lst += [number]


def add_():
    global BALANCE

    add_summ = int(input('Введите сумму пополнения кратную 50 у.е.: '))
    if add_summ % OPERATION_MULTIPLICITY == 0:
        BALANCE += add_summ
        logger(add_summ, log_list)
    else:
        print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')


def pop_():
    global BALANCE

    pop_summ = int(input('Введите сумму для снятия кратную 50 у.е.:'))
    if pop_summ % OPERATION_MULTIPLICITY == 0:
        percent = pop_summ * POP_PERCENT
        if percent < MIN_COMISSION: percent = MIN_COMISSION
        elif percent > MAX_COMISSION: percent = MAX_COMISSION
        if pop_summ + percent > BALANCE:                    
            print('На счете недостаточно средств')                    
        else:
            BALANCE -= pop_summ + percent
            logger((-1)*(pop_summ + percent), log_list)
    else:
        print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')


def add_count_percent():
    result = BALANCE * THIRD_COUNT_PERCENT
    logger(result, log_list)
    return result


def pop_reach_percent():
    result = BALANCE * REACH_PERCENT
    logger((-1)*result, log_list)
    return result


print('Добро пожаловать в банкомат! \n 1 Пополнить счет; 2 Снять средства; 3 Выход')

log_list = []

while True:
    if COUNT % 3 == 0 and COUNT != 0:
        BALANCE += add_count_percent()
    if BALANCE > REACH_LIMIT:
        BALANCE -= pop_reach_percent()
    print('Выберите действие: ')
    choice = input()
    match choice:
        case '1':
            add_()
            show_balance()
            COUNT += 1
        case '2':
            pop_()
            show_balance()
            COUNT += 1
        case '3':
            show_balance()
            print('До свидания!')
            break
    print(log_list)