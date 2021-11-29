lines = 0
dict_lines = {}

with open("texts/task_2.txt", 'r', encoding='utf-8') as file_obj:
  for line in file_obj:
    lines += 1
    words = line.split()
    dict_lines.update({lines: len(words)})

print(f'{dict_lines}\n')
for key in dict_lines.keys():
  print(f'{key} : {dict_lines[key]}')