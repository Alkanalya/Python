def my_func(num_1, num_2, num_3):
  return (sum([num_1,num_2, num_3]) - min(num_1,num_2, num_3))

while True:
  try:
    var_1 = int(input('Введите первое число: '))
    var_2 = int(input('Второе число: '))
    var_3 = int(input('Третье число: '))
  except ValueError:
    print('Необходимо вводить ЧИСЛА!!!\n')
    continue
  else:
    break

print(f"Сумма двух наибольших чисел: {my_func(var_1, var_2, var_3)}")