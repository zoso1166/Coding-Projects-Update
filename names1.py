#Names1 by James Page 3/29/2020

import sqlite3

conn = sqlite3.connect('fnames.sqlite')
cur = conn.cursor()
conn = sqlite3.connect('lnames.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS fnames
    (id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS lnames
    (from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

while True:
    fname = input('Enter a first name, or quit: ')
    if (fname == 'quit'): break
    lname = input('Enter a last name, or quit: ')
    if (lname == 'quit'): break
   