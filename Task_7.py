class ComplexNum():
    def __init__(self, number):
        a = []
        i = 0
        temp_1 = ''
        while True:
            temp_1 += number[i]
            if number[i + 1].isdecimal():
                i += 1
            else:
                self.re = int(temp_1)
                self.im = int(number[(i + 1):(len(number) - 1)].replace(' ', ''))
                break

ar = ComplexNum('-10 + 5i')
print(ar.re)
print(ar.im)

