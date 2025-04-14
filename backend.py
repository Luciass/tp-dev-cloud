
from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

FIREBASE_DB_URL = "https://tp-cloud-14-04-25-default-rtdb.europe-west1.firebasedatabase.app/messages.json"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/envoyer', methods=['POST'])
def envoyer():
    data = request.get_json()
    response = requests.post(FIREBASE_DB_URL, json=data)
    if response.ok:
        return jsonify({"status": "envoyé"}), 200
    return jsonify({"status": "échec", "detail": response.text}), 500

@app.route('/messages', methods=['GET'])
def messages():
    response = requests.get(FIREBASE_DB_URL)
    if response.ok:
        return jsonify(response.json()), 200
    return jsonify({"error": "Erreur de lecture"}), 500

@app.route('/logs')
def get_logs():
    with open('logs.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
