from itertools import count, cycle

num = int(input('С какого числа начать итерацию?\n'))
listik = input('Введите строку для итераций:\n')
stop = int(input('Сколько итераций провести?\n'))
i = 0
j = 0

for i in count(num):
  if i >= stop + num:
    break
  else:
    print(i)

for char in cycle(listik):
  if j >= stop:
    break
  print(char)
  j += 1