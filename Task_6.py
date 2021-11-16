database = []
i = 0

# Сделал возможность вводить характеристики для большей масштабируемости программы.
temp = input('Введите характеристики для товаров через пробел\n')
indx = temp.split()
print("Введите указанные характеристики товара через пробел. \nРазделяйте товары через 'Enter'. \nЕсли хотите закончить, напишите 'end'")
while True:
  raw_item = input()
  if raw_item == 'end':
    break
  new_item_dict = {}
  new_item = raw_item.split()

# Создаём словарь для товара:
  for a in range(len(indx)):
    new_item_dict.update({indx[a]: new_item[a]})
  i = i + 1

# Укладываем всё в базу:
  database.append((i, new_item_dict))

print(database)

# Делаем аналитику:
data = []
analit_dict = {}
# Создаём пустой словарь для аналитики с указанными характеристиками:
for chart in indx:
  analit_dict.update({chart: []})
# Собираем словарь аналитики из словарей товаров:
for items in database:
  item_dict = items[1]
  for key, value in item_dict.items():
    analit_dict[key].append(value)

# Выводим аналитику (не совсем так, как было в примере, но можно переделать):
for key in analit_dict.keys():
  print(f"{key} : {analit_dict[key]}")
