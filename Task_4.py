sentence = input('Введите слова через пробел. Для завершения строки нажмите "Enter"\n')
sntc_list = sentence.split()
i = 0
for word in sntc_list:
  i = i + 1
  print(f'{i}) {word[:10]}') 