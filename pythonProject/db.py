import sqlite3

def ins(mes: int, name: str, surname: str):
    d = sqlite3.connect('serv.db')
    cur = d.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INT, name TEXT, surname TEXT)")
    cur.execute(f"INSERT INTO users VALUES({mes}, '{name}', '{surname}')")
    d.commit()
    return "Goood"
