# Historgram

user_word = input('Enter a word: ')

word = user_word
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
           
print(d)