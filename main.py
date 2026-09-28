from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "AI Video App Backend is running"
    })

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json() or {}

    return jsonify({
        "success": True,
        "message": "Signup successful",
        "name": data.get("name"),
        "email": data.get("email")
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    return jsonify({
        "success": True,
        "message": "Login successful",
        "email": data.get("email")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
