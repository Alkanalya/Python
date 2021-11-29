learn_dict = {}
with open("texts/task_6.txt", 'r') as file:
  for line in file:
    data = line.split(':')
    hours = data[1].split()
    total = 0
    for item in hours:
      value = item.strip('(лаб)пр')
      if value != '-':
        total += int(value)
    learn_dict.update({data[0] : total})
print(learn_dict)