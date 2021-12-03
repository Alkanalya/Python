class Cell:
    def __init__(self, square):
        self.square = square

    def __add__(self, other):
        return Cell(self.square + other.square)

    def __sub__(self, other):
        if self.square - other.square < 0:
            print('Нельзя, ячеек не может быть меньше нуля.')
            return Cell(self.square)
        else:
            return Cell(self.square - other.square)

    def __mul__(self, other):
        return Cell(self.square * other.square)

    def __truediv__(self, other):
        return Cell(self.square // other.square)

    def make_order(self, cell_in_line):
        out_line = ''
        count = 0
        for i in range(self.square):
            out_line += '*'
            count += 1
            if count % cell_in_line == 0 and self.square - 1 != i:
                out_line += '\n'
        return out_line

a = Cell(32)
b = Cell(5)
c = a / b
print(c.make_order(4))

print('Введите размер начальной клетки:')
enter = Cell(int(input()))

print('Команды для взаимодействия:')
print("+ __ - прибавить клетки")
print("- __ - вычесть клетки")
print("* __ - умножить клетки")
print("/ __ - разделить клетки")
print("order __ - упорядочить клетки по количеству ячеек")
print("exit - выйти из программы")
print()
while True:
    comm = input().split()
    match comm[0]:
        case '+':
            enter = enter + Cell(int(comm[1]))
        case '-':
            enter = enter - Cell(int(comm[1]))
        case '*':
            enter = enter * Cell(int(comm[1]))
        case '/':
            enter = enter / Cell(int(comm[1]))
        case 'order':
            print(enter.make_order(int(comm[1])))
        case 'exit':
            break
        case _:
            print('Неверный ввод команды. Повторите ввод.')