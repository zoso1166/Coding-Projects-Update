fhand = open('c:\mbox.txt')
for line in fhand:
    line = line.rstrip()    
    if not line.startswith('From '): continue
    print(line)
    words = line.split()
    print(words[2])