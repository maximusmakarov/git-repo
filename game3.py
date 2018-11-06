import random

MAX_ERRORS = 8

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', 'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]

# print(secret_word)


def print_list_as_string(arg):
   print(''.join(arg))


users_word = ['*'] * len(secret_word)
print_list_as_string(users_word)

errors_counter = 0

while True:
   letter = input('введите букву слова: ').lower()

   if len(letter) != 1 or not letter.isalpha():
       continue

   if letter in secret_word:
       for pos, char in enumerate(secret_word):
           if char == letter:
               # print(letter)
               users_word[pos] = letter
       if '*' not in users_word:
           print('вы выиграли!!!')
           break
   else:
       errors_counter += 1
       print(f'ошибок: {errors_counter}')

       if errors_counter == MAX_ERRORS:
           print('вы проиграли :(')
           break

   print_list_as_string(users_word)

