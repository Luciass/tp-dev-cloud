from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Bienvenue sur votre app Flask hébergée sur Render !</h2>"

@app.route('/hello', methods=['GET'])
def hello():
    return {"message": "Bonjour depuis Render Flask API"}
