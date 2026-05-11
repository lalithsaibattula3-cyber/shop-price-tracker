import sqlite3
import csv

# ✅ connect to DB in SAME folder
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ✅ create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctor_slots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor_name TEXT,
    area_of_specialization TEXT,
    timings_available TEXT,
    slot_datetime TEXT
)
""")

count = 0

# ✅ read csv (same folder)
with open("doctors.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        cursor.execute("""
            INSERT INTO doctor_slots 
            (doctor_name, area_of_specialization, timings_available, slot_datetime)
            VALUES (?, ?, ?, ?)
        """, row)
        count += 1

conn.commit()
conn.close()

print(f"Inserted {count} rows ✅")