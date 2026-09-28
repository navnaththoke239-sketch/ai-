from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# ========== मुख्य पेज ==========
@app.route("/")
def home():
    return jsonify({"message": "✅ Chal raha hai!", "status": "success"})

# ========== साइनअप ==========
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        
        if not name or not email or not password:
            return jsonify({"error": "सर्व माहिती भरा"}), 400
        
        print(f"साइनअप आले: नाव={name}, ईमेल={email}")
        return jsonify({
            "message": "✅ साइनअप यशस्वी!",
            "name": name,
            "email": email
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== लॉगिन ==========
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")
        
        if not email or not password:
            return jsonify({"error": "ईमेल आणि पासवर्ड भरा"}), 400
        
        return jsonify({
            "message": "✅ लॉगिन यशस्वी!",
            "email": email
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
