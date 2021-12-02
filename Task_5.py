class Stationery:
    def __init__(self):
        self.name

    def draw(self):
        print("Запуск отрисовки")

class Pen:
    def __init__(self):
        self.name = 'Ручка'

    def draw(self):
        print("Запуск отрисовки ручкой...\n")

class Pencil:
    def __init__(self):
        self.name = 'Карандаш'

    def draw(self):
        print("Запуск отрисовки карандашом...\n")

class Handle:
    def __init__(self):
        self.name = 'Маркер'

    def draw(self):
        print("Запуск отрисовки маркером...\n")

stat_1 = Pen()
stat_2 = Pencil()
stat_3 = Handle()

print(stat_1.name)
stat_1.draw()

print(stat_3.name)
stat_3.draw()

print(stat_2.name)
stat_2.draw()