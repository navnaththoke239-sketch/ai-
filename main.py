from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
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

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Username and password required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Signup successful"
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Username and password required"
        }), 400

    return jsonify({
        "success": True,
        "message": "Login successful"
    })

# Online hosting साठी
if _name_ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
