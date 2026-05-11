import sqlite3
import random
import string
from datetime import datetime

class BookingService:
    def __init__(self, tickets_db, trains_db):
        self.tickets_db = tickets_db
        self.trains_db  = trains_db

    def _gen_pnr(self):
        return ''.join(random.choices(string.digits, k=10))

    def search_trains(self, source, destination):
        conn = sqlite3.connect(self.trains_db)
        c = conn.cursor()
        c.execute("""
            SELECT train_code, name, source, destination, departure, arrival, duration,
                   fare_1A, fare_2A, fare_3A, fare_SL, fare_CC, fare_2S, fare_EC
            FROM trains
            WHERE UPPER(source)=UPPER(?) AND UPPER(destination)=UPPER(?)
        """, (source, destination))
        rows = c.fetchall()
        conn.close()
        return rows

    def get_available_classes(self, train_code):
        conn = sqlite3.connect(self.trains_db)
        c = conn.cursor()
        c.execute("SELECT class, available FROM seat_availability WHERE train_code=? AND available>0", (train_code,))
        rows = c.fetchall()
        conn.close()
        return rows  # [(class, seats_left), ...]

    def get_fare(self, train_code, cls):
        col_map = {"1A":"fare_1A","2A":"fare_2A","3A":"fare_3A","SL":"fare_SL","CC":"fare_CC","2S":"fare_2S","EC":"fare_EC"}
        col = col_map.get(cls)
        if not col:
            return 0
        conn = sqlite3.connect(self.trains_db)
        c = conn.cursor()
        c.execute(f"SELECT {col} FROM trains WHERE train_code=?", (train_code,))
        row = c.fetchone()
        conn.close()
        return row[0] if row else 0

    def book_ticket(self, username, passenger, age, train_code, travel_date, cls, seats):
        # Check availability
        conn_t = sqlite3.connect(self.trains_db)
        ct = conn_t.cursor()
        ct.execute("SELECT available FROM seat_availability WHERE train_code=? AND class=?", (train_code, cls))
        row = ct.fetchone()
        if not row or row[0] < seats:
            conn_t.close()
            return False, "Not enough seats available."

        # Get train info
        ct.execute("SELECT name, source, destination FROM trains WHERE train_code=?", (train_code,))
        tr = ct.fetchone()
        train_name, src, dst = tr

        fare_per_seat = self.get_fare(train_code, cls)
        total_fare = fare_per_seat * seats

        # Deduct seats
        ct.execute("UPDATE seat_availability SET available=available-? WHERE train_code=? AND class=?",
                   (seats, train_code, cls))
        conn_t.commit()
        conn_t.close()

        # Insert ticket
        pnr = self._gen_pnr()
        booked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("""
            INSERT INTO tickets (pnr, username, passenger, age, train_code, train_name,
                                 source, destination, travel_date, class, seats, fare, status, booked_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (pnr, username, passenger, age, train_code, train_name, src, dst,
              travel_date, cls, seats, total_fare, "CONFIRMED", booked_at))
        conn.commit()
        conn.close()
        return True, pnr

    def get_pnr_status(self, pnr):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("SELECT * FROM tickets WHERE pnr=?", (pnr,))
        row = c.fetchone()
        conn.close()
        return row

    def cancel_ticket(self, pnr, username):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("SELECT status, train_code, class, seats, username FROM tickets WHERE pnr=?", (pnr,))
        row = c.fetchone()
        if not row:
            conn.close()
            return False, "PNR not found."
        status, train_code, cls, seats, owner = row
        if owner != username:
            conn.close()
            return False, "You can only cancel your own tickets."
        if status == "CANCELLED":
            conn.close()
            return False, "Ticket already cancelled."
        c.execute("UPDATE tickets SET status='CANCELLED' WHERE pnr=?", (pnr,))
        conn.commit()
        conn.close()

        # Restore seats
        conn_t = sqlite3.connect(self.trains_db)
        ct = conn_t.cursor()
        ct.execute("UPDATE seat_availability SET available=available+? WHERE train_code=? AND class=?",
                   (seats, train_code, cls))
        conn_t.commit()
        conn_t.close()
        return True, "Ticket cancelled successfully. Refund will be processed."

    def get_user_tickets(self, username):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("SELECT * FROM tickets WHERE username=? ORDER BY booked_at DESC", (username,))
        rows = c.fetchall()
        conn.close()
        return rows

    def get_all_tickets(self):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("SELECT * FROM tickets ORDER BY booked_at DESC")
        rows = c.fetchall()
        conn.close()
        return rows
