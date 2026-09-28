from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import pymongo
import openai
import replicate
import requests

load_dotenv()

app = Flask(_name_)
CORS(app)

# ========== MongoDB Connection ==========
MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["ai_studio"]
users_collection = db["users"]

# ========== API Keys ==========
openai.api_key = os.getenv("OPENAI_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# ========== Test Route ==========
@app.route("/")
def home():
    return jsonify({"message": "✅ AI Studio Backend Chalu Zala!", "status": "running"})

# ========== Signup ==========
@app.route("/signup", methods=["POST"])
def signup():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not all([name, email, password]):
            return jsonify({"error": "Sarv field bhara"}), 400

        if users_collection.find_one({"email": email}):
            return jsonify({"error": "Email already exist"}), 400

        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": password
        })
        return jsonify({"message": "✅ Signup Success!", "name": name}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== Login ==========
@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

        user = users_collection.find_one({"email": email, "password": password})
        if user:
            return jsonify({"message": "✅ Login Success!", "name": user["name"]}), 200
        return jsonify({"error": "Email ki password galat"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== Chat ==========
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_msg = data.get("message", "")

        if not user_msg:
            return jsonify({"error": "Message lihicha"}), 400

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_msg}]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== Generate Image ==========
@app.route("/generate-image", methods=["POST"])
def generate_image():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        output = replicate.run(
            "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21ffa62ad1519b3804",
            input={"prompt": prompt}
        )
        return jsonify({"image_url": output[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ========== Text to Speech ==========
@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    try:
        data = request.json
        text = data.get("text", "")

        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        res = requests.post(url, json={"text": text}, headers=headers)
        if res.status_code == 200:
            return jsonify({"audio": "✅ Generated"})
        return jsonify({"error": "Voice generation failed"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
