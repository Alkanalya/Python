total = 0
bad_workers = []
lines = 0
with open("texts/task_3.txt", 'r', encoding='utf-8') as file:
  for line in file:
    salary = float(line.split()[1])
    if salary < 20000.00:
      bad_workers.append(line.split()[0])
    total += salary
    lines += 1

for name in bad_workers:
  print(name)
print(f'Средний оклад = {total/lines:2f}')
