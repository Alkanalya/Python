quit_key = False
new_sum = 0
old_sum = 0

def sumation(argument):
    '''
    Функция считает сумму численных аргументов, пропуская нечисленные значения.
    В случае введения символа выхода - устанавливает ключ-выход для дальнейшего выхода из программы.

    arguments: argument - список аргументов, полученный из ввода и обработанный split'ом
    return: new_sum - результат суммирования элементов списка
    '''
    global quit_key
    new_sum = old_sum
    for num in argument:
        try:
            new_sum = new_sum + int(num)
        except ValueError:
            if num == 'q':
                quit_key = True
            continue
    return new_sum


print("Вводите строки с числами, разделяя их пробелами. Для выхода введите 'q'.")
while True:
    str = input().split()
    print(f'Было = {old_sum}')
    new_sum = sumation(str)
    print(f'Стало = {new_sum}')
    old_sum = new_sum
    if quit_key:
        print('До свидания!')
        break

