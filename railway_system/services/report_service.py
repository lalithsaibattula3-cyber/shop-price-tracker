import sqlite3

class ReportService:
    def __init__(self, tickets_db):
        self.tickets_db = tickets_db

    def get_summary(self):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM tickets WHERE status='CONFIRMED'")
        confirmed = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM tickets WHERE status='CANCELLED'")
        cancelled = c.fetchone()[0]
        c.execute("SELECT SUM(fare) FROM tickets WHERE status='CONFIRMED'")
        revenue = c.fetchone()[0] or 0
        c.execute("SELECT SUM(seats) FROM tickets WHERE status='CONFIRMED'")
        passengers = c.fetchone()[0] or 0
        conn.close()
        return {"confirmed": confirmed, "cancelled": cancelled, "revenue": revenue, "passengers": passengers}

    def get_train_report(self):
        conn = sqlite3.connect(self.tickets_db)
        c = conn.cursor()
        c.execute("""
            SELECT train_name, train_code, COUNT(*) as bookings, SUM(seats) as passengers, SUM(fare) as revenue
            FROM tickets WHERE status='CONFIRMED'
            GROUP BY train_code ORDER BY bookings DESC
        """)
        rows = c.fetchall()
        conn.close()
        return rows
