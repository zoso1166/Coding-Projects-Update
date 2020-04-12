word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 11
print(d)