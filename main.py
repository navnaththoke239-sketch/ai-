from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(_name_)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "✅ AI Studio Chal raha hai!", "status": "live"})

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    return jsonify({"message": "✅ Signup received", "data": data})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "")
    return jsonify({"reply": f"आपण म्हणालात: {msg}"})

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
