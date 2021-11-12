print('Количество километров в первый день:')
a = int(input())
print('Сколько километров нужно:')
b = int(input())
day = 1
while a <= b:
    day += 1
    a = a + a * 0.1
    print(f"{day}-й день: {a:.2f}")
print(f'На {day}-й день будет не менее {b} километров')
