import json

dict_with_profit = {}
dict_with_lose = {}
avarage_profit = {}
with open("texts/task_7.txt", 'r', encoding='utf-8') as file:
  for line in file:
    data = line.split()
    profit = int(data[2]) - int(data[3])
    if profit >= 0:
      dict_with_profit.update({data[0] : profit})
    else:
      dict_with_lose.update({data[0] : profit})
  avarage_profit.update({'avarage_profit' : (sum(dict_with_profit.values())) // len(dict_with_profit.values())})
  
  total_data = [dict_with_profit, avarage_profit, dict_with_lose]

print(total_data)

with open("texts/task_7.json", 'w', encoding='utf-8') as file_json:
  json.dump(total_data, file_json, ensure_ascii=False)