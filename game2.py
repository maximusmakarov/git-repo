import random

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', \
             'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]

print(secret_word)


def print_list_as_string(arg):
   print(''.join(arg))


users_word = ['*'] * len(secret_word)
print_list_as_string(users_word)


while True:
   letter = input('введите букву слова: ')

   if len(letter) != 1 or not letter.isalpha():
       continue

   print(letter)
