# Напишите программу банкомат. 
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой 
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

BALANCE = 0
COUNT = 0
OPERATION_MULTIPLICITY = 50
REACH_LIMIT = 5000000
REACH_PERCENT = 0.1
POP_PERCENT = 0.015
THIRD_COUNT_PERCENT = 0.03
MIN_COMISSION = 30
MAX_COMISSION = 600



print('Добро пожаловать в банкомат! \n 1 Пополнить счет; 2 Снять средства; 3 Выход')

while True:
    if COUNT % 3 == 0:
        BALANCE += BALANCE * THIRD_COUNT_PERCENT
    if BALANCE > REACH_LIMIT:
        BALANCE -= BALANCE * REACH_PERCENT
    print('Выберите действие: ')
    choice = input()
    match choice:
        case '1':
            add_summ = int(input('Введите сумму пополнения кратную 50 у.е.: '))
            if add_summ % OPERATION_MULTIPLICITY == 0:
                BALANCE += add_summ
            else:
                print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')
            print(f'Ваш баланс: {BALANCE}')
            COUNT +=1
        case '2':
            pop_summ = int(input('Введите сумму для снятия кратную 50 у.е.:'))
            if pop_summ % OPERATION_MULTIPLICITY == 0:
                percent = pop_summ * POP_PERCENT
                if percent < MIN_COMISSION: percent = MIN_COMISSION
                elif percent > MAX_COMISSION: percent = MAX_COMISSION
                if pop_summ + percent > BALANCE:                    
                    print('На счете недостаточно средств')                    
                else:
                    BALANCE -= pop_summ + percent
            else:
                print('Вы ввели сумму не кратную 50 у.е. Попробуйте еще раз')
            print(f'Ваш баланс: {BALANCE}')
            COUNT += 1
        case '3':
            print(f'Ваш баланс: {BALANCE}')
            print('До свидания!')
            break

