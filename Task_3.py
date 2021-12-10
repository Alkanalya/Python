class MyException(Exception):
    def __init__(self, text):
        self.text = text

print("Вводите числа через 'Enter'. Для окончания ввода напишите 'stop'.")
output = []
while True:
    enter = input()
    try:
        if (not enter.isdecimal() and enter[0] != '-') or len(enter) == 0:
            if enter == 'stop':
                break
            else:
                raise MyException('Вы ввели не число.')
        output.append(int(enter))
    except MyException as err:
        print(err)

for num in output:
    print(num)