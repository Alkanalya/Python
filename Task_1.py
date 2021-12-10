class Date():
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def make_date(cls, self):
        raw_date = self.split('-')
        try:
            day = int(raw_date[0])
            month = int(raw_date[1])
            year = int(raw_date[2])
        except TypeError:
            print('Неверный ввод данных.')
        else:
            return [day, month, year]

    @staticmethod
    def check_date(date_list):
        if 0 < date_list[2] < 2022:
            if (date_list[1] in [i for i in range(1, 13, 2)] or date_list[1] == 12) and (1 <= date_list[0] <= 31):
                print("It's OK")
            elif date_list[1] in [i for i in range(4, 11, 2)] and (1 <= date_list[0] <= 30):
                print("It's OK")
            elif date_list[1] == 2 and (1 <= date_list <= 28):
                print("It's OK")
            else:
                print("Wrong date.")
        else:
            print("Wrong date.")


Date.check_date(Date.make_date("31-12-2021"))
