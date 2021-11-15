'''print("Введите элементы списка, разделяя клавишей 'Enter'. Когда закончите - напишите 'end'")
my_list = []
while True:
    item = input()
    if item == 'end':
        break
    my_list.append(item)
print(my_list)'''

my_list = ['zero', 1, {2, 'two'}, ("three", 3), {'four': 4}]
for item in my_list:
    print(type(item))
