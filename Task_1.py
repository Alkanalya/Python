class Matrix:
    def __init__(self, lines):
        self.lines = lines

    def __str__(self):
        line_out = ''
        for line in self.lines:
            for num in line:
                line_out = line_out + str(num) + ' '
            if line != self.lines[-1]:
                line_out = line_out[:-1] + '\n'
        return line_out

    def __add__(self, other):
        fin_line = []
        fin_lines = []
        fin_num = 0
        for line_1, line_2 in zip(self.lines, other.lines):
            for num_1, num_2 in zip(line_1, line_2):
                fin_num = num_1 + num_2
                fin_line.append(fin_num)
            fin_lines.append(fin_line)
            fin_line = []
        return Matrix(fin_lines)

a = Matrix([[1, 2, 8], [2, 1, 9]])
b = Matrix([[5, 1, 20], [5, 1, 2]])
c = Matrix([[4, 6, 30], [10, 0, 100]])

print(a + b + c)


# Возможность вводить и получать сумму нескольких введённых матриц
# К сожалению, пока не реализовал сумму разноразмерных матриц :(
# Но для равноразмерных работает.
print("Введите 'start' для введения своих матриц.")
if input() == 'start':
    print('Введём несколько матриц для суммы.')
    print('Введите числа для строки матрицы через пробел')
    print("Чтобы закончить матрицу, написать 'end'.")
    print("Напишите 'sum' чтобы получить сумму введённых матриц")
    print("Для выхода из программы напишите 'exit'")

    temp_matrx = []
    matrx_1 = None

    while True:
        inter = input()
        if inter == 'end':
            if matrx_1 == None:
                matrx_1 = Matrix(temp_matrx)
                temp_matrx = []
            else:
                matrx_1 = matrx_1 + Matrix(temp_matrx)
                temp_matrx = []
        elif inter == 'exit':
            break
        elif inter == 'sum':
            print(matrx_1)
        else:
            try:
                line_mat = list(map(int, inter.split()))
                temp_matrx.append(line_mat)
            except ValueError:
                print('Неверный ввод данных в матрицу. Повторите ввод строки.')
                continue
