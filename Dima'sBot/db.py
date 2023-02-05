import sqlite3

def ins(mes: int, name: str, surname: str, d, cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, surname TEXT)")
    cur.execute(f"INSERT INTO users VALUES({mes}, '{name}', '{surname}')")
    d.commit()
    return "Goood"

def try_reg(id,cur):
    data = cur.execute("SELECT * FROM users").fetchall()
    ids = []
    for i in data:
        ids.append(i[0])
    return id in ids