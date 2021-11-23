from functools import reduce

print(reduce(lambda x,y: x * y, [num for num in range(100, 1001) if num % 2 == 0]))

# Проверка числа с помощью обычного цикла
mult = 1
for i in range(100, 1001, 2):
    mult = mult * i
print()
print(mult)