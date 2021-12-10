class Storage():
    def __init__(self):
        self.data_base = {'Printers': [], 'Scaners': [], 'Xerox': []}
        self.log = []

    def show_info(self):
        print(f"Кол-во принтеров: {len(self.data_base['Printers'])}\nКол-во сканеров: {len(self.data_base['Scaners'])}\nКол-во ксероксов: {len(self.data_base['Xerox'])}\n")

    def get_into(self, obj):
        if type(obj) == Printer:
            self.data_base['Printers'].append(obj)
        elif type(obj) == Xerox:
            self.data_base['Xerox'].append(obj)
        elif type(obj) == Scaner:
            self.data_base['Scaners'].append(obj)
        else:
            print('Something goes wrong...')

    def send_to_subdiv(self, cls_name):
        self.data_base[cls_name].pop()

class Org_tech():
    def __init__(self, colour, model_name):
        self.colour = colour
        self.model = model_name

class Printer(Org_tech):
    def __init__(self, colour, model_name):
        self.colour = colour
        self.model = model_name
        self.can_print = True
        self.can_scan = False


class Xerox(Org_tech):
    def __init__(self, colour, model_name):
        self.colour = colour
        self.model = model_name
        self.can_print = True
        self.can_scan = True

class Scaner(Org_tech):
    def __init__(self, colour, model_name):
        self.colour = colour
        self.model = model_name
        self.can_print = False
        self.can_scan = True


my_store = Storage()

print('Добро пожаловать в управление складом:')
while True:
    print('---------------------------------------------------------------------------')
    print('Команды:')
    print("1.'Принять' - принять оргтехнику на склад")
    print("2.'Отправить' - отправить оргтехнику в подразделение")
    print("3.'Показать инфо' - показать количество оргтехники на складе")
    print("4.'Показать логи' - показать движение оргтехники по складу")
    print("5.'Выход' - выход из программы")
    enter = input()
    match enter:
        case 'Принять' | '1':
            print("Введите данные в формате: число тип")
            while True:
                in_store = input().split()
                new_item = None
                match in_store[1].lower():
                    case 'принтер'| 'принтеры' | 'принтеров' | 'printer' | 'printers':
                        new_item = Printer('default', 'default')
                    case 'сканер' | 'сканеры' | 'сканеров' |'scaner' | 'scaners':
                        new_item = Scaner('default', 'default')
                    case 'ксерокс'| 'ксероксы' | 'ксероксов'| 'xeroxes' | 'xerox':
                        new_item = Xerox('default', 'default')
                    case _:
                        print('Неверный тип оргтехники. Повторите ввод.')
                        continue
                try:
                    number = int(in_store[0])
                except TypeError:
                    print('Неверно введено число оргтехники. Повторите ввод. Для отмены команды введите число оргтехники, равном нулю.')
                    continue
                else:
                    if number < 0:
                        print('Количество принимаемой оргтехники не может быть меньше нуля.')
                        continue
                    elif number == 0:
                        continue
                    else:
                        for i in range(number):
                            my_store.get_into(new_item)
                        my_store.log.append(f'На склад прибыло {number} оргтехники, тип: {new_item.__class__.__name__}')
                        break
        case 'Отправить' | '2':
            print("Введите данные в формате: число тип подразделение")
            while True:
                out_store = input().split()
                new_item = None
                match out_store[1].lower():
                    case 'принтер'| 'принтеры' | 'принтеров' | 'printer' | 'printers':
                        cls_name = 'Printers'
                    case 'сканер' | 'сканеры' | 'сканеров' |'scaner' | 'scaners':
                        cls_name = 'Scaners'
                    case 'ксерокс'| 'ксероксы' | 'ксероксов'| 'xeroxes' | 'xerox':
                        cls_name = 'Xerox'
                    case _:
                        print('Неверный тип оргтехники. Повторите ввод.')
                        continue
                try:
                    number = int(out_store[0])
                except TypeError:
                    print('Неверно введено число оргтехники. Повторите ввод. Для отмены команды введите число оргтехники, равном нулю.')
                    continue
                else:
                    if number < 0:
                        print('Количество отправляемой оргтехники не может быть меньше нуля.')
                        continue
                    elif number == 0:
                        continue
                    elif number > len(my_store.data_base[cls_name]):
                        print('На складе нет такого количества данного типа оргтехники.')
                        continue
                    else:
                        for i in range(number):
                            my_store.send_to_subdiv(cls_name)
                        my_store.log.append(f'Со склада отправлено {number} оргтехники типа {cls_name} в подразделение {out_store[2]}')
                        break

        case 'Показать инфо' | '3':
            my_store.show_info()

        case 'Показать логи' | '4':
            if my_store.log == []:
                print('Движений на складе не было.')
            else:
                for text in my_store.log:
                    print(text)

        case 'Выход' | '5':
            break

        case _:
            print('Неверно введена команда. Повторите ввод.')
