class MyException(Exception):
    def __init__(self, text):
        self.text = text

print("Введите числа:")
output = []
while True:
    enter = input()
    try:
        if not enter.isdecimal():
            if enter == 'stop':
                break
            else:
                raise MyException('Вы ввели не число.')
        output.append(int(enter))
    except MyException as err:
        print(err)

for num in output:
    print(num)