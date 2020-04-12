import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
('My Way', 15))
cur.execute('UPDATE Tracks SET plays = 16 WHERE title = "My Way"')
conn.commit()

print('Tracks:')

cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
for row in cur:
    print(row)
    
'''cur.execute('SELECT * FROM Tracks WHERE title = "My Way"')
for row in cur:
    print(row)
        
cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()'''

cur.close()