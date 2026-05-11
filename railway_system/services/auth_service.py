import sqlite3

class AuthService:
    def __init__(self, db_path):
        self.db_path = db_path

    def login(self, username, password):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT id, username, role FROM users WHERE username=? AND password=?", (username, password))
        row = c.fetchone()
        conn.close()
        if row:
            return {"id": row[0], "username": row[1], "role": row[2]}
        return None

    def register(self, username, password):
        try:
            conn = sqlite3.connect(self.db_path)
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password, role) VALUES (?,?,?)", (username, password, "user"))
            conn.commit()
            conn.close()
            return True, "Registration successful!"
        except sqlite3.IntegrityError:
            return False, "Username already exists."

    def change_password(self, username, old_pw, new_pw):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, old_pw))
        if not c.fetchone():
            conn.close()
            return False, "Current password incorrect."
        c.execute("UPDATE users SET password=? WHERE username=?", (new_pw, username))
        conn.commit()
        conn.close()
        return True, "Password changed successfully."

    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT id, username, role FROM users")
        rows = c.fetchall()
        conn.close()
        return rows
