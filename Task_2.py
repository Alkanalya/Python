def info(name, surname, day_of_birth, city, email, number):
  print(f"\n{name.capitalize()} {surname.capitalize()}, {day_of_birth} г.р., {city}, e-mail: {email}, Номер телефона: {number}")

arg_1 = input('Введите информацию о человеке.\nИмя: ')
arg_2 = input('Фамилия: ')
arg_3 = input('День Рождения: ')
arg_4 = input('Город проживания: ')
arg_5 = input('E-mail: ')
arg_6 = input('Номер телефона: ')

info(city=arg_4, surname=arg_2, day_of_birth=arg_3, email=arg_5, name=arg_1, number=arg_6)