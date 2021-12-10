class UnlimError(Exception):
    def __init__(self, text):
        self.text = text


enter = list(map(int, input('Введите два числа через пробел:\n').split()))
try:
    if enter[1] == 0:
        raise UnlimError('На ноль сегодня делить нельзя.')
    res = enter[0] / enter[1]
except UnlimError as err:
    print(err)
else:
    print(res)
