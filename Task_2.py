list_nums = input('Введите числа через пробел.\n').split()
nums = [int(number) for number in list_nums]

bigger_nums = [nums[i] for i in range(len(nums)) if (nums[i] > nums[i - 1])]
print(bigger_nums)
