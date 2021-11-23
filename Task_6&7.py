def int_func(word):
    first_char = ord(word[0])
    new_word = chr(first_char - 32) + word[1:]
    return new_word

list_of_words = input('Введите слова через пробел\n').split()
print(list_of_words)
bad_words = []
for word in list_of_words:
    for char in word:
        if (ord(char) < 97) or (ord(char) > 122):
            bad_words.append(word)
            break

for word in bad_words:
    list_of_words.remove(word)

for word in list_of_words:
    print(int_func(word))
