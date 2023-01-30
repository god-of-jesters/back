import sqlite3

def ins(mes: int):
    d = sqlite3.connect('serv.db')
    cur = d.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(int id, string name)")
    cur.execute(f"INSERT INTO users VALUES({mes}, 'АГЫВШ')")
    d.commit()
    return "Goood"
