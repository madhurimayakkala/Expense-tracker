print("▶ app.py is running")
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Ensure the table exists no matter how the app is started (python app.py or flask run)

def fetchall(q, args=()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(q, args)
    rows = cur.fetchall()
    conn.close()
    return rows

def exec_q(q, args=()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(q, args)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    expenses = fetchall("SELECT * FROM expenses ORDER BY date DESC")
    data = fetchall("SELECT category, SUM(amount) FROM expenses GROUP BY category")

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#8A2BE2', '#00FA9A', '#FF7F50']

    return render_template("index.html",
                           expenses=expenses, labels=labels, values=values, colors=colors)

@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form["title"]
    amount = float(request.form["amount"])
    category = request.form["category"]
    exec_q("INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
           (title, amount, category))
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_expense(id):
    exec_q("DELETE FROM expenses WHERE id = ?", (id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    print("▶ init_db() about to run")
    try:
        init_db()
        print("✅ Database initialized successfully!")
    except Exception as e:
        print("❌ init_db() failed:", e)

    print("▶ starting Flask server...")
    try:
        app.run(debug=True)
    except Exception as e:
        print("❌ Flask failed to start:", e)
