import sqlite3

def init_db():
    conn = sqlite3.connect("data/threats.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logs (ip TEXT, result TEXT)")
    conn.commit()
    conn.close()

def save_result(ip, result):
    conn = sqlite3.connect("data/threats.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?,?)", (ip, str(result)))
    conn.commit()
    conn.close()
