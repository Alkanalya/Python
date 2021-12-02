from time import sleep


class TraficLight:
    def __init__(self):
        self.__color = 'off'

    def running(self):
        for i in range(2):
            self.__color = '\33[31m red'
            print(self.__color)
            sleep(7)
            self.__color = '\33[31m red \33[0m & \33[33m yellow'
            print(self.__color)
            sleep(2)
            self.__color = '\33[32m green'
            print(self.__color)
            sleep(7)
            self.__color = '\33[33m yellow'
            print(self.__color)
        print('\33[0mЗавершение работы светофора')

light_1 = TraficLight()
print(f'The trafic light is {light_1._TraficLight__color}')
if input("Введите 'run' для запуска светофора\n") == 'run':
    light_1.running()

light_2 = TraficLight()
print(f'The trafic light is {light_2._TraficLight__color}')