with open("texts/task_5.txt", 'w+', encoding='utf-8') as file:
  numbers = input('Введите числа.\n')
  file.write(numbers)
  file.seek(0)
  print(sum(map(int, file.readline().split())))
    