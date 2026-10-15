
from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Aarav", "course": "AIML"},
    {"id": 2, "name": "Priya", "course": "CSE"}
]

@app.route("/")
def home():
    return jsonify({"students": students})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
