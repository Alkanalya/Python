class Car():
    def __init__(self, name,  color):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, speed):
        print("Поехали!")
        self.speed = speed

    def stop(self):
        print("Остановка")
        self.speed = 0

    def turn(self, direction):
        print(f'Поворот {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')

class WorkCar(Car):
    def show_speed(self):
        print(f'{self.speed} км/ч')
        if self.speed > 40:
            print('Превышение скорости!')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, name, color):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


print('Введите через пробел название машины, цвет и тип машины:')
print('1 - Гражданская машина')
print('2 - Рабочая машина')
print('3 - Спортивная машина')
print('4 - Рабочая машина')

car_params = input().split()

match int(car_params[2]):
    case 1:
        car = TownCar(car_params[0], car_params[1])
    case 2:
        car = WorkCar(car_params[0], car_params[1])
    case 3:
        car = SportCar(car_params[0], car_params[1])
    case 4:
        car = PoliceCar(car_params[0], car_params[1])

print()
print('Команды для машины:')
print('go __ - начать движение со скоростью __ (целое число, км/ч)')
print('stop - остановиться')
print('turn __ - повернуть __(написать сторону)')
print('show speed - показать скорость')
print('exit - выход из программы')

while True:
    commnds = input().split()
    match commnds[0]:
        case 'go':
            car.go(int(commnds[1]))
        case 'stop':
            if car.speed == 0:
                print('Машина уже стоит.')
            else:
                car.stop()
        case 'turn':
            if car.speed == 0:
                print('Не могу повернуть, скорость равна нулю')
            else:
                car.turn(commnds[1])
        case 'show':
            car.show_speed()
        case 'exit':
            break
