import re
hand = open('c:/mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)