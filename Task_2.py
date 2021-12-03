from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def tiss_consump(self):
        pass

class Coat(Clothes):
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    @property
    def tiss_consump(self):
        return round(self.volume / 6.5 + 0.5)

class Costume(Clothes):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    @property
    def tiss_consump(self):
        return round(2 * self.height + 0.3)

clothes_1 = Coat('Манто', 10)
clothes_2 = Costume('Фрак', 20)

print(clothes_1.tiss_consump + clothes_2.tiss_consump)


# Введение своих данных о вещах и итогового расчёта ткани
print("Введите тип одежды ('пальто' или 'костюм'), название и размер/высоту")
print("Чтобы получить итоговый расчёт ткани, введите 'итого'")
print("Для выхода введите 'выход'")

all_clothes = 0
while True:
    enter = input().split()
    match enter[0]:
        case 'пальто':
            cloth = Coat(enter[1], int(enter[2]))
        case 'костюм':
            cloth = Costume(enter[1], int(enter[2]))
        case 'итого':
            print(all_clothes)
            continue
        case 'выход':
            break
        case _:
            print('Неверный ввод данных. Повторите ввод.')
            continue
    all_clothes += cloth.tiss_consump
    cloth = None