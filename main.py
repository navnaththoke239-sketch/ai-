from flask import Flask, jsonify

app = Flask(_name_)

@app.route("/")
def home():
    return jsonify({"message": "✅ Chal raha hai!", "status": "success"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
