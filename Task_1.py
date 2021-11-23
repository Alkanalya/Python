def sub(var_1, var_2):
    try:
        subtr = var_1 / var_2
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
        return 'Будьте внимательны в следующий раз'
    return round(subtr, 3)

a = int(input("Введите делимое и делитель, разделяя Enter'ом\n"))
b = int(input())

print(sub(a,b))