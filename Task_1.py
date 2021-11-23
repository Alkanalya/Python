from sys import argv

script_name, total_hours, work_per_hour, premium = argv

try:
    salary = int(total_hours) * int(work_per_hour) + int(premium)
    print(f'Зарплата: {salary}')
except ValueError:
    print('Введены неверные аргументы!')
