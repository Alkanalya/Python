database = []
i = 0
print("Введите через пробел характеристики товара в указанной последовательности: Название, Цена, Количество, Ед. Разделяйте товары через 'Enter'. Если хотите закончить, напишите 'end'")
while True:
  raw_item = input()
  if raw_item == 'end':
    break
  new_item = raw_item.split()
  new_item_dict = {
    "название" : new_item[0],
    "цена" : new_item[1],
    "количество" : new_item[2],
    "ед" : new_item[3]
  }
  i = i + 1
  database.append((i, new_item_dict))

print(database)

data = []
for items in database:
  item_dict = items[1]
  print(item_dict)
  for key in item_dict.keys():
    val = []
    analit_dict = {key : val.append(item_dict.get(key))}

print(analit_dict)