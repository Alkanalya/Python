raw_rating = input('Введите числа через пробел\n')
sliced_rating = raw_rating.split()
old_rating = []
for num in sliced_rating:
  old_rating.append(int(num))
print(old_rating)
# Дописать сортировку??

score = int(input('Введите новую оценку для рейтинга\n'))
i = 0
while (score < old_rating[i]) and (i < len(old_rating)):
  i = i + 1
old_rating.insert(i, score)
print(old_rating)