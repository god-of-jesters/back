import sqlite3

d = sqlite3.connect('serv.db')
cur = d.cursor()
d.commit()
print(cur.execute("SELECT * FROM users").fetchone())