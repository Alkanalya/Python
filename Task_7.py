class ComplexNum():
    def __init__(self, number):
        i = 0
        temp = ''
        while True:
            temp += number[i]
            if number[i + 1].isdecimal() or (number[i + 1] == '.'):
                i += 1
            else:
                try:
                    self.re = int(temp)
                    self.im = int(number[(i + 1):(len(number) - 1)].replace(' ', ''))
                except ValueError:
                    self.re = round(float(temp), 2)
                    self.im = round(float(number[(i + 1):(len(number) - 1)].replace(' ', '')), 2)
                finally:
                    break

    def __add__(self, other):
        temp_1 = self.re + other.re
        if (temp_2 := self.im + other.im) < 0:
            return ComplexNum(str(temp_1) + str(temp_2) + 'i')
        else:
            return ComplexNum(str(temp_1) + '+' + str(temp_2) + 'i')

    def __mul__(self, other):
        temp_1 = (self.re * other.re) - (self.im * other.im)
        if (temp_2 := (self.re * self.im) + (other.re * other.im)) < 0:
            return ComplexNum(str(temp_1) + str(temp_2) + 'i')
        else:
            return ComplexNum(str(temp_1) + '+' + str(temp_2) + 'i')

    def __sub__(self, other):
        temp_1 = self.re - other.re
        if (temp_2 := self.im - other.im) < 0:
            return ComplexNum(str(temp_1) + str(temp_2) + 'i')
        else:
            return ComplexNum(str(temp_1) + '+' + str(temp_2) + 'i')

    def __truediv__(self, other):
        temp_1 = ((self.re * other.re) + (self.im * other.im)) / (other.re**2 + other.im**2)
        if (temp_2 := ((self.im * other.re) + (self.re * other.im)) / (other.re**2 + other.im**2)) < 0:
            return ComplexNum(str(temp_1) + str(temp_2) + 'i')
        else:
            return ComplexNum(str(temp_1) + '+' + str(temp_2) + 'i')

    def __str__(self):
        if self.im < 0:
            return str(self.re) + str(self.im) + 'i'
        else:
            return str(self.re) + '+' + str(self.im) + 'i'


print('Введите 2 комплексных числа')
try:
    a = ComplexNum(input('a='))
    b = ComplexNum(input('b='))
except TypeError:
    print('Неверно введено комплексное число.')
else:
    print(f'Сложение: {a + b}')
    print(f'Вычитание: {a - b}')
    print(f'Умножение: {a * b}')
    print(f'Деление: {a / b}')

