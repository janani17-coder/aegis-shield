import os
import sqlite3
from flask import Flask, request, session
from werkzeug.security import check_password_hash

app = Flask(__name__)

# Read the secret from an environment variable.
app.secret_key = os.environ["FLASK_SECRET_KEY"]

DB = sqlite3.connect("payroll.db", check_same_thread=False)


def login():
    username = request.form["username"]
    password = request.form["password"]

    row = DB.execute(
        "SELECT id, role, password_hash FROM users WHERE username = ?",
        (username,)
    ).fetchone()

    if row and check_password_hash(row[2], password):
        session["uid"] = row[0]
        session["role"] = row[1]
        return "welcome"

    return "bad login", 401