class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'Карточка работника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Итоговая зарплата работника: {self._income["wage"] + self._income["bonus"]}')

worker_1 = Position("Виктор", "Цой", "Кочегар", 5000, 1000)
worker_2 = Position("Патрис", "Лумумба", "Президент", 100000, 1000000)
worker_3 = Position("Рокки", "Бальбоа", "Боксёр", 0, 20000)

worker_1.get_full_name()
print(f'Имя - {worker_1.name}\nФамилия - {worker_1.surname}\nДолжность - {worker_1.position}\nЗарплата = {worker_1._income["wage"]} + {worker_1._income["bonus"]}\n')
worker_1.get_total_income()

print('\n')
worker_2.get_full_name()
print(f'Имя - {worker_2.name}\nФамилия - {worker_2.surname}\nДолжность - {worker_2.position}\nЗарплата = {worker_2._income["wage"]} + {worker_2._income["bonus"]}\n')
worker_2.get_total_income()

print('\n')
worker_3.get_full_name()
print(f'Имя - {worker_3.name}\nФамилия - {worker_3.surname}\nДолжность - {worker_3.position}\nЗарплата = {worker_3._income["wage"]} + {worker_3._income["bonus"]}\n')
worker_3.get_total_income()