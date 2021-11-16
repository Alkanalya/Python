print("Введите элементы списка, разделяя клавишей 'Enter'. Когда закончите - напишите 'end'")
my_list = []
while True:
    item = input()
    if item == 'end':
        break
    my_list.append(item)

# Вариант через вставку в новый лист
my_list_changed = []
i = 1
while i < len(my_list):
    my_list_changed.append(my_list[i])
    my_list_changed.append(my_list[i - 1])
    i += 2
if len(my_list) % 2 == 1:
    my_list_changed.append(my_list[-1])
print(my_list_changed)

# Разворот на месте с доп. переменной
temp = 0
for i in range(1, len(my_list), 2):
#   Прямой обмен переменных, но мы не проходили этого вроде...
#   my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
    temp = my_list[i]
    my_list[i] = my_list[i - 1]
    my_list[i - 1] = temp
print(my_list)

