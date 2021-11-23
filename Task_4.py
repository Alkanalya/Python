def my_func(x, y):
    # return 1 / (x ** abs(y))
    return x ** y

def my_func_alt(x, z):
    div = 1
    for i in range(z):
        div = div * x
    return 1 / div

x = float(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
z = abs(y)

print(f'Основной вариант: {round(my_func(x, y), 6)}')
print(f'Альтернативный вариант: {round(my_func_alt(x, z), 6)}')