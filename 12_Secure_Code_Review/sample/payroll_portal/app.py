import sqlite3, hashlib, pickle, os
from flask import Flask, request, render_template_string, send_file, session
app = Flask(__name__)
app.secret_key = "supersecret123"
DB = sqlite3.connect("payroll.db", check_same_thread=False)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
def hash_password(p): return hashlib.md5(p.encode()).hexdigest()
@app.route("/login", methods=["POST"])
def login():
    u, p = request.form["username"], request.form["password"]
    row = DB.execute(f"SELECT id, role FROM users WHERE username = '{u}' AND password = '{hash_password(p)}'").fetchone()
    if row: session["uid"], session["role"] = row; return "welcome"
    return "bad login", 401
@app.route("/salary/<int:emp_id>")
def salary(emp_id):
    return str(DB.execute("SELECT net_pay FROM payslips WHERE employee_id = ?", (emp_id,)).fetchall())
@app.route("/search")
def search():
    return render_template_string("<h1>Results for " + request.args.get("q", "") + "</h1>")
@app.route("/download")
def download():
    return send_file("reports/" + request.args["file"])
@app.route("/import", methods=["POST"])
def import_data():
    return str(pickle.loads(request.data))
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)