import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/import", methods=["POST"])
def import_data():
    try:
        data = json.loads(request.data)

        if not isinstance(data, (dict, list)):
            return jsonify({"error": "Invalid data format"}), 400

        return jsonify({
            "status": "success",
            "message": "JSON data received"
        }), 200

    except (json.JSONDecodeError, UnicodeDecodeError):
        return jsonify({"error": "Invalid JSON"}), 400