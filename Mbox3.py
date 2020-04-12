fhand = open('c:\mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    newline = line.upper()
    print(newline)