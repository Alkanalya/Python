file = open(r"texts/task_1_0.txt", 'w', encoding='utf-8')
print("Продолжайте вводить строки, которые хотите увидеть в файле, через Enter. Пустая строка окончит запись.")

# Основная реализация
while True:
  next_line = input()
  if next_line == '':
    break
  file.write(next_line + '\n')
file.close()

file = open(r"texts/task_1_1.txt", 'w', encoding='utf-8')
print("Эти строки попадут во второй файл. Принцип тот же.")
# Альтернативная реализация через writelines
new_lines = []
while True:
  next_line = input()
  if next_line == '':
    break
  new_lines.append(next_line + '\n')
file.writelines(new_lines)
file.close()

# Альтернативная реализация через менеджер контекста
print('А это пойдёт в третий файл.')
with open(r"texts/task_1_2.txt", "w", encoding='utf-8') as file_obj:
  while True:
    new_line = input()
    if new_line == '':
      break
    print(new_line, file=file_obj)

