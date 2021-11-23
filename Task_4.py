raw_nums = input('Введите последовательность чисел.\n').split()
list_of_nums = [int(num) for num in raw_nums]
new_list = [num for num in list_of_nums if list_of_nums.count(num) == 1]
print(new_list)
