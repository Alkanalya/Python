trans_dict = {
  'One':'Один',
  'Two':'Два',
  'Three':'Три',
  'Four':'Четыре',
  'Five':'Пять',
  'Six':'Шесть',
  'Seven':'Семь',
  'Eight':'Восемь',
  'Nine':'Девять'}


with open("texts/task_4_in.txt", 'r') as file_in:
  file_out = open("texts/task_4_out.txt", 'w')
  for line in file_in:
    ciph = line.split()[0]
    file_out.write(line.replace(ciph, trans_dict[ciph]))
  file_out.close()