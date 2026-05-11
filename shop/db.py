import sqlite3

def connect():
    return sqlite3.connect("database.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # Items table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    # Bills table (UPDATED)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER,
        total_price REAL,
        quantity REAL,
        unit TEXT,
        price_per_unit REAL,
        date TEXT,
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
    """)

    conn.commit()
    conn.close()