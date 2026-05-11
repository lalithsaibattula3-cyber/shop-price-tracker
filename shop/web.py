from flask import Flask, render_template, request
from datetime import datetime
from db import connect, create_tables

app = Flask(__name__)
create_tables()


# ---------------- LOGIN PAGE ----------------
@app.route("/")
def login():
    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    result = None

    if request.method == "POST":

        action = request.form.get("action")

        # If coming from login page
        if action is None:
            return render_template(
                "dashboard.html",
                result=result
            )

        conn = connect()
        cursor = conn.cursor()

        # ---------- ADD BILL ----------
        if action == "add":

            name = request.form["name"]
            total_price = float(
                request.form["price"]
            )

            quantity = float(
                request.form["quantity"]
            )

            unit = request.form["unit"]

            date = datetime.now().strftime(
                "%Y-%m-%d %I:%M %p"
            )

            price_per_unit = (
                total_price / quantity
            )

            cursor.execute(
                "SELECT id FROM items WHERE name = ?",
                (name,)
            )

            res = cursor.fetchone()

            if res:
                item_id = res[0]

            else:
                cursor.execute(
                    """
                    INSERT INTO items (name)
                    VALUES (?)
                    """,
                    (name,)
                )

                item_id = cursor.lastrowid

            cursor.execute("""
                INSERT INTO bills
                (
                    item_id,
                    total_price,
                    quantity,
                    unit,
                    price_per_unit,
                    date
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                item_id,
                total_price,
                quantity,
                unit,
                price_per_unit,
                date
            ))

            conn.commit()

            result = (
                "Bill added successfully ✅"
            )

        # ---------- SEARCH ITEM ----------
        elif action == "search":

            name = request.form[
                "search_name"
            ]

            cursor.execute("""
                SELECT
                    b.total_price,
                    b.date,
                    b.price_per_unit,
                    b.unit
                FROM bills b
                JOIN items i
                ON b.item_id = i.id
                WHERE LOWER(i.name)=LOWER(?)
                ORDER BY b.date DESC
                LIMIT 1
            """, (name,))

            data = cursor.fetchone()

            if data:
                result = {
                    "total": data[0],
                    "date": data[1],
                    "ppu": data[2],
                    "unit": data[3]
                }

            else:
                result = (
                    "Item not found ❌"
                )

        conn.close()

    return render_template(
        "dashboard.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)