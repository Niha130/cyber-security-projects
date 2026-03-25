import sqlite3
from config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS traffic (
            ip TEXT,
            count INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_traffic(ip, count):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO traffic VALUES (?,?)", (ip, count))
    conn.commit()
    conn.close()
