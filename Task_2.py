print("Введите время в секундах:")
sec = int(input())
hours = sec // 3600
if hours < 10:
    hours = '0' + str(hours)
sec = sec % 3600
minutes = sec // 60
if minutes < 10:
    minutes = '0' + str(minutes)
sec = sec % 60
if sec < 10:
    sec = '0' + str(sec)
print(f"{hours}:{minutes}:{sec}")
