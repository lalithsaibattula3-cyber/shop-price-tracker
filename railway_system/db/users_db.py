import sqlite3

def init_users_db(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role     TEXT DEFAULT 'user'
        )
    """)
    # Default admin account
    c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?,?,?)",
              ("admin", "admin123", "admin"))
    conn.commit()
    conn.close()
