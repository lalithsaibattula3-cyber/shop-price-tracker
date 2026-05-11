import sqlite3

def init_tickets_db(path):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            pnr         TEXT PRIMARY KEY,
            username    TEXT,
            passenger   TEXT,
            age         INTEGER,
            train_code  INTEGER,
            train_name  TEXT,
            source      TEXT,
            destination TEXT,
            travel_date TEXT,
            class       TEXT,
            seats       INTEGER,
            fare        INTEGER,
            status      TEXT DEFAULT 'CONFIRMED',
            booked_at   TEXT
        )
    """)
    conn.commit()
    conn.close()
