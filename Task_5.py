print('Выручка:')
in_cash = int(input())
print('Издержки:')
out_cash = int(input())
if in_cash > out_cash:
    print('Компания отработала в прибыль.')
    print('Рентабельность выручки:', (in_cash - out_cash) / in_cash)
    print('Введите число сотрудников:')
    staff = int(input())
    print('Прибыль фирмы на 1 сотрудника:', (in_cash - out_cash) / staff)
elif in_cash < out_cash:
    print('Компания отработала в убыток :(')
else:
    print('Компания отработала без прибыли.')