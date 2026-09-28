from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "✅ Chal raha hai!", "status": "success"})

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    return jsonify({
        "message": "✅ Signup Success!",
        "name": data.get("name"),
        "email": data.get("email")
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({
        "message": "✅ Login Success!",
        "email": data.get("email")
    })

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
