print("Введите число:")
num = int(input())
max_ciph = -1
while num != 0:
    if num % 10 > max_ciph:
        max_ciph = num % 10
    num = num // 10
print('Максимальная цифра в числе:', max_ciph)