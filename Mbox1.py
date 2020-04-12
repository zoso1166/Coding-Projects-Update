fhand = open('c:\mbox.txt')

count = 0
for line in fhand:
    count = count + 1
    line = line.rstrip()

    if line.startswith('From:'):
        print(line)
        print('Line count: ', count)

    