mport random

words_list = ['автострада', 'бензин', 'инопланетянин', 'самолет', 'библиотека', \
             'шайба', 'олимпиада']

secret_word = random.sample(words_list, 1)[0]

# print(help(random.sample))

print(secret_word)

