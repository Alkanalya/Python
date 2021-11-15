print("Введите элементы списка, разделяя клавишей 'Enter'. Когда закончите - напишите 'end'")
my_list = []
while True:
    item = input()
    if item == 'end':
        break
    my_list.append(item)

my_list_changed = []
# вставка в новый лист
i = 1
while i < len(my_list):
    my_list_changed.append(my_list[i])
    my_list_changed.append(my_list[i - 1])
    i = i + 2
if len(my_list) % 2 == 1:
    my_list_changed.append(my_list[-1])
print(my_list_changed)

# разворот на месте с доп переменной?
# срез + insert...
