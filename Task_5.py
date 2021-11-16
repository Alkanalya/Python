# Создание своего начального рейтинга. Но без сортировки :(
# Без сортировки требуется ввод по неубыванию.
'''raw_rating = input('Введите числа по неубыванию через пробел\n')
sliced_rating = raw_rating.split()
old_rating = []
for num in sliced_rating:
  old_rating.append(int(num))
print(old_rating)'''

# Но я сделал вставку для любых целых чисел :)
rating = [7, 6, 6, 4, 2, 1]
score = int(input('Введите новую оценку для рейтинга\n'))
for num in rating:
    if score > num:
        rating.insert(rating.index(num), score)
        break
    if rating.index(num) == len(rating) - 1:
        rating.append(score)
        break
print(rating)
