import sqlite3
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('admin','admin123')")

    conn.commit()
    conn.close()

def vulnerable_login(username, password):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executing:", query)

    c.execute(query)
    result = c.fetchone()

    conn.close()
    return result
