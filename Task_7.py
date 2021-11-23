from itertools import count

n = int(input('Введите число\n'))
print()

def fuct():
  global n
  res = 1
  for i in range(1,n+1):
    res = res * i
    yield res

for el in fuct():
    print(el)