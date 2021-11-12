while True:
    var = input()
    if var == 'Выход':
        break
    print(f'Вы ввели "{var}", тип: {type(var)}')
    print("Введите 'Выход' чтобы выйти")
