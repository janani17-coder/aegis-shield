from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return render_template("search.html", query=query)