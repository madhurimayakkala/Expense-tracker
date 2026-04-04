Expense Tracker

A simple web-based expense tracker built using Flask.
It lets you record, manage, and view your daily expenses.

Features
add and delete expenses
store data in a database
simple UI using HTML templates
lightweight and fast
Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS (Jinja templates)
Database: SQLite
Project Structure
expense-tracker/
│── app.py
│── expenses.db
│── schema.sql
│── requirements.txt
│── templates/
│── static/
Setup
# create virtual environment (optional but recommended)
python -m venv .venv

# activate it
# windows:
.venv\Scripts\activate
# mac/linux:
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the app
python app.py
Notes

This project was built to understand backend development using Flask and working with databases.
