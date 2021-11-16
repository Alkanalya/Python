# Сделать вводимый через input() список, не создавая полноценный парсер, не смог :(.
# А возможно ли такое?...

my_list = [None, 'zero', 1, {2, 'two'}, ("three", 3), {'four': 4}, b'5', False]
for item in my_list:
    print(type(item))
